import threading
import http_server
import socket_server
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    http = threading.Thread(target=http_server.run_http_server)
    socket = threading.Thread(target=socket_server.run_socket_server)
    http.start()
    socket.start()
