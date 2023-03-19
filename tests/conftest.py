"""Создаем файл для тестирования списка отсортированного по заданию"""
import pytest


@pytest.fixture
def test_data():
    return [
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {
                "amount": "45849.53",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961"
        },

        {
            "id": 509645757,
            "state": "EXECUTED",
            "date": "2019-10-30T01:49:52.939296",
            "operationAmount": {
                "amount": "23036.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453"
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869"
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "CANCELED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
              "amount": "48223.05",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
          },
        ]