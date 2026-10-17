# ProgrPython

## Program BMI

Program oblicza BMI dla wielu osób podczas jednej sesji. Wyniki zaokrągla do dwóch miejsc po przecinku i przechowuje w liście słowników `results` w pamięci. Imię nie może być puste, wzrost musi mieścić się w zakresie 80–250 cm, a masa w zakresie 20–300 kg. Niepoprawne i puste dane są odrzucane, a program prosi o ich ponowne podanie. Można używać przecinka lub kropki dziesiętnej.

Menu programu:

- `1` - oblicz BMI kolejnej osoby
- `2` - wyświetl historię wyników
- `3` - wyświetl podsumowanie: liczbę osób, średnie, minimalne i maksymalne BMI oraz liczebność kategorii
- `4` - usuń wybrany wynik z historii
- `0` - zakończ program

Wyniki można dodawać, wyświetlać i usuwać. Historia istnieje tylko w pamięci podczas bieżącej sesji; po zakończeniu programu zostaje utracona.

Utwórz środowisko wirtualne:

```bash
python3 -m venv .venv
```

Aktywuj je i uruchom program:

```bash
source .venv/bin/activate
python bmi.py
```

Program nie wymaga instalowania dodatkowych pakietów.