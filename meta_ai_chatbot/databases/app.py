import uuid
from datetime import datetime
from dynamodb_operations import store_message
from s3_operations import backup_to_s3

# Función simulada para recibir mensajes del usuario
def receive_user_message(session_id, user_id, message_text):
    # Generar un ID de mensaje único
    message_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    
    # Guardar el mensaje en DynamoDB
    store_message(
        session_id=session_id,
        message_id=message_id,
        user_id=user_id,
        bot_id="ChatBotV1",
        message_text=message_text,
        sender_type="user",
        timestamp=timestamp
    )
    
    # Simular una respuesta del chatbot
    bot_response = "Gracias por tu mensaje."
    
    # Guardar la respuesta del bot en DynamoDB
    store_message(
        session_id=session_id,
        message_id=str(uuid.uuid4()),
        user_id=user_id,
        bot_id="ChatBotV1",
        message_text=bot_response,
        sender_type="bot",
        timestamp=datetime.now().isoformat()
    )
    
    # Opcional: Crear una copia de seguridad en S3
    backup_to_s3(session_id, {
        'UserMessage': message_text,
        'BotResponse': bot_response
    })
    
    return bot_response

# Ejemplo de uso
if __name__ == "__main__":
    session_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())  # ID anónimo del usuario
    print("Bot:", receive_user_message(session_id, user_id, "Hola, ¿cómo estás?"))
