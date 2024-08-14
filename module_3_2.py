def send_email(message, recipient, sender="university.help@gmail.com"):

    if "@" not in recipient or not (recipient.endwith('.com', '.ru', 'net')):

        print("Невозможно отправить письмо с адреса {} на адрес {}")

    elif sender == recipient:
        
        print("Невозможно отправить письмо самому себе")

    else:
        print("Отправляем письмо")
    # message = "Приветствую вас!"
    # recipient = "okolica_kesh@mail.ru"
    # sender = "university.help@gmail.com"

    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

