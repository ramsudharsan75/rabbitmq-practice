import pika

connection_credentials = pika.PlainCredentials(
    username='ramsudharsan75', password='Krishna75!')
connection_params = pika.ConnectionParameters(
    host='localhost', credentials=connection_credentials)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = 'Dummy message'

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print('message sent')
connection.close()
