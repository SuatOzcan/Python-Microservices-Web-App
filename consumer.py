
import pika


params = pika.URLParameters('amqps://ygtwdsgt:kWLjRwODAZ3IXAwwnZVdMTweoRRA6emB@cow.rmq2.cloudamqp.com/ygtwdsgt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()