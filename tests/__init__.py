import requests


def send_data_to_huntflow(data, token, api_url):
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.post(api_url, headers=headers, json=data)

    return response.json()


data = {
    "first_name": "John",
    "last_name": "Doe",
    "middle_name": "Michael",
    "money": "$100000",
    "phone": "89999999999",
    "email": "mail@mail.ru",
    "skype": "my_skype",
    "position": "Frontend-разработчик",
    "company": "Google Inc.",
    "photo": None,
    "birthday": "2000-01-01",
    "externals": [
        {
            "auth_type": "NATIVE",
            "account_source": None,
            "data": {
                "body": "Resume text"
            },
            "files": [26]
        }
    ],
    "social": [
        {
            "social_type": "TELEGRAM",
            "value": "TelegramUsername"
        }
    ]
}

token = "e8af143aa19513acd5c5b7306eba0edc1f455b53f465c89a4d34cbf4dbe7e1e3"
api_url = "https://dev-100-api.huntflow.dev/v2/accounts/26/applicants"

response = send_data_to_huntflow(data, token, api_url)
print(response)
