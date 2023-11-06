credentials = {
    "username": 'Тест',
    "patronymic": 'Тест',
    "email": 'irina.vasileva.qa@gmail.com',
    "vosh_login": 'v00.000.000',
    "surname": 'Тест',
    "date_birth": '11.11.2011',
    "phone": 9876543210,
    "snils": 15179977012,
    "profession": 'Школьник',
    "city": 'Москва',
    "organization": 'Организация',
    "school": 1234,
    "class": '5Б'
}

# Варианты валидных значений:
surnames = ("Иванова-Сидорова", "Ем", "Христорождественская", " Петров ", "сидоров")
names = ("Анна-Мария", "Ян", "Абдурахмангаджи", " Петр ", "олег")
patronymics = (" Петрович ", "олегович", "Магомедаминович", "")
phone_numbers = ("+79991234567", "999-999-99-99", "+7(999)1234567", "+7(999)123-45-67")

# Варианты невалидных значений:
invalid_emails = ("irina.vasileva.qa@gmail", "irina.vasileva.gmail.com", "irina.vasileva qa@gmail.com")
