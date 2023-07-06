class HuntFlowSettings:

    UPLOAD_FILE_API = "https://dev-100-api.huntflow.dev/v2/accounts/26/upload"

    CREATE_APPLICANT_API = (
        "https://dev-100-api.huntflow.dev/v2/accounts/26/"
        "applicants"
    )

    GET_VACANCIES_API = (
        "https://dev-100-api.huntflow.dev/v2/accounts/26/"
        "vacancies?count=100&page={page}&mine=false&opened=false"
    )

    ADD_APPLICANT_TO_VACANCY_API = (
        "https://dev-100-api.huntflow.dev/v2/"
        "accounts/26/applicants/{applicant_id}/vacancy"
    )

    GET_STATUSES_API = (
        "https://dev-100-api.huntflow.dev/v2/accounts/26/vacancies/statuses"
    )

    FILE_UPLOAD_HEADERS = {
        "Accept": "multipart/form-data",
        "Authorization": "Bearer {token}",
        "x-file-parse": "false",
    }

    JSON_REQUEST_HEADERS = {
        "Accept": "application/json",
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json",
    }

    externals = [
        {
            "auth_type": "NATIVE",
            "files": None
        }
    ]


huntflow_settings = HuntFlowSettings()
