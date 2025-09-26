"""
Лабораторна робота №1.2
"""
import string
import time

SHIFT = 3
LETTERS = string.ascii_letters + string.punctuation + string.digits

def encode_text(text: str, shift: int) -> str:
    """
    Шифрує текст за допомогою зсуву.
    """
    result = ""
    for char in text:
        if char == " " or char not in LETTERS:
            result += char
        else:
            index = LETTERS.index(char)
            new_index = (index + shift) % len(LETTERS)
            result += LETTERS[new_index]
    return result

def decode_text(text: str, shift: int) -> str:
    """
    Дешифрує текст за допомогою зсуву.
    """
    result = ""
    for char in text:
        if char == " " or char not in LETTERS:
            result += char
        else:
            index = LETTERS.index(char)
            new_index = (index - shift) % len(LETTERS)
            result += LETTERS[new_index]
    return result

def print_time(show: bool = False) -> None:
    """
    Виводить поточний час, якщо show дорівнює True.
    """
    if show:
        print("Поточний час:", time.ctime())

def main():
    """
    Основна функція програми. Запитує режим роботи та текст для обробки.
    """
    choice_mode = input("Would you like to encode or decode? ").strip().lower()
    text = input("Please enter text: ")

    if choice_mode == "encode":
        result = encode_text(text, SHIFT)
    elif choice_mode == "decode":
        result = decode_text(text, SHIFT)
    else:
        print("Невірний режим. Введіть 'encode' або 'decode'.")
        return

    print("Вхідний текст:", text)
    print("Результат:", result)
    print_time(True)  # Вивід поточного часу

if __name__ == '__main__':
    main()
