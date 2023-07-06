import unittest
from unittest.mock import ANY, patch, MagicMock

from src.requests.api_client import APIClient


class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient()
        self.mock_response = MagicMock()
        self.mock_response.raise_for_status.return_value = None

    def test_request_upload_file(self):
        # Arrange
        self.mock_response.json.return_value = {'id': 123}
        with patch(
            'requests.post',
            return_value=self.mock_response
        ) as mock_post:

            # Act
            response = self.api_client.request_upload_file(
                'tests/fixtures/test.pdf',
                'test_api_url',
                {'header': 'test_header'}
            )

            # Assert
            mock_post.assert_called_once_with(
                'test_api_url',
                headers={'header': 'test_header'},
                files={
                    'file': (
                        'tests/fixtures/test.pdf',
                        ANY,
                        'application/pdf'
                    )
                }
            )
            self.assertEqual(response, {'id': 123})

    def test_request_post(self):
        # Arrange
        self.mock_response.json.return_value = {'result': 'success'}
        with patch(
            'requests.post',
            return_value=self.mock_response
        ) as mock_post:

            # Act
            response = self.api_client.request_post(
                {'key': 'value'},
                'test_api_url',
                {'header': 'test_header'}
            )

            # Assert
            mock_post.assert_called_once_with(
                'test_api_url',
                headers={'header': 'test_header'},
                json={'key': 'value'}
            )
            self.assertEqual(response, {'result': 'success'})

    def test_request_get(self):
        # Arrange
        self.mock_response.json.return_value = {'result': 'success'}
        with patch(
            'requests.get',
            return_value=self.mock_response
        ) as mock_get:

            # Act
            response = self.api_client.request_get(
                'test_api_url',
                {'header': 'test_header'}
            )

            # Assert
            mock_get.assert_called_once_with(
                'test_api_url',
                headers={'header': 'test_header'}
            )
            self.assertEqual(response, {'result': 'success'})
