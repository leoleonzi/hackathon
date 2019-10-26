
# Manipulacao das mensagens que vem das variaveis aumentadas
import numpy as np
import json
import time
from collections import namedtuple

from simulator_client import SimulatorClient

def receiveMessageTest():
    payload = { "current_1": 0, "error": 1, "machine": 3, "occurrence_nbr": 325, "status": 0, "temperature": 56, "timestamp": "2019-09-07 18:28:38" }
    statuses = [0,0,0,0,0,1,1,1,0,0,0,0,0]
    for status in statuses:
        payload['status'] = status
        yield payload

def receiveMessage():
    message_received = SimulatorClient.get_json().json()

    return message_received


def sendMessage(message_to_operator):
    print("chegou")
    loop = False

def main():
    limit_time = 5
    duration_stop = 0
    loop = True
    passou = 0
    receiveMessage = receiveMessageTest()
    while True:
        time.sleep(0.5)
        msg = next(receiveMessage)
        print(msg)
        if msg["status"] == 0:
            if passou == 0:
                time_stop = msg["timestamp"]
            duration_stop += 1
        else:
            duration_stop = 0

        if duration_stop >= limit_time:
            if duration_stop == limit_time:
                variables_error_moment = msg["variables"]
            message_to_operator = {"id_machine": msg["id_machine"],
                                    "variables":
                                    variables_error_moment,
                                    "status": msg["status"],
                                    "duration_stop": duration_stop,
                                    "time_stop": time_stop
                                    }
            
            sendMessage(message_to_operator)
            print(duration_stop)


if __name__ == '__main__':
    main()