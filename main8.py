import time
def countdown_timer(seconds):
    print("Таймер запущено!")
    for i in range(seconds, 0, -1):
        print(f"Залишилося {i} секунд")
        time.sleep(1)
    print("Час вийшов! Таймер завершено.")
def main():
    user_input = input("Введіть час в секундах для таймера: ")
    try:
        seconds = int(user_input)
        if seconds <= 0:
            raise ValueError
        countdown_timer(seconds)
    except ValueError:
        print("Некоректне значення часу. Будь ласка, введіть додатне ціле число.")
if __name__ == "__main__":
    main()
