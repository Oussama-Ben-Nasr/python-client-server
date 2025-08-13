import socket
import threading
import sys
import click

def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

@click.command()
@click.option('--host', prompt='Choose server host', default='localhost', help='Server ip address e.g localhost.')
@click.option('--port', prompt='Choose server port', help='Any valid int from 1 to 65536.')
def main(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
    except:
        print("Could not make a connection to the server")
        input("Press enter to quit")
        sys.exit(0)

    receiveThread = threading.Thread(target = receive, args = (sock, True))
    receiveThread.start()
    while True:
        message = input()
        sock.sendall(str.encode(message))

if __name__=='__main__':
    main()