import random
import webbrowser


def create_location_url():
    x = format(random.uniform(-90.0, 90.0), '.7f') 
    y = format(random.uniform(-180.0, 180.0), '.7f')
    url = "https://www.google.ru/maps/@" + x + "," + y + ",12z"
    return url


def validator(command):
    while True:
        if command.lower() == "generate":
            url = create_location_url()
            webbrowser.open(url)
            print("\n")
            break            
        else:
            command = input("Команда введена неверно, повторите попытку: ")


def main():
    command = input("Чтобы сгенерирорвать случайные координаты\n"
        "и открыть их на сайте Google Maps, введите \"generate\":\n")
    validator(command)
    while True:
        question = input("Введите нужную Вам команду:\n"
            "restart -  сгенерировать новые координаты\n"
            "quit - завершить работу\n")
        if question.lower() == "restart":
            print("\n")
            url = create_location_url()
            webbrowser.open(url)
        elif question.lower() == "quit":
            break       
        else:
            print("\n")     


if __name__ == "__main__":
    main()
