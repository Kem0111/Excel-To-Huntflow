from functools import wraps
import requests
import mimetypes
from typing import Dict


class APIClient:

    @staticmethod
    def _handle_request_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            return response.json()
        return wrapper

    @_handle_request_decorator
    def request_upload_file(self, file_path: str,
                            api_url: str, headers: Dict) -> Dict:
        mime_type = mimetypes.guess_type(file_path)[0]
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, mime_type)}
            return requests.post(api_url, headers=headers, files=files)

    @_handle_request_decorator
    def request_post(self, body: Dict, api_url: str, headers: Dict) -> Dict:
        return requests.post(api_url, headers=headers, json=body)

    @_handle_request_decorator
    def request_get(self,  api_url: str, headers: Dict) -> Dict:
        return requests.get(api_url, headers=headers)
