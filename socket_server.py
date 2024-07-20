import socket
import logging
from datetime import datetime
import socket
import urllib.parse
import json


def save_data_from_form(data):
    filename = 'storage/data.json'
    nowdate = datetime.now().isoformat()
    parse_data = urllib.parse.unquote_plus(data.decode())
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
    except FileNotFoundError:
        data_dict = {}
    try:
        parse_dict = {key: value for key, value in [el.split('=') for el in parse_data.split('&')]}
        data_dict[nowdate] = parse_dict
        with open(filename, 'w',encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii= False, indent= 4)
    except ValueError as e:
        logging.error(e)
    except OSError as e:
        logging.error(e)

def run_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 5000))
    logging.info('Socket server started ...')
    try:
        while True:
            msg, address = server_socket.recvfrom(1024)
            save_data_from_form(msg)
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.server_close()





