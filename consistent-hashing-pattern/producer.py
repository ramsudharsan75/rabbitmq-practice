import pika
from pika.exchange_type import ExchangeType

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_parameters = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='consistenthashing',
                         exchange_type="x-consistent-hash")

message = 'This message will be sent with headers'

routing_key = 'Please hash me again and again!'

channel.basic_publish(exchange='consistenthashing',
                      routing_key=routing_key,
                      body=message)

print(f'sent message: {message}')

connection.close()
