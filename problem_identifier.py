
# Manipulacao das mensagens que vem das variaveis aumentadas
import numpy as np
import json
from collections import namedtuple

def receiveMessage():

    #message_received = {"current_1", "error", "machine", "occurrence_nbr", "variables", "status", "timestamp"}
    data = open("message.json", "r")
    message_received = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    print(message_received)
    return message_received


def sendMessage(message_to_operator):
    print("chegou")
    loop = False

def main():
    limit_time = 20
    duration_stop = 0
    loop = True
    passou = 0
    for i in range(20):
        msg = receiveMessage()
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
            print("chegou1")


if __name__ == '__main__':
    main()