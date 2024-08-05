# config.py

from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener variables de entorno
AWS_REGION = os.getenv('AWS_REGION')
DYNAMODB_CHAT_TABLE = 'ChatbotMessages'
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
