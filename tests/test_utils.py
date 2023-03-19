import re

import pytest

from utils import get_filtered_data, get_formatted_date


def test_json_list(test_data):
    assert test_data


"""Вызываем тестируемую функцию"""


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 7
    assert data[0]['date'] == "2019-12-07T06:17:14.634890"
    assert data[0]["state"] == "EXECUTED"


"""Вызываем тестируемую функцию"""


def test_get_formatted_date(test_data):
    data = get_formatted_date(test_data[:1])  # Вызываем тестируемую функцию
    pattern = r"\d{4}\s\d{2}\*\*\s\*\*\*\*\s\d{4}"
    for d in data:
        card_number = re.search(pattern, d)
        assert card_number is not None, f"Card number is not encrypted: {d}"
