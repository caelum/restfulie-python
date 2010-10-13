from lettuce import before, after
from fake_server import start_server, stop_server

@before.each_scenario
def start(scenario):
    start_server()

@after.each_scenario
def stop(scenario):
    stop_server()

