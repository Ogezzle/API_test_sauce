
import json
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
import requests


class Folk:
    def __init__(self):
        self._builtIn= None

    @property
    def builtin(self):
        if not self._builtIn:
            try:
                self._builtIn = BuiltIn()
            except RobotNotRunningError:
                self._builtIn = None
        return self._builtIn

    @keyword('prepare payload')
    def prepare_payload(self,data_file: str, key: str):
        with open(data_file, 'r', encoding='utf-8') as of:
            json_data = json.load(of)
            test_data = json_data['data'][key]
        return test_data

    @keyword('post request')
    def post_request(self,url: str, payload, auth: dict = None):
        resp = requests.post(url=url, json=json.loads(payload), param=auth)
        self._builtIn.log_to_console("RESP status code {} and Response Message {}".format(resp.status_code, resp.text))

