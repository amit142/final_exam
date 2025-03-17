from flask import Flask, render_template_string, jsonify
import boto3
import os
from botocore.exceptions import ClientError, NoCredentialsError

app = Flask(__name__)
app.debug = True

# HTML template for the main page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>AWS Resource Monitor</title>
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
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .section {
            margin-bottom: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
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
    <div class="container">
        <h1>AWS Resource Monitor</h1>
        
        <div class="section">
            <h2>EC2 Instances</h2>
            <table>
                <tr>
                    <th>Instance ID</th>
                    <th>Instance Type</th>
                    <th>State</th>
                    <th>Public IP</th>
                    <th>Private IP</th>
                </tr>
                {% for instance in ec2_instances %}
                <tr>
                    <td>{{ instance.id }}</td>
                    <td>{{ instance.instance_type }}</td>
                    <td>{{ instance.state.get('Name', 'Unknown') }}</td>
                    <td>{{ instance.public_ip_address or 'N/A' }}</td>
                    <td>{{ instance.private_ip_address or 'N/A' }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="section">
            <h2>VPCs</h2>
            <table>
                <tr>
                    <th>VPC ID</th>
                    <th>CIDR Block</th>
                    <th>Is Default</th>
                    <th>State</th>
                </tr>
                {% for vpc in vpcs %}
                <tr>
                    <td>{{ vpc.id }}</td>
                    <td>{{ vpc.cidr_block }}</td>
                    <td>{{ vpc.is_default }}</td>
                    <td>{{ vpc.state }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="section">
            <h2>Load Balancers</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>DNS Name</th>
                    <th>Type</th>
                    <th>Scheme</th>
                </tr>
                {% for lb in load_balancers %}
                <tr>
                    <td>{{ lb.get('LoadBalancerName', 'N/A') }}</td>
                    <td>{{ lb.get('DNSName', 'N/A') }}</td>
                    <td>{{ lb.get('Type', 'N/A') }}</td>
                    <td>{{ lb.get('Scheme', 'N/A') }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
        
        <div class="section">
            <h2>AMIs</h2>
            <table>
                <tr>
                    <th>AMI ID</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>State</th>
                </tr>
                {% for ami in amis %}
                <tr>
                    <td>{{ ami.id }}</td>
                    <td>{{ ami.name or 'N/A' }}</td>
                    <td>{{ ami.description or 'N/A' }}</td>
                    <td>{{ ami.state }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    try:
        ec2_resource = boto3.resource('ec2')
        ec2_instances = list(ec2_resource.instances.all())
        return render_template_string(
            HTML_TEMPLATE,
            ec2_instances=ec2_instances
        )
    except (ClientError, NoCredentialsError) as e:
        return jsonify({
            "status": "warning",
            "message": "Application is running but AWS credentials are not configured correctly",
            "error": str(e)
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
