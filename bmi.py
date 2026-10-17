from math import isfinite


def pobierz_liczbe_z_zakresu(komunikat, minimum, maksimum):
    while True:
        wartosc = input(komunikat).strip().replace(",", ".")
        try:
            liczba = float(wartosc)
            if isfinite(liczba) and minimum <= liczba <= maksimum:
                return liczba
        except ValueError:
            print("To nie jest poprawna liczba.")
            continue
        print(f"Podaj liczbę z zakresu {minimum}–{maksimum}.")


def pobierz_imie():
    while True:
        imie = input("Podaj imię: ").strip()
        if imie:
            return imie
        print("Imię nie może być puste.")


def interpretuj_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    if bmi < 25.0:
        return "waga prawidłowa"
    if bmi < 30.0:
        return "nadwaga"
    return "otyłość"


def oblicz_i_zapisz_wynik(results):
    imie = pobierz_imie()
    wzrost = pobierz_liczbe_z_zakresu("Podaj wzrost w cm (80–250): ", 80, 250)
    masa = pobierz_liczbe_z_zakresu("Podaj masę ciała w kg (20–300): ", 20, 300)

    bmi = round(masa / (wzrost / 100) ** 2, 2)
    kategoria = interpretuj_bmi(bmi)
    results.append({"imie": imie, "wzrost": wzrost, "masa": masa, "bmi": bmi, "kategoria": kategoria})
    print(f"{imie}, Twoje BMI wynosi {bmi:.2f}: {kategoria}.")


def wyswietl_historie(results):
    if not results:
        print("Historia jest pusta.")
        return

    print("\nHistoria wyników:")
    for numer, wynik in enumerate(results, start=1):
        print(f"{numer}. {wynik['imie']}: BMI {wynik['bmi']:.2f} - {wynik['kategoria']}")


def usun_wynik(results):
    if not results:
        print("Nie ma wyników do usunięcia.")
        return

    wyswietl_historie(results)
    try:
        numer = int(input("Podaj numer wyniku do usunięcia: ").strip())
    except ValueError:
        print("Podaj poprawny numer z historii.")
        return

    if not 1 <= numer <= len(results):
        print("Nie ma wyniku o takim numerze.")
        return

    usuniety = results.pop(numer - 1)
    print(f"Usunięto wynik osoby: {usuniety['imie']}.")


def wyswietl_podsumowanie(results):
    if not results:
        print("Brak wyników do podsumowania.")
        return

    wartosci_bmi = [wynik["bmi"] for wynik in results]
    liczebnosci = {kategoria: 0 for kategoria in ("niedowaga", "waga prawidłowa", "nadwaga", "otyłość")}
    for wynik in results:
        liczebnosci[wynik["kategoria"]] += 1

    print("\nPodsumowanie:")
    print(f"Liczba osób: {len(results)}")
    print(f"Średnie BMI: {sum(wartosci_bmi) / len(wartosci_bmi):.2f}")
    print(f"Minimum BMI: {min(wartosci_bmi):.2f}")
    print(f"Maksimum BMI: {max(wartosci_bmi):.2f}")
    print("Liczba osób w kategoriach:")
    for kategoria, liczba in liczebnosci.items():
        print(f"- {kategoria}: {liczba}")


def wyswietl_menu():
    print("\n=== Kalkulator BMI ===")
    print("1. Oblicz BMI")
    print("2. Wyświetl historię")
    print("3. Wyświetl podsumowanie")
    print("4. Usuń wynik z historii")
    print("0. Zakończ")


def main():
    results = []
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ").strip()
        if wybor == "1":
            oblicz_i_zapisz_wynik(results)
        elif wybor == "2":
            wyswietl_historie(results)
        elif wybor == "3":
            wyswietl_podsumowanie(results)
        elif wybor == "4":
            usun_wynik(results)
        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowa opcja. Wybierz 0, 1, 2, 3 lub 4.")


if __name__ == "__main__":
    main()