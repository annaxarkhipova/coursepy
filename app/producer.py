


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

address = 'roman@one.com'
channel.basic_publish(exchange='',
                      routing_key=address,
                      body='This is your first message !')
print('Message sent')
connection.close()