from fastapi import Response
from fastapi.testclient import TestClient

from dkvsample.app import app
from dkvsample.model.echo_model import EchoModel

client = TestClient(app)

SAMPLE_STR_VALUE_1: str = 'SampleValue1'
SAMPLE_STR_VALUE_2: str = 'SampleValue2'
SAMPLE_INT_VALUE: int = 1

class TestApp:
    def test_health_check(self):
        res: Response = client.get('/health')

        assert res.status_code == 200
        assert res.json()['status'] == 'ok'

    def test_echo_valid_two_parameters(self):
        payload: EchoModel = {
            'skey1': SAMPLE_STR_VALUE_1,
            'skey2': SAMPLE_STR_VALUE_2
        }
        res: Response = client.post('/echo', json=payload)

        assert res.status_code == 200
        assert res.json() == payload

    def test_echo_valid_one_parameter(self):
        payload: EchoModel = {
            'skey1': SAMPLE_STR_VALUE_1
        }
        res: Response = client.post('/echo', json=payload)

        assert res.status_code == 200
        assert res.json()['skey1'] == payload['skey1'] and res.json()['skey2'] is None

    def test_echo_valid_no_parameters(self):
        payload: EchoModel = {}
        res: Response = client.post('/echo', json=payload)

        assert res.status_code == 200
        assert res.json()['skey1'] is None and res.json()['skey2'] is None

    def test_echo_invalid_parameters(self):
        payload: dict = {
            'skey1': SAMPLE_INT_VALUE
        }
        res: Response = client.post('/echo', json=payload)

        assert res.status_code == 422
        assert 'Input should be a valid string' == res.json()['detail'][0]['msg']
