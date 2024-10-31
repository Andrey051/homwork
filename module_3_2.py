def send_email(message = " " ,  recipient = " " ,  sender = "university.help@gmail.com" ):  # создаю функцию send_email, которая принимает 2 обычных аргумента  и 1 обязательно именованный аргумент со значением по умолчанию
    if "@"  not in recipient   or  "@" not in sender or not recipient.endswith((".com",".ru",".net")) or not sender.endswith((".com",".ru",".net")) :  # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")  # то вывести на экран(в консоль) строку
    elif  sender == recipient: # Если же sender и recipient совпадают
        print("Нельзя отправить письмо самому себе!") # вывести "Нельзя отправить письмо самому себе!"
    elif sender == 'university.help@gmail.com':  # Если же отправитель по умолчанию - university.help@gmail.com
        print( "Письмо успешно отправлено с адреса <sender> на адрес <recipient>.") # то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    else:                                                                           # В противном случае вывести
        print( "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.") # вывести сообщение

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
