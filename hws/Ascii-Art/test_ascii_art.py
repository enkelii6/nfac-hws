import pytest
from ascii_art import generate_ascii


def test_generate_ascii():
    result = generate_ascii("Hello")

    # Проверяем, что результат является строкой
    assert isinstance(result, str), "Функция должна возвращать строку"

    # Проверяем, что строка не пустая
    assert result.strip(), "Функция не должна возвращать пустую строку"

    # Проверяем, что каждый символ Hello есть в выводе (предположим, что generate_ascii использует стандартный ASCII-арт)
    for char in "Hello":
        assert char in result, f"Символ '{char}' отсутствует в ASCII-арте"

