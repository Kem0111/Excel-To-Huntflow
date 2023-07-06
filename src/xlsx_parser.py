import pandas as pd
from typing import List, Dict
from src.core.fix_parser_state import get_start_line


def pars_exel_file(file_path: str) -> List[Dict[str, str]]:
    """
    Function to parse the Excel file starting from the last processed line.
    """
    start_line = get_start_line()
    df = pd.read_excel(file_path)
    data = []

    for i, row in df.iterrows():

        if i < start_line:
            continue

        name_parts = row['ФИО'].split()
        row_dict = {}

        match len(name_parts):
            case 2:
                row_dict['last_name'] = name_parts[0]
                row_dict['first_name'] = name_parts[1]
            case 3:
                row_dict['last_name'] = name_parts[0]
                row_dict['first_name'] = name_parts[1]
                row_dict['middle_name'] = name_parts[2]

        row_dict['money'] = row['Ожидания по ЗП']
        row_dict['position'] = row['Должность']
        row_dict['status'] = row['Статус']
        row_dict['comment'] = row['Комментарий']

        data.append(row_dict)

    return data
