import random
import webbrowser

def random_location():
    x = format(random.uniform(-90.0, 90.0), '.7f') 
    y = format(random.uniform(-180.0, 180.0), '.7f')

    xy = "https://www.google.ru/maps/@" + x + "," + y + ",12z"

    return webbrowser.open(xy)

def validator(command):
    while True:
        if command == "generate":
            random_location()
            print("\n")
            break            
        else:
            command = input("Команда введена неверно, повторите попытку: ")

command = input("Чтобы сгенерирорвать случайные координаты\n"
       "и открыть их на сайте Google Maps, введите \"generate\":\n\n")

validator(command)

while True:
    question = input("Введите нужную Вам команду:\n\n"
          "restart -  сгенерировать новые координаты\n"
          "quit - завершить работу\n\n")
    if question == "restart":
        print("\n")
        random_location()
    elif question == "quit":
        break            
