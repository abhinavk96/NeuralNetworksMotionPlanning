from PodSixNet.Channel import Channel
from PodSixNet.Server import Server

from time import sleep


class ClientChannel(Channel):
    def Network(self, data):
        print (data)


class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print ('new connection:', channel)


print ("STARTING SERVER ON LOCALHOST")
server = MyServer()
while True:
    server.Pump()
    sleep(0.01)