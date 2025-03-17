import os
import boto3
from flask import Flask, render_template_string

app = Flask(__name__)

# Fetch AWS credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = "us-east-1"

# Initialize Boto3 clients
session = boto3.Session(
   aws_access_key_id=AWS_ACCESS_KEY,
   aws_secret_access_key=AWS_SECRET_KEY,
   region_name=REGION
)
ec2_client = session.client("ec2")
elbv2_client = session.client("elbv2")  # Application and Network Load Balancers
elb_client = session.client("elb")      # Classic Load Balancers

@app.route("/")
def home():
   # Fetch EC2 instances
   instances = ec2_client.describe_instances()
   instance_data = []
   for reservation in instances["Reservations"]:
       for instance in reservation["Instances"]:
           instance_data.append({
               "ID": instance["InstanceId"],
               "State": instance["State"]["Name"],
               "Type": instance["InstanceType"],
               "Public IP": instance.get("PublicIpAddress", "N/A")
           })
  
   # Fetch VPCs
   vpcs = ec2_client.describe_vpcs()
   vpc_data = [{"VPC ID": vpc["VpcId"], "CIDR": vpc["CidrBlock"]} for vpc in vpcs["Vpcs"]]
  
   # Fetch Load Balancers (both classic and v2)
   # Get Application and Network Load Balancers
   lb_data = []
   try:
       elbv2_lbs = elbv2_client.describe_load_balancers()
       for lb in elbv2_lbs.get("LoadBalancers", []):
           lb_data.append({
               "LB Name": lb.get("LoadBalancerName", "N/A"),
               "DNS Name": lb.get("DNSName", "N/A"),
               "Type": lb.get("Type", "ALB/NLB")
           })
   except Exception as e:
       print(f"Error fetching ALB/NLB: {e}")
   
   # Get Classic Load Balancers
   try:
       classic_lbs = elb_client.describe_load_balancers()
       for lb in classic_lbs.get("LoadBalancerDescriptions", []):
           lb_data.append({
               "LB Name": lb.get("LoadBalancerName", "N/A"),
               "DNS Name": lb.get("DNSName", "N/A"),
               "Type": "Classic"
           })
   except Exception as e:
       print(f"Error fetching Classic LB: {e}")
  
   # Fetch AMIs (only owned by the account)
   try:
       amis = ec2_client.describe_images(Owners=["self"])
       ami_data = [{"AMI ID": ami["ImageId"], "Name": ami.get("Name", "N/A")} for ami in amis.get("Images", [])]
   except Exception as e:
       print(f"Error fetching AMIs: {e}")
       ami_data = []
  
   # Render the result in a simple table
   html_template = """
   <html>
   <head>
       <title>AWS Resources</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               margin: 20px;
               background-color: #f5f5f5;
           }
           h1 {
               color: #333;
               text-align: center;
           }
           table {
               width: 100%;
               border-collapse: collapse;
               margin-bottom: 30px;
           }
           th, td {
               padding: 10px;
               border: 1px solid #ddd;
               text-align: left;
           }
           th {
               background-color: #f2f2f2;
           }
           tr:nth-child(even) {
               background-color: #f9f9f9;
           }
       </style>
   </head>
   <body>
       <h1>Running EC2 Instances</h1>
       <table>
           <tr><th>ID</th><th>State</th><th>Type</th><th>Public IP</th></tr>
           {% for instance in instance_data %}
           <tr><td>{{ instance['ID'] }}</td><td>{{ instance['State'] }}</td><td>{{ instance['Type'] }}</td><td>{{ instance['Public IP'] }}</td></tr>
           {% endfor %}
       </table>
      
       <h1>VPCs</h1>
       <table>
           <tr><th>VPC ID</th><th>CIDR</th></tr>
           {% for vpc in vpc_data %}
           <tr><td>{{ vpc['VPC ID'] }}</td><td>{{ vpc['CIDR'] }}</td></tr>
           {% endfor %}
       </table>
      
       <h1>Load Balancers</h1>
       <table>
           <tr><th>LB Name</th><th>DNS Name</th><th>Type</th></tr>
           {% for lb in lb_data %}
           <tr><td>{{ lb['LB Name'] }}</td><td>{{ lb['DNS Name'] }}</td><td>{{ lb['Type'] }}</td></tr>
           {% endfor %}
       </table>
      
       <h1>Available AMIs</h1>
       <table>
           <tr><th>AMI ID</th><th>Name</th></tr>
           {% for ami in ami_data %}
           <tr><td>{{ ami['AMI ID'] }}</td><td>{{ ami['Name'] }}</td></tr>
           {% endfor %}
       </table>
   </body>
   </html>
   """
  
   return render_template_string(html_template, instance_data=instance_data, vpc_data=vpc_data, lb_data=lb_data, ami_data=ami_data)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5001, debug=True)
