import pika
from pika.exchange_type import ExchangeType

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_parameters = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange',
                         exchange_type=ExchangeType.topic)

user_payments_message = 'Routing message for user payment'

channel.basic_publish(exchange='mytopicexchange',
                      routing_key='user.payments', body=user_payments_message)

user_india_message = 'Routing message for user india'

channel.basic_publish(exchange='mytopicexchange',
                      routing_key='user.india', body=user_india_message)

print(f'sent messages')

connection.close()
