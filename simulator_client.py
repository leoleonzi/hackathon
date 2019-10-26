import requests

class SimulatorClient:

    @staticmethod
    def get_json():
        return requests.get('http://172.16.25.18:8000/')