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

# Run in separate tab
docker run -p 2181:2181 -p 9092:9092 -e ADVERTISED_HOST=192.168.178.59 -e ADVERTISED_PORT=9092 spotify/kafka

# Run producer (twitter -> kafka)
python3 tweePyTest.py

# Run consumer (kafka -> print)
SERVERS=192.168.178.65 python3 consumer_test.py
