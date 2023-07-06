import os


def get_start_line() -> int:
    """
    Function to get the last processed line from the file.
    If the file doesn't exist, it means that the processing hasn't
    started yet or earlier the script didn't fail, so it returns 0.
    """
    if os.path.exists('last_processed_line.txt'):
        with open('last_processed_line.txt', 'r') as f:
            return int(f.read())
    else:
        return 0


def update_last_processed_line(line_number: int) -> None:
    """
    Function to update the last processed line in the file
    if the script failed
    """
    with open('last_processed_line.txt', 'w') as f:
        f.write(str(line_number))
