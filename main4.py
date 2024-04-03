from datetime import datetime
def days_until_birthday(name, birthdate):
    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d")
    current_date = datetime.now()
    if (current_date.month, current_date.day) > (birthdate_obj.month, birthdate_obj.day):
        next_birthday_year = current_date.year + 1
    else:
        next_birthday_year = current_date.year
    next_birthday = datetime(next_birthday_year, birthdate_obj.month, birthdate_obj.day)
    days_until_next_birthday = (next_birthday - current_date).days
    return f"Привіт, {name}! До твого наступного дня народження залишилося {days_until_next_birthday} днів."
def main():
    name = input("Введіть ваше ім'я: ")
    birthdate = input("Введіть вашу дату народження у форматі РРРР-ММ-ДД: ")
    print(days_until_birthday(name, birthdate))
if __name__ == "__main__":
    main()
