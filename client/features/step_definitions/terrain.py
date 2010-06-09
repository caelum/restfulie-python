from lettuce import *
from fake_server import start_server, stop_server


@before.all
def start_fake_server():
    return start_server()


@after.all
def stop_fake_server(total):
    return stop_server()
