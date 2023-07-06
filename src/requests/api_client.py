import requests
import mimetypes
from typing import Dict


class APIClient:

    def request_upload_file(self, file_path: str, api_url: str, headers: Dict) -> Dict:

        mime_type = mimetypes.guess_type(file_path)[0]
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, mime_type)}
            response = requests.post(api_url,
                                     headers=headers,
                                     files=files)
        return response.json()

    def request_post(self, body: Dict, api_url: str, headers: Dict) -> Dict:
        response = requests.post(api_url, headers=headers, json=body)

        return response.json()

    def request_get(self,  api_url: str, headers: Dict) -> Dict:
        response = requests.get(api_url, headers=headers)
        return response.json()

