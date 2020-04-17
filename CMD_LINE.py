import socket as sock
import cv2 as cv
import numpy as np

class socket_wrapper :
    # A simple wrapper class to handle sockets
    # Automatic creation and connecting is handled here

    def __init__(self, socket = None) :
        if socket == None :
            self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        else :
            self.socket = socket

    def connect(self, host, port) :
        self.socket.connect((host, port))

    def send(self, msg) :
        total_sent = 0
        while total_sent < len(msg) :
            sent = self.socket.send(msg[total_sent:])
            if sent == 0 :
                raise RuntimeError("Socket connection was broken. Please restart and try again")
            total_sent += sent

    def recieve(self) :
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.socket.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("Socket connection was broken. Please restart and try again")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

class server :
    # A simple class to handle server creation
    # May need to be put on a separate thread later

    def __init__(self, socket = None) :
        if socket == None :
            self.socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        else :
            self.socket = socket

        self.socket.bind(('', 8080))

        self.socket.listen(5)

    def run(self) :
        while True :
            client_socket, address = self.socket.accept()
            print(str(address) + " Has just connected")

def main():
    a = input()

    if a == "server" :
        main_server = server(sock.socket(sock.AF_INET, sock.SOCK_STREAM))
        main_server.run()
    else :
        client = socket_wrapper(sock.socket(sock.AF_INET, sock.SOCK_STREAM))
        client.connect('localhost', 8080)

if __name__ == "__main__" :
    main()
