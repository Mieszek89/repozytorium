import csv
from pprint import pp
from sys import argv

# 1. Przecwycenie argumentów wejściowych
try:
    input_file = argv[1]
    output_file = argv[2]
    changes = argv[3:]

# 2. Odczytanie pliku csv
    csv_rows = []
    with open(input_file, encoding='utf-8') as file_stream:
        for line in csv.reader(file_stream):
            csv_rows.append(line)
    pp(csv_rows)
# 3. Zmiany w odczytanym elemencie

    for lines in changes:
        change = lines
        row, column, value = change.split(",")
        csv_rows[int(row)][int(column)] = value

# 4. wyświetlenie zmodyfikowanych wartości
    pp(csv_rows)


# 5. Zapisanie zmian w pliku out

    with open(output_file, "w", encoding='utf-8', newline= '') as file_stream:
        csv_writer = csv.writer(file_stream)
        csv_writer.writerows(csv_rows)

except ValueError: #błąd wartości
    print(f"Podano błędne wartości")

except SyntaxError: #błąd składniowy
    print(f"Wpropowadzono błędny zapis")

except IndexError: #błąd indexu
    print(f"Podano nieprawidłowy index")

except AttributeError:
    print(f"Podano nipoprawny typ danych")

