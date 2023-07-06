from src.utils.check_token import get_token_if_path
from src.core.settings import upload_file_api
from src.requests.api_client import APIClient


class HuntFlowImporter:

    def __init__(self, token: str, path_to_db: str):
        self.token = get_token_if_path(token)
        self.path_to_db = path_to_db
        self.huntflow_client = APIClient()

    def run(self):
        print(self.token, self.path_to_db)
