# Zmienne
Months = ("Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "lipiec",
          "Sierpien", "Wrzesien", "Październik", "Listopad", "Grudzien")

Inflation1 = [1.59, -0.45, 2.32, 1.26, 1.78, 2.33, 1.50, 1.78, 2.33, 0.62, 2.35, 0.34]
Inflation2 = [1.58, -0.29, 2.48, 0.27, 1.42, 1.05, 1.48, 1.58, -0.08, 1.16, -0.40, 1.50]

# Miejsce do wprowadzenia danych

Credit = float(input("Kwota kredytu:"))
Interest = float(input("oprocentowanie:"))
Installment = float(input("rata:"))

# Wyliczenia w pierwszym roku

January = ((Credit * (Interest + Inflation1[0]) / 100) / 12) + Credit - Installment
Difference = Credit - January
February = ((January * (Interest + Inflation1[1]) / 100) / 12) + January - Installment
Difference2 = January - February
March = ((February * (Interest + Inflation1[2]) / 100) / 12) + February - Installment
Difference3 = February - March
April = ((March * (Interest + Inflation1[3]) / 100) / 12) + March - Installment
Difference4 = March - April
May = ((April * (Interest + Inflation1[4]) / 100) / 12) + April - Installment
Difference5 = April - May
June = ((May * (Interest + Inflation1[5]) / 100) / 12) + May - Installment
Difference6 = May - June
July = ((June * (Interest + Inflation1[6]) / 100) / 12) + June - Installment
Difference7 = June - July
August = ((July * (Interest + Inflation1[7]) / 100) / 12) + July - Installment
Difference8 = July - August
September = ((August * (Interest + Inflation1[8]) / 100) / 12) + August - Installment
Difference9 = August - September
October = ((September * (Interest + Inflation1[9]) / 100) / 12) + September - Installment
Difference10 = September - October
November = ((October * (Interest + Inflation1[10]) / 100) / 12) + October - Installment
Difference11 = October - November
December = ((November * (Interest + Inflation1[11]) / 100) / 12) + November - Installment
Difference12 = November - December

Mon = [January, February, March, April, May, June, July, August, September, October, November, December]

print("1 rok")
print(f"Twoja pozostała kwota kredytu to:, {Months[0], Mon[0]},To o {Difference:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[1], Mon[1]},To o {Difference2:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[2], Mon[2]},To o {Difference3:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[3], Mon[3]},To o {Difference4:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[4], Mon[4]},To o {Difference5:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[5], Mon[5]},To o {Difference6:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[6], Mon[6]},To o {Difference7:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[7], Mon[7]},To o {Difference8:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[8], Mon[8]},To o {Difference9:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[9], Mon[9]},To o {Difference10:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[10], Mon[10]},To o {Difference11:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[11], Mon[11]},To o {Difference12:.2f}, mniej niż w poprzednim miesiącu")

# Wyliczenia dla drugiego roku

January2 = ((December * (Interest + Inflation2[0]) / 100) / 12) + December - Installment
difference = December - January2
February2 = ((January2 * (Interest + Inflation2[1]) / 100) / 12) + January2 - Installment
difference2 = January2 - February2
March2 = ((February2 * (Interest + Inflation2[2]) / 100) / 12) + February2 - Installment
difference3 = February2 - March2
April2 = ((March2 * (Interest + Inflation2[3]) / 100) / 12) + March2 - Installment
difference4 = March2 - April2
May2 = ((April2 * (Interest + Inflation2[4]) / 100) / 12) + April2 - Installment
difference5 = April2 - May2
June2 = ((May2 * (Interest + Inflation2[5]) / 100) / 12) + May2 - Installment
difference6 = May2 - June2
July2 = ((June2 * (Interest + Inflation2[6]) / 100) / 12) + June2 - Installment
difference7 = June2 - July2
August2 = ((July2 * (Interest + Inflation2[7]) / 100) / 12) + July2 - Installment
difference8 = July2 - August2
September2 = ((August2 * (Interest + Inflation2[8]) / 100) / 12) + August2 - Installment
difference9 = August2 - September2
October2 = ((September2 * (Interest + Inflation2[9]) / 100) / 12) + September2 - Installment
difference10 = September2 - October2
November2 = ((October2 * (Interest + Inflation2[10]) / 100) / 12) + October2 - Installment
difference11 = October2 - November2
December2 = ((November2 * (Interest + Inflation2[11]) / 100) / 12) + November2 - Installment
difference12 = November2 - December2

Mon2 = [January2, February2, March2, April2, May2, June2, July2, August2, September2, October2, November2, December2]

print("2 rok")
print(f"Twoja pozostała kwota kredytu to:, {Months[0], Mon2[0]},To o {difference:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[1], Mon2[1]},To o {difference2:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[2], Mon2[2]},To o {difference3:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[3], Mon2[3]},To o {difference4:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[4], Mon2[4]},To o {difference5:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[5], Mon2[5]},To o {difference6:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[6], Mon2[6]},To o {difference7:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[7], Mon2[7]},To o {difference8:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[8], Mon2[8]},To o {difference9:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[9], Mon2[9]},To o {difference10:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[10], Mon2[10]},To o {difference11:.2f}, mniej niż w poprzednim miesiącu")
print(f"Twoja pozostała kwota kredytu to:, {Months[11], Mon2[11]},To o {difference12:.2f}, mniej niż w poprzednim miesiącu")
