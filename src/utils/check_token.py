import os


def get_token_if_path(token):
    """
    The script should eccept token or path to file with huntflow tokens,
    so if it file, return the first token
    """
    if os.path.isfile(token):
        with open(token, 'r') as f:
            token = f.readline().strip()
            return token
    return token
