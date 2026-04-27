## Lekce 5: Vestavěné funkce

V této lekci se naučíme používat nástroje, které má Python už v sobě zabudované. Fungují podobně jako funkce v Excelu (SUM, MIN, MAX).

### Základní funkce pro čísla
- `sum(seznam)` – sečte všechna čísla v seznamu.
- `min(seznam)` – najde nejmenší hodnotu.
- `max(seznam)` – najde největší hodnotu.
- `len(seznam)` – (z anglického *length*) – vrátí počet prvků v seznamu.
- `abs(číslo)` – vrátí absolutní hodnotu (odstraní mínus).

### Jak spočítat průměr?
Python nemá přímo funkci `average`. Průměr spočítáme tak, že součet vydělíme počtem prvků:
`prumer = sum(cisla) / len(cisla)`

### Tip pro praxi
Funkce se dají vnořovat do sebe. Například:

`print(round(sum(ceny) / len(ceny), 2))` 
*(Tento kód sečte ceny, vydělí je počtem a výsledek zaokrouhlí na 2 místa).*

<br>

*Jednoduchý výpis:*

hodnoty = [5, 10, 15]
print(sum(hodnoty)) &nbsp;&nbsp;&nbsp;   # Vypíše: 30

*Hezký výpis s textem (f-string):*

print(f"Celkové skóre je: {sum(hodnoty)} bodů.")

*Kombinace s výpočtem (Průměr):*

prumer = sum(hodnoty) / len(hodnoty)
print(f"Tvůj průměr je: {round(prumer, 2)}")
