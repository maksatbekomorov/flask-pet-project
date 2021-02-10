from faker import Faker
import pandas as pd


fake = Faker()


def table_filling(dict):
    # x = {'table_name': 'n1', 'table_rows': '1123', 'table_column': ['c1', 'c2', 'c3', 'c4'], 'columns_type': ['street_address', 'name', 'phone_number', 'zipcode']}
    x = dict
    table = pd.DataFrame(columns=x['table_column'], index=range(int(x['table_rows'])))  # сюди потрібно передавати к-сть рядків!
    af = [getattr(fake, field) for field in x['columns_type']]
    for i in range(len(table.columns)):
        table[table.columns[i]] = [af[i]() for x in table[table.columns[i]]]
    table.name = x['table_name']
    return table
