#
# def pas():
#     list_pas = []
#     lock = 0
#     range_lock = range(3, 21)
#     number_lock = random.choice(range_lock)
#     lock += number_lock
#     range_pas = range(1, 21)
#     for i in range_pas:
#         range_pas_2 = range(i + 1, 21)
#         for j in range_pas_2:
#             if i != lock and j != lock and lock % (i + j) == 0:
#                 list_pas.append(i)
#                 list_pas.append(j)
#     print(f'{lock} - число из первой вставки')
#     print(list_pas, '- нужный пороль')
#
#
# pas()
def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" not in recipient or not recipient.endswith((".com", ".ru", ".net"))
            or "@" not in sender or not sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Примеры вызова функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')