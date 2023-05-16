import uuid

import pika


def on_response_message_received(ch, method, properties, body):
    print(f'response received: {body}')


connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

response_queue = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=response_queue.method.queue, auto_ack=True,
                      on_message_callback=on_response_message_received)

channel.queue_declare(queue='request-queue')

message = 'Can I request a response?'
cor_id = str(uuid.uuid4())

message_properties = pika.BasicProperties(
    reply_to=response_queue.method.queue,
    correlation_id=cor_id,
)

channel.basic_publish(exchange='',
                      routing_key='request-queue',
                      body=message,
                      properties=message_properties)
print('message sent')

print('Client Started')
channel.start_consuming()
