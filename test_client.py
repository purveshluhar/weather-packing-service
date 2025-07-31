"""
Program to test the microservice
"""

from dotenv import load_dotenv
import os
from socket_handler import (recv_message_str, setup_socket_client,
                            send_message_json)


def run_test_client():
    """
    Program to run the service
    :return:
    """

    # Load the PORT from .env
    load_dotenv()
    port = os.getenv("PORT")

    # Set up the socket
    socket = setup_socket_client(port)

    data = [
        {'temp_max': 78, 'temp_min': 60, 'main': "Clear"},
        {'temp_max': 50, 'temp_min': 40, 'main': "Rain"}
    ]

    send_message_json(socket, data)

    recv_message_str(socket)


if __name__ == "__main__":
    run_test_client()