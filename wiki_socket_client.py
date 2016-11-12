# -*- coding: utf-8 -*-
import socketIO_client

class WikiNamespace(socketIO_client.BaseNamespace):
    def on_change(self, change):
        print('%(user)s edited %(title)s' % change)

    def on_connect(self):
        self.emit('subscribe', 'commons.wikimedia.org')


socketIO = socketIO_client.SocketIO('https://stream.wikimedia.org')
socketIO.define(WikiNamespace, '/rc')

socketIO.wait()
