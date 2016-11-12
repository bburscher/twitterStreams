import os
from confluent_kafka import Producer, Consumer, KafkaError

SERVERS = os.environ.get('SERVERS', 'localhost')
TOPICS = os.environ.get('TOPICS', 'election')
# if running multiple times, GROUPID should be unique
# if all should receive all messages, or the same if
# messages should be load-balanced on all clients
GROUPID = os.environ.get('GROUPID', 'consumertest')


if __name__ == '__main__':
    c = Consumer({'bootstrap.servers': SERVERS, 'group.id': GROUPID,
                  'default.topic.config': {'auto.offset.reset': 'smallest'}})
    c.subscribe(TOPICS.split(','))

    running = True
    while running:
        print('waiting for message..')
        msg = c.poll() # blocking
        if not msg.error():
            message = msg.value().decode('utf-8')
            print('[RCV] {}'.format(message))
        elif msg.error().code() != KafkaError._PARTITION_EOF:
            print('[ERR] {}'.format(msg.error))
            running = False

    print('closing..')
    c.close()
