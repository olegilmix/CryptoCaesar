from string import punctuation

# Генерация алфавитов
lang_en = [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
lang_ru = [chr(i) for i in range(1040,1104)]

def is_valid_number(message, start, end):
    while True:
        try:
            print(message)
            result = int(input())
            if start <= result <= end:
                return result
            else:
                print(f'Ошибка число должно быть от {start} до {end}!')
        except ValueError:
            print('Ошибка: Введите число')

def is_valid_text(lang):
    while True:
        print('Введите текст')
        txt = input()
        if txt == '':
            print('Ошибка: Пустой текст')
            continue
        elif txt[0] in punctuation:
            print('Ошибка: Текст должен начинаться с буквы, а не с спец. символа')
        elif lang == 1 and txt[0] in lang_en:
            return txt
        elif lang == 2 and txt[0] in lang_ru:
            return txt
        else:
            print('Ошибка: Текст не соответствует выбранному языку')

def code(lang, rotate, text):
    result = ''
    if lang == 1:
        alphabet = lang_en
        power = 26
    else:
        alphabet = lang_ru
        power = 32

    for symbol in text:
        if symbol.isalpha():
            if symbol.isupper():
                result += alphabet[(alphabet.index(symbol) + rotate) % power]
            else:
                result += alphabet[(alphabet.index(symbol) + rotate) % power + power]
        else:
            result += symbol
    
    return result


def decode(lang, rotate, text):
    result = ''
    if lang == 1:
        alphabet = lang_en
    else:
        alphabet = lang_ru

    for symbol in text:
        if symbol.isalpha():
            if symbol.isupper():
                result += alphabet[(alphabet.index(symbol) - rotate) % 26]
            else:
                result += alphabet[(alphabet.index(symbol) - rotate) % 26 + 26]
        else:
            result += symbol
    
    return result