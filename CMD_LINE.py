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
            self.sock = sock

    def connect(self, host, port) :
        self.socket.connect((host, port))

    def send(self, msg) :
        total_sent = 0
        while total_sent < len(msg) :
            sent = self.sock.send(msg[total_sent:])
            if sent == 0 :
                raise RuntimeError("Socket connection was broken. Please restart and try again")
            total_sent += sent

    def recieve(self) :
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

class server :
    

def main():
    print("test")

    main_socket = socket_wrapper()

    main_socket.connect("localhost", 8080)
    main_socket.send("aaa")
    print(main_socket.recieve())

if __name__ == "__main__" :
    main()
