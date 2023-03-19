from datetime import datetime

"""Функция филтрации значений по ключу"""


def get_filtered_data(data):
     # Сколько значений по ключу "state", если такой ключь имееться и у него значение EXECUTED
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    data.sort(key=lambda x: x["date"], reverse=True)
    # Возращает поледние 5 значений
    return data[:7]


"""Функция форматирования даты в нужный формат"""


def get_formatted_date(data):
    new_data_list = []
    for row in data:
        date = row['date']
        date_obj = datetime.fromisoformat(date)
        formatted_date = date_obj.strftime('%d.%m.%Y')
        deskription = row['description']    # Вид банковской операции
        if "from" in row.keys():
            sender = row['from'].split()    # Реквизиты банка
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"     # шифрует номер карты
            sender_info = " ".join(sender)      # Склеиваем коллекцию
            recipient = f"**{row['to'][-4:]}"    # шифруем номер счета
            amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["code"]}' # Вывести данные о сумме и виде валуты

        # Необходимые значения записываем в новый список
            new_data_list.append(f"""
{formatted_date} {deskription } 
{sender_info} {sender_bill} {recipient}
{amount}
""")

    return new_data_list   # Возращаем новый список с нужными данными

