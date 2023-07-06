import os


def get_token_if_path(token):

    if os.path.isfile(token):
        with open(token, 'r') as f:
            token = f.read().strip()
            return token
    return token
