from time import sleep
import lib
import sys

# Основная функция
def caesar_crypto():
    while True:
        print('Шифр Цезаря v1.0. Author - olegilmix')
        sleep(1)
        print('Добро пожаловать!')
        sleep(2)

        caesar = lib.is_valid_number('1 - Старт\n2 - Выход', 1, 2)

        if caesar == 2:
            print('Всего хорошего!')
            sys.exit(0)


        print('Выберите тип направления:')
        direction = lib.is_valid_number('1 - Шифрование\n2 - Дешифрование', 1, 2)

        if direction == 3:
            exit()

        sleep(0.5)
        print('Выберите язык')
        lang = lib.is_valid_number('1 - Английский язык\n2 - Русский язык', 1, 2)

        sleep(0.5)
        if lang == 1:
            rotate = lib.is_valid_number('Введите шаг сдвига (от 0 до 25)', 0, 25)
        else:
            rotate = lib.is_valid_number('Введите шаг сдвига (от 0 до 31)', 0, 31)

        if direction == 1:
            text = lib.is_valid_text(lang)
            result = lib.code(lang, rotate, text)
            line = 20
            sleep(0.6)

            if len(result) > 20:
                line = len(result)
            print('_' * line)
            print('Зашифрованный текст:')
            print(result)
            print('_' * line)

            choice = lib.is_valid_number('\nЗапустить скрипт еще раз\n1 - да\n2 - нет', 1, 2)
            if choice == 1:
                continue
            else:
                print('До свидания!')
                sleep(1.5)
                sys.exit(0)
        else:
            text = lib.is_valid_text(lang)
            result = lib.decode(lang, rotate, text)
            line = 20
            sleep(0.6)

            if len(result) > 20:
                line = len(result)
            print('_' * line)
            print('\nРасшифрованный текст:')
            print(result)
            print('_' * line)

            choice = lib.is_valid_number('\nЗапустить скрипт еще раз\n1 - да\n2 - нет', 1, 2)
            if choice == 1:
                continue
            else:
                print('До свидания!')
                sleep(1.5)
                sys.exit(0)
        

if __name__ == "__main__":
    caesar_crypto()