#Notas a considerar
#Se deben activar los permisos de S3 y Dynamodb en la credencial de usuario que se creo
#AmazonDynamoDBFullAccess y AmazonS3FullAccess son los permisos que debe tener
#El testeo fue con un ejemplo basico, falta aplicarlo con el verdadero
#Guarda los documentos en json y estos se almacenan en un bucket de s3
#Checar si se guardo la informacion se puede usar este comando 'aws dynamodb scan --table-name ChatbotMessages --region us-east-1' (sin las commillas)
#Crear un bucket si no esta creado, este se llamo 'bucketchatroom'
import boto3
from datetime import datetime
from config import AWS_REGION, DYNAMODB_CHAT_TABLE, S3_BUCKET_NAME
from dynamodb_operations import store_message
from s3opc import backup_to_s3

def test_dynamodb_connection():
    """Prueba la conexión con DynamoDB y verifica la existencia de la tabla."""
    try:
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
        table = dynamodb.Table(DYNAMODB_CHAT_TABLE)
        print("Conexión a DynamoDB establecida correctamente.")

        # Obtener los primeros elementos de la tabla para verificar que funciona
        response = table.scan(Limit=1)
        print("Contenido de la tabla:", response['Items'])
    except Exception as e:
        print(f"Error en la conexión con DynamoDB: {e}")

def main():
    """Función principal del chatbot."""
    # Aquí puedes agregar la lógica principal del chatbot
    print("Ejecutando el chatbot...")

    # Ejemplo de almacenamiento de un mensaje
    session_id = '123456'
    message_id = 'msg001'
    user_id = 'anon_user'
    bot_id = 'bot001'
    message_text = 'Hola, ¿cómo puedo ayudarte?'
    sender_type = 'bot'
    timestamp = datetime.now().isoformat()

    try:
        response = store_message(
            session_id=session_id,
            message_id=message_id,
            user_id=user_id,
            bot_id=bot_id,
            message_text=message_text,
            sender_type=sender_type,
            timestamp=timestamp
        )
        print("Mensaje almacenado en DynamoDB:", response)
    except Exception as e:
        print(f"Error al almacenar el mensaje en DynamoDB: {e}")

    # Ejemplo de copia de seguridad a S3
    chat_data = {
        'session_id': session_id,
        'messages': [
            {
                'message_id': message_id,
                'user_id': user_id,
                'bot_id': bot_id,
                'message_text': message_text,
                'sender_type': sender_type,
                'timestamp': timestamp
            }
        ]
    }

    try:
        backup_to_s3(session_id, chat_data)
    except Exception as e:
        print(f"Error al realizar la copia de seguridad en S3: {e}")

if __name__ == "__main__":
    # Ejecuta la función de prueba y luego la función principal
    test_dynamodb_connection()
    main()
