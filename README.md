twitterStreams
==============

distributed analytics of live tweet stream

authors: Bjorn + Martijn


Installation
============

Compile `librdkafka` and install requirements

    git clone https://github.com/edenhill/librdkafka.git
    cd librdkafka
    ./configure
    make
    sudo make install

    pip3 install -r requirements.txt


Usage
=====

# Download Kafka, and run in separate tabs
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

# Run once
TOPIC='election'
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic $TOPIC

# Run producer (twitter -> kafka)
python3 tweePyTest.py

# Run consumer (kafka -> print)
SERVERS=$IP_OR_HOSTNAME python3 consumer_test.py
