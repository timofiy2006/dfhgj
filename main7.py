import sys

def main():
    arguments = sys.argv[1:]  
    print("Список аргументів командного рядка:")
    for arg in arguments:
        print(arg)
if __name__ == "__main__":
    main()
