import pika
from pika.exchange_type import ExchangeType

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_parameters = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='headersexchange',
                         exchange_type=ExchangeType.headers)

message = 'This message will be sent with headers'

channel.basic_publish(exchange='headersexchange',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          headers={'name': 'Ram'}
                      )
                      )

print(f'sent message: {message}')

connection.close()
