strzaly_marysi = 5
# Zmiana liczby strzałów Marysi na 0

while strzaly_marysi > 0:
    akcja = input("Naciśnij Enter, aby usunąć strzał Marysi (lub wpisz 'exit' aby zakończyć): ")

    if akcja == "exit":
        print("Koniec gry. Marysia ma jeszcze", strzaly_marysi, "strzałów.")
        break

    if strzaly_marysi > 0:
        strzaly_marysi -= 1
        print("Strzał usunięty! Marysia ma jeszcze", strzaly_marysi, "strzałów.")
    else:
        print("Marysia strzelał(a) wszystkimi palcami, nie ma już więcej strzałów.")
