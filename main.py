def atm():
    pin = 1111
    total_sum = 10_000_000
    print("1", "UZB")
    print("2", "RUS")
    print("3", "ENG")
    lan = int(input("Choose a language / Выберите язык / Tilni tanlang: "))

    lang = {
        "UZB": {
            "welcome": "O'zbek tili tanlandi.",
            "password_prompt": "Plastik karta paroli: ",
            "wrong_password": "Parol xato.",
            "menu": [
                "Balansni tekshirish",
                "Naqd pul olish",
                "SMS xabarlarni boshqarish",
                "Parolni o'zgartirish",
                "Mobil aloqa uchun to'lov",
                "Kredit to'lovlari",
                "Kommunal to'lovlar",
                "Dasturdan chiqish"
            ],
            "balance_check": "Balansingizda",
            "sum_left": "so'm mablag' mavjud.",
            "amount_left": "so'm qoldi.",
            "withdraw": [
                "50 000 so'm",
                "100 000 so'm",
                "150 000 so'm",
                "200 000 so'm",
                "300 000 so'm",
                "400 000 so'm",
                "Boshqa summa kiriting"
            ],
            "enter_sum": "Summa kiriting: ",
            "insufficient": "Mablag' yetarli emas.",
            "sms_options": ["SMS xabarni o'chirish", "SMS xabarni yoqish"],
            "enter_phone": "Telefon raqamini kiriting (+998 bilan): ",
            "sms_disabled": " raqam uchun SMS xabarlari o'chirildi.",
            "sms_enabled": " raqam uchun SMS xabarlari yoqildi.",
            "mobile_payment": "Mobil aloqa uchun to'lov:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "To'lov summasini kiriting: ",
            "payment_successful": " to'lovi amalga oshirildi. Qolgan balans: ",
            "password_change": "Parolni o'zgartirish:",
            "password_old": "Joriy parolni kiriting: ",
            "password_new": "Yangi parolni kiriting: ",
            "password_confirm": "Yangi parolni qayta kiriting: ",
            "password_changed": "Yangi parol muvaffaqiyatli o'rnatildi.",
            "credit_prompt": "Kredit to'lovi summasini kiriting: ",
            "utility_prompt": "Kommunal to'lov summasini kiriting: ",
            "exit": "Dasturdan chiqish"
        },
        "RUS": {
            "welcome": "Русский язык выбран.",
            "password_prompt": "Пароль банковской карты: ",
            "wrong_password": "Неправильный пароль.",
            "menu": [
                "Проверить баланс",
                "Снятие наличных",
                "Управление SMS-сообщениями",
                "Смена пароля",
                "Оплата мобильной связи",
                "Погашение кредита",
                "Оплата коммунальных услуг",
                "Выход из программы"
            ],
            "balance_check": "На вашем счёте",
            "sum_left": "сум доступны.",
            "amount_left": "сум осталось.",
            "withdraw": [
                "50 000 сум",
                "100 000 сум",
                "150 000 сум",
                "200 000 сум",
                "300 000 сум",
                "400 000 сум",
                "Введите другую сумму"
            ],
            "enter_sum": "Введите сумму: ",
            "insufficient": "Недостаточно средств.",
            "sms_options": ["Отключить SMS", "Подключить SMS"],
            "enter_phone": "Введите номер телефона (начиная с +998): ",
            "sms_disabled": " для номера отключены SMS-сообщения.",
            "sms_enabled": " для номера подключены SMS-сообщения.",
            "mobile_payment": "Оплата мобильной связи:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "Введите сумму платежа: ",
            "payment_successful": "Платёж выполнен. Остаток на балансе: ",
            "password_change": "Смена пароля:",
            "password_old": "Введите текущий пароль: ",
            "password_new": "Введите новый пароль: ",
            "password_confirm": "Повторите новый пароль: ",
            "password_changed": "Новый пароль успешно установлен.",
            "credit_prompt": "Введите сумму платежа по кредиту: ",
            "utility_prompt": "Введите сумму коммунального платежа: ",
            "exit": "Выход из программы"
        },
        "ENG": {
            "welcome": "English language selected.",
            "password_prompt": "Card PIN: ",
            "wrong_password": "Incorrect PIN.",
            "menu": [
                "Check balance",
                "Withdraw cash",
                "Manage SMS messages",
                "Change PIN",
                "Mobile payment",
                "Credit payments",
                "Utility payments",
                "Exit application"
            ],
            "balance_check": "Your balance is",
            "sum_left": "so'm available.",
            "amount_left": "so'm left.",
            "withdraw": [
                "50 000 so'm",
                "100 000 so'm",
                "150 000 so'm",
                "200 000 so'm",
                "300 000 so'm",
                "400 000 so'm",
                "Enter another amount"
            ],
            "enter_sum": "Enter amount: ",
            "insufficient": "Insufficient funds.",
            "sms_options": ["Disable SMS notifications", "Enable SMS notifications"],
            "enter_phone": "Enter phone number (starting with +998): ",
            "sms_disabled": " SMS notifications disabled for the number.",
            "sms_enabled": " SMS notifications enabled for the number.",
            "mobile_payment": "Mobile payment:",
            "operator_select": ["UzMobile", "Beeline", "Ucell", "UMS", "Perfectum"],
            "enter_amount": "Enter the payment amount: ",
            "payment_successful": "Payment completed. Remaining balance: ",
            "password_change": "Change PIN:",
            "password_old": "Enter current PIN: ",
            "password_new": "Enter new PIN: ",
            "password_confirm": "Re-enter new PIN: ",
            "password_changed": "New PIN set successfully.",
            "credit_prompt": "Enter the credit payment amount: ",
            "utility_prompt": "Enter the utility payment amount: ",
            "exit": "Exit application"
        }

    }

    lang_selected = "UZB" if lan == 1 else "RUS" if lan == 2 else "ENG"
    print(lang[lang_selected]["welcome"])

    # password check
    entering_pin = int(input(lang[lang_selected]["password_prompt"]))
    if entering_pin == pin:
        while True:
            for i, option in enumerate(lang[lang_selected]["menu"], 1):
                print(f"{i}, {option}")
            menu = int(input("Select an option: "))
            if menu == 1:
                print(f"{lang[lang_selected]['balance_check']} {total_sum} "
                      f"{lang[lang_selected]['sum_left']}")
            elif menu == 2:
                print("\n".join(lang[lang_selected]["withdraw"]))
                cash = int(input(lang[lang_selected]["enter_sum"]))
                if total_sum >= cash:
                    total_sum -= cash
                    print(f"-----{lang[lang_selected]['balance_check']} {total_sum} "
                          f"{lang[lang_selected]['amount_left']}----")
                else:
                    print(f"-----{lang[lang_selected]['insufficient']}--------")
            elif menu == 3:
                print(f"1. {lang[lang_selected]['sms_options'][0]}")
                print(f"2. {lang[lang_selected]['sms_options'][1]}")
                sms = int(input("-----Choose: "))
                phone_number = input(lang[lang_selected]["enter_phone"])
                if sms == 1:
                    print(f"  ------{phone_number}{lang[lang_selected]['sms_disabled']}------")
                else:
                    print(f"  ------{phone_number}{lang[lang_selected]['sms_enabled']}------")

            elif menu == 4:
                print(lang[lang_selected]["password_change"])
                old_pin = int(input(lang[lang_selected]["password_old"]))
                if old_pin == pin:
                    new_pin = int(input(lang[lang_selected]["password_new"]))
                    re_new_pin = int(input(lang[lang_selected]["password_confirm"]))
                    if new_pin == re_new_pin:
                        pin = new_pin
                        print(lang[lang_selected]["password_changed"])
                    else:
                        print("Error: PIN do not match")
                else:
                    print(lang[lang_selected]["wrong_password"])
            elif menu == 5:
                print(lang[lang_selected]["mobile_payment"])
                for i, operator in enumerate(lang[lang_selected]["operator_select"], 1):
                    print(f"{i}, {operator}")
                operator_choice = int(input("---- Select your operator"))
                input(lang[lang_selected]["enter_phone"])
                sum = int(input(lang[lang_selected]["enter_amount"]))

                if total_sum >= sum:
                    total_sum -= sum
                    print(f"----{lang[lang_selected]['operator_select'][operator_choice - 1]}"
                          f"{lang[lang_selected]['payment_successful']} {total_sum}"
                          f"{lang[lang_selected]['amount_left']}----")
                else:
                    print(lang[lang_selected]["insufficient"])
            elif menu == 8:
                print(lang[lang_selected][exit])
                break

            else:
                print("Error: Invalid option")
    else:
        print(lang[lang_selected]["wrong_password"])


atm()
