# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    """Works like str.capitalize()"""
    try:
        return text.capitalize()
    except AttributeError:
        print('Attribute is not a string')


if __name__ == '__main__':
    print(int_func('true or false'))
    result_list = []
    string_words = input('Enter the words you want to capitalize: ')
    for i in string_words.split():
        result_list.append(int_func(i))
    result_string = ' '.join(result_list)
    print(result_list)

