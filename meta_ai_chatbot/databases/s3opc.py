import boto3
import json
from datetime import datetime
from config import AWS_REGION, S3_BUCKET_NAME

# Conectar con S3
def create_s3_client(region_name=AWS_REGION):
    session = boto3.Session(region_name=region_name)
    s3_client = session.client('s3')
    return s3_client

def backup_to_s3(session_id, data):
    """Almacena una copia de seguridad de los datos en S3."""
    s3 = create_s3_client()
    backup_data = json.dumps(data)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'chatbot_backups/chatbot_backup_{session_id}_{timestamp}.json'

    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=file_name,
        Body=backup_data,
        ContentType='application/json'
    )
    print(f"Copia de seguridad creada en S3: {file_name}")
