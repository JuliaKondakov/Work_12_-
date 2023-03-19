
import json

from utils import get_filtered_data, get_formatted_date

"""импортируем и открываем список JSON"""


def main():

    with open('bank_list.json', 'r', encoding='utf-8') as f:
        data = json.load(f)



        data = get_filtered_data(data)
        data = get_formatted_date(data)

        for row in data:
            print(row)


if __name__ == '__main__':
    main()
