# amqps://ygtwdsgt:kWLjRwODAZ3IXAwwnZVdMTweoRRA6emB@cow.rmq2.cloudamqp.com/ygtwdsgt

import pika

params = pika.URLParameters('amqps://ygtwdsgt:kWLjRwODAZ3IXAwwnZVdMTweoRRA6emB@cow.rmq2.cloudamqp.com/ygtwdsgt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main',body='hello main')
