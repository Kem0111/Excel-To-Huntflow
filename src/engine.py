import glob
import copy
from typing import Any, Dict, List, Optional
from src.core.exeptions import RestartScriptException

from src.utils.check_token import get_token_if_path
from src.core.settings import huntflow_settings
from src.requests.api_client import APIClient
from src.xlsx_parser import pars_exel_file
from src.utils.file_search import find_file_in_directory
from src.core.fix_parser_state import update_last_processed_line


class HuntFlowImporter:

    def __init__(self, token: str, directory_path: str) -> None:
        self.token = get_token_if_path(token)
        self.directory_path = directory_path
        self.huntflow_client = APIClient()
        self.excel_file = glob.glob(self.directory_path + '/*.xlsx')[0]
        self.externals = copy.deepcopy(huntflow_settings.externals)

        self.json_request_headers = self._add_token_in_headears(
            huntflow_settings.JSON_REQUEST_HEADERS
        )
        self.file_upload_headers = self._add_token_in_headears(
            huntflow_settings.FILE_UPLOAD_HEADERS
        )

    def run(self):
        applicants = pars_exel_file(self.excel_file)
        """
        Run the import process.
        """
        try:
            vacancies = self.get_vacancies(
                api_url=huntflow_settings.GET_VACANCIES_API,
                headers=self.json_request_headers
            )
            statuses = self.huntflow_client.request_get(
                api_url=huntflow_settings.GET_STATUSES_API,
                headers=self.json_request_headers
            )
            for i, applicant in enumerate(applicants):
                self.process_applicant(applicant, vacancies, statuses)

        except Exception as e:
            print(f"Found error: {e}")
            # To restart the script from the stop over if error
            update_last_processed_line(i)
            raise RestartScriptException

    def process_applicant(
        self,
        applicant: List[Dict[str, str]],
        vacancies: List[Dict[str, Any]],
        statuses: List[Dict[str, Any]]
    ) -> None:
        """
        Process a single applicant. Add an applicant to huntflow,
        Connect an applicant with his resume and vacancy with
        status and comment.

        # Note: Data validation is not performed in this script as
        it is assumed that all positions and statuses in the Excel
        file are valid for all candidates. In a real-world scenario,
        it would be important to include data validation to ensure
        the integrity and correctness of the data being processed.

        """
        file_id = self.process_file(applicant)

        vacancy_id = self._get_id(vacancies, "position", applicant["position"])
        status_id = self._get_id(statuses["items"], "name",
                                 applicant["status"])

        if file_id:
            self.externals[0]["files"] = [file_id]
            applicant["externals"] = self.externals

        response = self.huntflow_client.request_post(
            applicant,
            huntflow_settings.CREATE_APPLICANT_API,
            self.json_request_headers
        )

        applicant_to_vacancy_body = {
            "vacancy": vacancy_id,
            "status": status_id,
            "comment": applicant["comment"]
        }
        self.huntflow_client.request_post(
            applicant_to_vacancy_body,
            huntflow_settings.ADD_APPLICANT_TO_VACANCYAPI.format(
                applicant_id=response["id"]
            ),
            self.json_request_headers
        )

    def _add_token_in_headears(self, headers: Dict[str, str]) -> Dict:
        headers["Authorization"] = headers["Authorization"].format(
            token=self.token
        )
        return headers

    def _get_file_prefix(self, applicant: Dict[str, str]) -> str:
        """
        For to find a resume in directory
        """
        file_prefix = (
                f"{applicant.get('last_name')} "
                f"{applicant.get('first_name')}"
            )
        middle_name = applicant.get('middle_name')
        if middle_name:
            file_prefix += f" {middle_name}"
        return file_prefix

    def process_file(self, applicant: Dict[str, str]) -> Optional[int]:
        """
        Find an applicant resume in dirrectory
        Upload it to huntflow
        """
        file_prefix = self._get_file_prefix(applicant)
        file_directory = f"{self.directory_path}/{applicant['position']}"
        file_path = find_file_in_directory(file_directory, file_prefix)
        if file_path:
            respone = self.huntflow_client.request_upload_file(
                file_path,
                huntflow_settings.UPLOAD_FILE_API,
                self.file_upload_headers
            )
            return respone["id"]

    def get_vacancies(self, api_url: str, headers: Dict) -> List[Dict]:

        vacancies = []
        page = 1
        while True:

            response = self.huntflow_client.request_get(
                api_url=api_url.format(page=page),
                headers=headers
            )
            if not response.get("items"):
                break
            vacancies.extend(response["items"])
            page += 1
        return vacancies

    def _get_id(self, items: List[Dict], key: str, value: str) -> int:
        """
        For to get status and vacancy id for an applicant
        """
        for item in items:
            if item[key] == value:
                return item["id"]
