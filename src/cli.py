import argparse


def get_cli_args():
    parser = argparse.ArgumentParser(
        prog='import_to_huntflow',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        "--token",
        help='Token or path to file with tokens',
        type=str
    )
    parser.add_argument(
        "--path",
        help='Path to the folder with the database',
        type=str
    )

    args = parser.parse_args()
    return args.token.strip(), args.path.strip()
