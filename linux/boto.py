import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

running_instances = []

for r in response['Reservations']:
    for i in r['Instances']:
        print('id:', i['InstanceId'], 'state:', i['State']['Name'])
        if(i['State']['Name']=='running'):
            running_instances.append(i['InstanceId'])

if(len(running_instances)>0):
    print('Stopping running instances')
    response = ec2.stop_instances(
        InstanceIds=running_instances
    )
    print('Successfully stoped Running Instances')   