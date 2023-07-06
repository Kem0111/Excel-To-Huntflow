import pandas as pd


def pars_exel(file_path):

    df = pd.read_excel(file_path)

    data = []

    for _, row in df.iterrows():
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
