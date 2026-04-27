# Lekce 2: Interaktivní programy (Funkce INPUT)

Dnes se naučíme, jak do programu dostat data od uživatele. Zatímco `print()` data vypisuje ven, `input()` je načítá dovnitř.

### Teorie
Příkaz `input("Text pro uživatele")` vždy zastaví program a čeká, až uživatel něco napíše a stiskne **Enter**.
**Pozor:** Vše, co uživatel napíše, bere Python jako text (string). Pokud chceš číslo, musíš to převést: `int(input())`.

---

## Tvůj úkol
V souboru `main.py` vypracuj následující tři úlohy. Každou úlohu si vyzkoušej spustit v terminálu pomocí příkazu `python main.py`.

### 1. Úloha: Registrace uživatele
Zeptej se uživatele na jeho **jméno** a **oblíbenou barvu**. Potom vypiš větu:
`Ahoj [jméno], tvoje oblíbená barva je [barva]. To je skvělá volba!`

### 2. Úloha: Jednoduchá kalkulačka (Sčítání)
Zeptej se na **první číslo** a potom na **druhé číslo**. Program vypíše jejich součet.
*Nápověda: Nezapomeň použít `int()` pro převod textu na celé číslo!*

### 3. Úloha: Výpočet věku psa
Zeptej se uživatele, **kolik mu je let**. Program spočítá, kolik by mu bylo let, kdyby byl pes (předpokládejme, že 1 lidský rok = 7 psích let).
Výsledek vypiš ve formátu: `V psích letech by ti bylo: [výsledek] let. Haf!`

---
### 🚀 Jak odevzdat?
1. Otevři si soubor `main.py`.
2. Napiš kód.
3. Spusť ho v terminálu: `python Lekce_02_Input/main.py`
4. Pokud funguje, proveď vlevo v menu **Commit** a **Push**.
