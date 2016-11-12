import os
from confluent_kafka import Producer, Consumer, KafkaError

SERVERS = os.environ.get('SERVERS', 'localhost')
TOPIC = os.environ.get('TOPIC', 'election')


if __name__ == '__main__':
    c = Consumer({'bootstrap.servers': SERVERS, 'group.id': 'mygroup',
                  'default.topic.config': {'auto.offset.reset': 'smallest'}})
    c.subscribe([TOPIC])

    running = True
    while running:
        print('waiting for message..')
        msg = c.poll() # blocking
        if not msg.error():
            message = msg.value().decode('utf-8')
            print('[RCV] {}'.format(message))
        elif msg.error.code() != KafkaError._PARTITION_EOF:
            print('[ERR] {}'.format(msg.error))
            running = False

    print('closing..')
    c.close()
