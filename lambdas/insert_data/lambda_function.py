import json
import boto3
import urllib

def lambda_handler(event, context):
    s3_file_name = event['Records'][0]['s3']['object']['key']
    s3_file_name = urllib.parse.unquote(s3_file_name).replace('+', ' ')
    print(f"File received: {s3_file_name}")  
    
    if "hired_employees" in s3_file_name:
        table_name = "hired_employees"
    elif "departments" in s3_file_name:
        table_name = "departments"
    elif "jobs" in s3_file_name:
        table_name = "jobs"
    else:
        raise Exception(f"Unknown CSV file structure: {s3_file_name}")
    
    print(f"Table: {table_name}") 

    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = s3.get_object(Bucket=bucket, Key=s3_file_name)['Body'].read().decode('utf-8').splitlines()

    print(f"CSV file read successfully. Number of rows: {len(csv_file) - 1}")

    # Prueba final antes de insertar en la base de datos
    return {"statusCode": 200, "body": f"File {s3_file_name} processed correctly. They will be inserted into {table_name}."}
