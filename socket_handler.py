"""
Program with functions related to socket and socket communication
"""

import zmq

def setup_socket_server(port=5600):
    """
    Function setups the port
    :param port: integer
    :return: socket
    """

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:{port}")

    return socket

def setup_socket_client(port=5600):
    """
    Function setups the port
    :param port: integer
    :return: socket
    """

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")

    return socket

def recv_message_str(socket):
    """
    Function to receive message in string format along the pipeline
    :param socket:
    :return: receive message
    """

    message = socket.recv()
    print(f"SERVER: {message}")

    return message


def send_message_str(socket, message):
    """
    Function to send message along the pipeline
    :param socket:
    :param message:
    :return:
    """

    socket.send_string(message)

def recv_message_json(socket):
    """
    Function to receive message in string format along the pipeline
    :param socket:
    :return: receive message
    """

    message = socket.recv_json()
    print(f"SERVER: {message}")

    return message


def send_message_json(socket, message):
    """
    Function to send message along the pipeline
    :param socket:
    :param message:
    :return:
    """

    socket.send_json(message)