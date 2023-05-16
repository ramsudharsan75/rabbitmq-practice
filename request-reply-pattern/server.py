import pika


def on_request_message_received(ch, method, properties, body):
    print(f'request received: {properties.correlation_id} as {body}')
    message_properties = pika.BasicProperties(
        correlation_id=properties.correlation_id
    )

    ch.basic_publish(exchange='', routing_key=properties.reply_to,
                     body=f'Yes I can respond to your request: {properties.correlation_id}',
                     properties=message_properties)


connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

response_queue = channel.queue_declare(queue='request-queue')

channel.basic_consume(queue=response_queue.method.queue, auto_ack=True,
                      on_message_callback=on_request_message_received)

print('Server Started')
channel.start_consuming()
