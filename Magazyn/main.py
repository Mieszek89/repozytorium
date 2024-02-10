print(f"Witaj w programie Księgowo-Magazynowym, poniżej przedstawiam dostępne funkcje:\n")

balance = 100
history = []

warehouse = {
    "hulajnoga": {
        "price": 40,
        "quantity": 7,
    },
    "rower": {
        "price": 100,
        "quantity": 3,
    },
}


with open("balance.txt", "w", encoding="UTF-8") as file_stream:
    file_stream.write(f"{balance}")

with open("history.txt", "a", encoding="UTF-8") as file_stream:
    for line in history:
        file_stream.write(line + "\n")

with open("warehouse.txt", "w", encoding="UTF-8") as file_stream:
    for key, value in warehouse.items():
        file_stream.write(f"{key}: {value}\n")

with open('warehouse.txt', 'r') as file:
        file_content = file.readlines()
        print(f"Stan magazynu to:\n")
        for line in file_content:
            print(f"{line}")


while True:

    print(f"1.Saldo - Pobiera kwotę do dodania lub odjęcia z konta.")
    print(f"2.Sprzedaż - Pobiera nazwę produktu, cenę oraz liczbę sztuk.")
    print(f"3.Zakup - Pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu.")
    print(f"4.Konto - Wyświetla stan konta.")
    print(f"5.Lista - Wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.")
    print(f"6.Magazyn - Wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.")
    print(f"7.Przegląd - Wyświetla wszystkie wprowadzone akcje zapisane pod indeksami „od” ... „do”.")
    print(f"8.Koniec - Aplikacja kończy działanie.\n")

    command = input("Wprowadź co chcesz zrobić: ").title()
    # Operacje na saldzie zmienna balance
    if command == "Saldo":
        balance_change = int(input("Wprowadź kwotę do dodania lub odjęcia: "))
        balance += balance_change  # dodaje lub odejmuje warość ze zmiennej balance

        if balance >= 0:
            message = f"Zmieniłeś saldo o {balance_change}"
            print(message)
            history.append(message)

        else:
            balance -= balance_change
            message2 = f"Saldo nie może być na minusie"
            print(message2)
            history.append(message2)

    elif command == "Sprzedaż":
        # Odjęcie z magazynu, dodanie pieniędzy do konta
        product_name = input("Podaj nazwę przedmiotu: ").lower()
        product_quantity = int(input("Podaj ilość przedmiotów do sprzedania: "))
        product = warehouse.get(product_name)  # pobranie produktu product_name ze zmiennej warehouse

        if product:
            warehouse_quantity = product["quantity"]

            if warehouse_quantity - product_quantity >= 0:
                total_price = product["price"] * product_quantity  # Końcowa kwota operacji
                balance += total_price  # Saldo konta po zwiększeniu po przeprowadzeniu operacji sprzedaży
                product["quantity"] -= product_quantity  # Zmniejsza ilości produktu po operacji sprzedaży
                message3 = f"Dokonałeś sprzedaży {product_name} w ilości {product_quantity}"
                print(message3)
                history.append(message3)

            else:
                message4 = f"Nie ma tyle produktów na magazynie - znajduje się tam {warehouse_quantity} produktów"
                print(message4)
                history.append(message4)

        else:
            message5 = f"Nie ma takiego produktu {product_name}"
            print(message5)
            history.append(message5)

    elif command == "Zakup":
        # Dodanie do magazynu, dodanie pieniędzy do konta
        product_name = input("Podaj nazwę przedmiotu: ").lower()
        product_quantity = int(input("Podaj ilość przedmiotów do zakupu: "))
        product_price = int(input("Podaj cenę przedmiotów do zakupu: "))
        product_item = {
            product_name: {
                'price': product_price,
                'quantity': product_quantity,
                }
            }
        total_price = product_quantity * product_price
        balance = balance - total_price
        product = warehouse.get(product_name)

        if balance >= 0:

            if product:
                warehouse_quantity = product["quantity"]
                warehouse_price = product["price"]
                product["quantity"] += product_quantity
                product["price"] = product_price
                message6 = f"Dokonałeś zakupu produktu {product_name} w ilości {product_quantity}"
                history.append(message6)
                print(message6)

            else:
                warehouse.update(product_item)
                message7 = f"Dokonałeś zakupu produktu {product_name} w ilości {product_quantity}"
                history.append(message7)
                print(message7)

        else:
            balance = balance + total_price
            message8 = f"Za mało pieniędzy na koncie nie można dokonać zakupu"
            history.append(message8)
            print(message8)

    elif command == "Konto":
        message9 = f"Stan konta: {balance}"
        print(message9)
        history.append(message9)

    elif command == "Lista":
        message10 = f"{warehouse}"
        print(message10)
        history.append(message10)

    elif command == "Magazyn":
        product_name = input("Podaj nazwę przedmiotu: ").lower()
        product2 = warehouse.get(product_name)
        message11 = f"{product2}"
        print(message11)
        history.append(message11)

    elif command == "Przegląd":
        index = int(input(f"Wprowadź wartości od: "))
        index2 = int(input(f"Wprowadź wartość do: "))
        history_index = history[index:index2]
        message12 = f"{history_index}"
        print(message12)
        history.append(message12)

    elif command == "Koniec":

        with open("balance.txt", "w", encoding="UTF-8") as file_stream:
            file_stream.write(f"balance = {balance}")

        with open("history.txt", "a", encoding="UTF-8") as file_stream:
            for line in history:
                file_stream.write(line + "\n")

        with open("warehouse.txt", "w", encoding="UTF-8") as file_stream:
            for key, value in warehouse.items():
                file_stream.write(f"{key}: {value}\n")


        break

    else:
        message13 = f"Wprowadziłeś błędną komendę"
        print(message13)
        history.append(message13)
