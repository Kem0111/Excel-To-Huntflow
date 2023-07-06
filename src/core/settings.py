upload_file_api = "https://dev-100-api.huntflow.dev/v2/accounts/26/upload"

create_applicant_api = "https://dev-100-api.huntflow.dev/v2/accounts/26/applicants"

upload_file_headers = {
    "Accept": "multipart/form-data",
    "Authorization": "Bearer {token}",
    "x-file-parse": "false",
}

create_applicant_headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {token}",
    "Content-Type": "application/json",
}
