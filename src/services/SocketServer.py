import socket
from _thread import *

from services.GameSettings import GameSettings as gs


class SocketServer:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        print('Server ', self.ip)
        self.port = gs.SERVERPORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_list = []
        self.message_list = {}

    def run_server(self):
        try:
            self.socket.bind((self.ip, self.port))
        except socket.error as e:
            print(str(e))

        self.socket.listen(2)  # Only Two clients may connect (Player 1 and Player 2)
        print('Server is running, waiting for connection')
        start_new_thread(self.build_connection, ())

    def threaded_client(self, client):
        if len(self.client_list) == 1:
            client.send(str.encode('host-connected'+'\n'))
            print('[Server-Info] host-connected')
        else:
            for stored_client in self.client_list:
                stored_client.send(str.encode('player-joined' + '\n'))
                print("[Server-Info] player-joined")
        while True:
            try:
                msg = client.recv(512)
                reply = msg.decode('utf-8').splitlines()

                if msg:
                   # print('[Server-Info] Received: ', reply)
                   # print('[Server-Info] Sending to all', reply)
                    pass

                if reply == 'standby':
                    for var in reply:
                        client.send(str.encode(var+'\n'))
                else:
                    # send to both player
                    for player in self.client_list:
                        player.send(msg)

            except socket.error as e:
                print('[Server-Info] Error in message ', e)
                break

    def build_connection(self):
        while True:
            client, addr = self.socket.accept()
            self.client_list.append(client)
            start_new_thread(self.threaded_client, (client,))
