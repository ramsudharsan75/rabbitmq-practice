import pika
from pika.exchange_type import ExchangeType


def on_message1_callback(ch, method, properties, message):
    print(f'Message 1 received {message}')


def on_message2_callback(ch, method, properties, message):
    print(f'Message 2 received {message}')


connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='consistenthashing',
                         exchange_type='x-consistent-hash')

channel.queue_declare(queue='letterbox1')

channel.queue_bind('letterbox1',
                   'consistenthashing',
                   routing_key='1')

channel.queue_declare(queue='letterbox2')

channel.queue_bind('letterbox2',
                   'consistenthashing',
                   routing_key='2')

channel.basic_consume(queue='letterbox1', auto_ack=True,
                      on_message_callback=on_message1_callback)


channel.basic_consume(queue='letterbox2', auto_ack=True,
                      on_message_callback=on_message2_callback)

print('Started consuming')
channel.start_consuming()
