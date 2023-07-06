import requests_mock
from src.requests.api_client import APIClient
from src.core.settings import upload_file_api


def test_upload_file_to_huntflow():
    with requests_mock.Mocker() as m:
        file_path = 'tests/fixtures/test.pdf'
        m.post(
            upload_file_api,
            json={'result': 'success'}
        )
        client = APIClient()
        response = client.upload_file_to_huntflow(file_path)

        assert response == {'result': 'success'}
