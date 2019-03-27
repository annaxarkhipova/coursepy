
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='annaarkx-MOBL2'))

channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)





def callback_in_first_message(ch, method, properties, body):
    print(" [x] Received %r" % body)






channel.basic_consume(callback_in_first_message,
                      queue='hello',
                      no_ack=True, properties=pika.BasicProperties(delivery_mode=2))

print(' Waiting for messages. To exit press CTRL+C')
channel.start_consuming()