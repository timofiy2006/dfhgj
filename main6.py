from datetime import datetime

def difference_in_seconds(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d")
    difference_seconds = abs((date2_obj - date1_obj).total_seconds())
    return difference_seconds
def main():
    print("Введіть першу дату у форматі YYYY-MM-DD:")
    date1 = input()
    print("Введіть другу дату у форматі YYYY-MM-DD:")
    date2 = input()
    difference = difference_in_seconds(date1, date2)
    print("Різниця між цими датами в секундах:", difference)
if __name__ == "__main__":
    main()
