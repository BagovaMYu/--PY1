def get_count_char(str_):
    str_ = str_.lower()
    char_dict = {}
    for char in str_:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))


main_char_dict = get_count_char(main_str)

def get_percent(char_dict):
    total_char = sum(char_dict.values())
    for current_char in char_dict:
        char_dict[current_char] = round((char_dict[current_char] * 100 / total_char), 2)

    return char_dict

#print(get_percent(main_char_dict))
