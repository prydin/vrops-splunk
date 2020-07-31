import requests
import json


class Sender:
    url = ""
    headers = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "" }

    def __init__(self, url, token):
        self.url = url
        self.headers["Authorization"] = "Splunk " + token

    def send_message(self, message):
        print("Sending: " + message)
        data = { "event": message }
        result = requests.post(url=self.url, data=json.dumps(data), verify=False, headers=self.headers)
        print(result)


