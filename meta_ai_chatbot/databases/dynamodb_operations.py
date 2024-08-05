import boto3
from config import AWS_REGION, DYNAMODB_CHAT_TABLE

# Conectar con DynamoDB
try:
    dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
    table = dynamodb.Table(DYNAMODB_CHAT_TABLE)
except Exception as e:
    print(f"Error al conectar con DynamoDB o acceder a la tabla: {e}")
    raise

def store_message(session_id, message_id, user_id, bot_id, message_text, sender_type, timestamp, intent=None, response_type=None):
    """Almacena un mensaje de un chatbot en DynamoDB."""
    try:
        response = table.put_item(
            Item={
                'SessionID': session_id,
                'MessageID': message_id,
                'UserID': user_id,  # ID anónimo del usuario
                'BotID': bot_id,
                'MessageText': message_text,
                'SenderType': sender_type,  # 'user' o 'bot'
                'Timestamp': timestamp,
                'Intent': intent,
                'ResponseType': response_type
            }
        )
        print(f"Mensaje guardado con éxito: {response}")
        return response
    except Exception as e:
        print(f"Error al almacenar el mensaje en DynamoDB: {e}")
        return None
