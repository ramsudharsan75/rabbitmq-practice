import pika
from pika.exchange_type import ExchangeType

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='secondexchange',
                         exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='letterbox')

channel.queue_bind('letterbox', 'secondexchange')


def on_message_callback(ch, method, properties, message):
    print(f'Message received {message}')


channel.basic_consume(queue='letterbox', auto_ack=True,
                      on_message_callback=on_message_callback)


print('Started consuming')
channel.start_consuming()
