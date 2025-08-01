"""
Main function to run the test client to send information to weather-packing
microservice

Includes:
- run_test_client()
"""

from dotenv import load_dotenv
import os
from helper_func.socket_handler import (recv_message_str, setup_socket_client,
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

    test_data = [[
        # When it is hot
        {'temp_max': 78, 'temp_min': 61, 'main': "Clear"}
    ], [
        # When it is raining
        {'temp_max': 50, 'temp_min': 61, 'main': "Rain"}
    ], [
        # When it is cold
        {'temp_max': 31, 'temp_min': 10, 'main': "Cold"}
    ], [
        # When it is snowing
        {'temp_max': 32, 'temp_min': 10, 'main': "Snow"}
    ], [
        # When it is going to be hot and also going to rain
        {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
        {'temp_max': 80, 'temp_min': 61, 'main': "Rain"}
    ], [
        # When it is going to be hot and also going to Drizzle
        {'temp_max': 80, 'temp_min': 61, 'main': "Clear"},
        {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
    ], [
        # Invalid key in data
        {'temp_max': 80, 'temp_min': 61, 'main-1': "Clear"},
        {'temp_max': 80, 'temp_min': 61, 'main-1': "Drizzle"}
    ], [
        # Invalid value in data
        {'temp_max': "", 'temp_min': 61, 'main': "Clear"},
        {'temp_max': 80, 'temp_min': 61, 'main': "Drizzle"}
    ], [
        # Invalid data
        {}
    ], [
        # Invalid data
        ""
    ]]

    # Loop through all the query data sent
    for data in test_data:
        print(f"DATA SENT: {data}")
        send_message_json(socket, data)

        message = recv_message_str(socket)
        print(f"RESPONSE: {message.decode()}\n")


if __name__ == "__main__":
    run_test_client()