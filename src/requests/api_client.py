import requests
import mimetypes
from typing import Dict


class APIClient:

    def upload_file_to_huntflow(file_path: str, api_url: str, headers: Dict):

        mime_type = mimetypes.guess_type(file_path)[0]
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, mime_type)}
            response = requests.post(api_url,
                                     headers=headers,
                                     files=files)
        return response.json()

    def send_data_to_huntflow(data: Dict, api_url: str, headers: Dict):
        response = requests.post(api_url, headers=headers, json=data)

        return response.json()
