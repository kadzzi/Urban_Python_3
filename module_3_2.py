def email_valid(email: str) -> bool:
    country_codes = [".com", ".ru", ".net"]
    flag = False
    for code in country_codes:
        if code == email[-1 * len(code):]:
            flag = True
    if flag:
        if '@' in email and email[0] != '@':
            return True
    return False


def send_email(message, recipient, *, sender="university.help@gmail.com") -> None:
    if (email_valid(recipient) is False) or (email_valid(sender) is False):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


# test_str = 'fikus@mail.ru'
# print(email_valid(test_str))
