import pika

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='letterbox')


def on_message_callback(ch, method, properties, message):
    print(f'Message received {message}')


channel.basic_consume(queue='letterbox', auto_ack=True,
                      on_message_callback=on_message_callback)


print('Started consuming')
channel.start_consuming()
