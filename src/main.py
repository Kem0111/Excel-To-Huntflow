#!/usr/bin/env python3
from src.cli import get_cli_args
from src.engine import HuntFlowImporter


def main():

    token, path_to_db = get_cli_args()
    importer = HuntFlowImporter(token, path_to_db)
    importer.run()


if __name__ == "__main__":
    main()
