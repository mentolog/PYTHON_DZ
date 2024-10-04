import pytest
from StringUtils import StringUtils  # Импортируем класс из другого файла


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),  # Позитивный тест
    ("", ""),  # Негативный тест: пустая строка
    (" skypro", " skypro"),  # Негативный тест: пробел в начале
    ("TEST", "Test"),  # Позитивный тест: все заглавные
])
def test_capitilize(utils, input_str, expected):
    assert utils.capitilize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),  # Позитивный тест
    ("", ""),  # Негативный тест: пустая строка
    ("    ", ""),  # Негативный тест: строка из пробелов
    ("test", "test"),  # Позитивный тест: непустая строка
])
def test_trim(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),  # Позитивный тест
    ("1:2:3", ":", ["1", "2", "3"]),  # Позитивный тест: другой разделитель
    ("", ",", []),  # Негативный тест: пустая строка
    ("a,b,c,", ",", ["a", "b", "c", ""]),  # Негативный тест: лишний разделитель
])
def test_to_list(utils, input_str, delimiter, expected):
    assert utils.to_list(input_str, delimiter) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),  # Позитивный тест
    ("SkyPro", "Z", False),  # Негативный тест: символ не найден
    ("", "S", False),  # Негативный тест: пустая строка
    ("123456", "2", True),  # Позитивный тест: число как строка
])
def test_contains(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Позитивный тест
    ("SkyPro", "Z", "SkyPro"),  # Негативный тест: символ не найден
    ("", "S", ""),  # Негативный тест: пустая строка
    ("123123", "1", "23123"),  # Позитивный тест: число как строка
])
def test_delete_symbol(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),  # Позитивный тест
    ("SkyPro", "P", False),  # Негативный тест: символ не в начале
    ("", "S", False),  # Негативный тест: пустая строка
    ("123", "1", True),  # Позитивный тест: строка с числами
])
def test_starts_with(utils, input_str, symbol, expected):
    assert utils.starts_with(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "o", True),  # Позитивный тест
    ("SkyPro", "y", False),  # Негативный тест: символ не в конце
    ("", "o", False),  # Негативный тест: пустая строка
    ("123", "3", True),  # Позитивный тест: строка с числами
])
def test_end_with(utils, input_str, symbol, expected):
    assert utils.end_with(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", True),  # Негативный тест: пустая строка
    (" ", True),  # Негативный тест: строка из пробела
    ("skypro", False),  # Позитивный тест
])
def test_is_empty(utils, input_str, expected):
    assert utils.is_empty(input_str) == expected


@pytest.mark.parametrize("lst, joiner, expected", [
    ([1, 2, 3], ", ", "1, 2, 3"),  # Позитивный тест
    ([], ", ", ""),  # Негативный тест: пустой список
    (["a", "b", "c"], "-", "a-b-c"),  # Позитивный тест: другой разделитель
    ([1000], ", ", "1000"),  # Позитивный тест: один элемент
])
def test_list_to_string(utils, lst, joiner, expected):
    assert utils.list_to_string(lst, joiner) == expected


if __name__ == "__main__":
    pytest.main()
