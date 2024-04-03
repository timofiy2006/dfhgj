import random
def generate_random_name():
    names = ["Андрій", "Олена", "Іван", "Марія", "Петро", "Оксана"]
    surnames = ["Петров", "Іванов", "Сидоров", "Коваленко", "Павленко", "Коваль"]
    random_name = random.choice(names)
    random_surname = random.choice(surnames)
    return random_name + " " + random_surname
def main():
    random_full_name = generate_random_name()
    print("Згенероване випадкове ім'я та прізвище:", random_full_name)
if __name__ == "__main__":
    main()
