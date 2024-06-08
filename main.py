def to_uppercase(s: str) -> str:
    """
    Преобразует все символы в строке s в верхний регистр и возвращает результат.

    :param s: Строка для преобразования.
    :return: Строка с всеми символами в верхнем регистре.
    """
    return s.upper()


def capitalize_words(s: str) -> str:
    """
    Делает заглавными первые буквы каждого слова в строке s и возвращает результат.

    :param s: Строка для преобразования.
    :return: Строка с первыми буквами каждого слова в верхнем регистре.
    """
    return ' '.join(word.capitalize() for word in s.split())

input_string = "привет, мир. как дела?"
uppercased_string = to_uppercase(input_string)
print(uppercased_string)

capitalized_string = capitalize_words(input_string)
print(capitalized_string)

# TODO: Заметки
## Дата: 08.06.2024
## Преподаватель: Дуплей Максим Игоревич