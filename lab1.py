import numpy as np
import datetime
import re


def card_check(card_number, expiry_date, cvc):
    # Проверка по алгоритму Луна с использованием NumPy
    def luhn_algorithm(card_number):
        card_digits = np.array([int(digit) for digit in card_number.replace(" ", "")])
        card_digits[-2::-2] *= 2
        card_digits[card_digits > 9] -= 9
        return np.sum(card_digits) % 10 == 0

    # Проверка срока действия карты
    def validate_expiry_date(expiry_date):
        try:
            month, year = map(int, expiry_date.split("/"))
            if not (1 <= month <= 12):
                return False
            current_year = int(str(datetime.datetime.now().year)[-2:])
            current_month = datetime.datetime.now().month
            return (year > current_year) or (year == current_year and month >= current_month)
        except ValueError:
            return False

    # Проверка CVC/CVV кода
    def validate_cvc(cvc):
        return cvc.isdigit() and (len(cvc) == 3 or len(cvc) == 4)

    # Проверка всех условий
    if not luhn_algorithm(card_number):
        print("Номер карты недействителен по алгоритму Луна.")
        return False

    if not validate_expiry_date(expiry_date):
        print("Срок действия карты недействителен.")
        return False

    if not validate_cvc(cvc):
        print("CVC/CVV код недействителен.")
        return False

    return True



def bank_answer():
    bank_confirm = input("Введите ответ банка (Yes/No): ").lower()
    if re.match(r'^(y(es)?)$', bank_confirm):
        return True
    elif re.match(r'^(n(o)?)$', bank_confirm):
        print("Отрицательный ответ банка")
        return False
    else:
        print("Неверный ответ банка")
        return False


def payment_check():
    card_balance = float(input("Введите баланс карты: "))
    payment = float(input("Введите стоимость покупки: "))
    if card_balance >= payment:
        payment_check_confirm = input("Подтвердите покупку (Введите Yes/No): ").lower()
        if re.match(r'^(y(es)?)$', payment_check_confirm):
            return True
        elif re.match(r'^(n(o)?)$', payment_check_confirm):
            print("Отрицательный ответ пользователя")
            return False
        else:
            print("Неверный ответ пользователя")
            return False
    else:
        print("Стоимость покупки больше баланса")
        return False


def main():
    # Запрос данных для проверки карты
    card_number = input("Введите номер карты: ")
    expiry_date = input("Введите срок действия карты (ММ/ГГ): ")
    cvc = input("Введите CVC/CVV код: ")

    cardcheck = card_check(card_number, expiry_date, cvc)
    
    if cardcheck:
        bankanswer = bank_answer()
    
    while not (cardcheck) or not (bankanswer):
        print("")
        # Повторный ввод данных при ошибке
        card_number = input("Введите номер карты: ")
        expiry_date = input("Введите срок действия карты (ММ/ГГ): ")
        cvc = input("Введите CVC/CVV код: ")

        cardcheck = card_check(card_number, expiry_date, cvc)
        if cardcheck:
            bankanswer = bank_answer()

    paymentcheck = payment_check()
    if paymentcheck:
        bankanswer = bank_answer()
    
    while not (paymentcheck) or not (bankanswer):
        print("")
        paymentcheck = payment_check()
        if paymentcheck:
            bankanswer = bank_answer()
    print("Операция прошла успешно")


if __name__ == "__main__":
    main()
