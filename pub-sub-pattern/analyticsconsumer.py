import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, message):
    print(f'Analytics service message received: {message}')


connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_parameters = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange',
                         exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='mytopicexchange', queue=queue.method.queue,
                   routing_key='*.india')

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
                      on_message_callback=on_message_received)

print('Started consuming')
channel.start_consuming()
