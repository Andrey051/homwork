from os import remove
calls = 0  # Создал переменную calls = 0 вне функций
def count_calls(): # Создал функцию count_calls
    global calls  # должна вызываться в остальных двух функциях
    calls += 1  # изменяем в ней значение переменной calls

def string_info(string): #(принимает аргумент - строку) Создаю функцию string_info с параметром string
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): # Создать функцию is_contains с двумя параметрами string и list_to_search
    count_calls()
    string_low = string.lower()
    for i in list_to_search :
        if string_low == i.lower() : # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
