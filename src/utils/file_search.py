import os
from typing import Optional
import unicodedata


def find_file_in_directory(directory: str, file_prefix: str) -> Optional[str]:
    for file in os.listdir(directory):
        normalized_file = unicodedata.normalize('NFC', file)
        if normalized_file.startswith(file_prefix):
            return os.path.join(directory, file)
    return None
