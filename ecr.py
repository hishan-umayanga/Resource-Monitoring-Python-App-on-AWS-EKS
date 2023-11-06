import boto3

client = boto3.client('ecr') #make private Amazon ECR

response = client.create_repository(repositoryName="my-cloud-native-repo")

repository_uri =  response['repository']['repositoryUri']
print(repository_uri)