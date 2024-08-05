import boto3

# Conectar con DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# Crear la tabla
response = dynamodb.create_table(
    TableName='ChatbotMessages',
    KeySchema=[
        {
            'AttributeName': 'SessionID',
            'KeyType': 'HASH'  # Clave de partición
        },
        {
            'AttributeName': 'MessageID',
            'KeyType': 'RANGE'  # Clave de ordenación
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'SessionID',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'MessageID',
            'AttributeType': 'S'
        }
    ],
    BillingMode='PAY_PER_REQUEST'  # Facturación bajo demanda
)

print("Tabla creada con éxito:", response['TableDescription']['TableName'])
