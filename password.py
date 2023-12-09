password = "password"

def ask_password():
    for i in range(3):
        p = input("Введите пороль: ")
        if p == password:
            print("ПРИНЯТ!")
            return

    print("В доступе отказано!")


ask_password()
