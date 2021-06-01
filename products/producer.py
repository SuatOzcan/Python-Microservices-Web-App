# amqps://ygtwdsgt:kWLjRwODAZ3IXAwwnZVdMTweoRRA6emB@cow.rmq2.cloudamqp.com/ygtwdsgt

import pika, json

params = pika.URLParameters('amqps://ygtwdsgt:kWLjRwODAZ3IXAwwnZVdMTweoRRA6emB@cow.rmq2.cloudamqp.com/ygtwdsgt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',body=json.dumps(body), properties=properties)
