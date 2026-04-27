# Efektivní matematika a zaokrouhlování

Jak psát méně kódu při počítání a jak zkrotit dlouhá desetinná čísla.

### 1. Zkrácené zápisy (In-place operátory)
Často potřebujeme změnit hodnotu proměnné (např. přičíst 1 k věku nebo přičíst body v hře). 
Místo dlouhého psaní existuje zkratka:

| Dlouhý zápis | Zkrácený zápis | Co to udělá? |
| :--- | :--- | :--- |
| `x = x + 5` | `x += 5` | Přičte 5 k původní hodnotě |
| `x = x - 2` | `x -= 2` | Odečte 2 |
| `x = x * 3` | `x *= 3` | Vynásobí původní hodnotu |
| `x = x / 4` | `x /= 4` | Vydělí původní hodnotu |

**Pamatuj:** Znaménko je vždy před rovnítkem! `+=`, `-=`, `*=`.

### 2. Zaokrouhlování: `round()`
Python při dělení často vyhazuje čísla jako `3.33333333335`. Pro krásný výstup používáme funkci `round()`.

**Syntaxe:** `round(číslo, počet_míst)`

* `round(3.14159, 2)` -> Výsledek: `3.14`
* `round(3.14159)` -> Výsledek: `3` (zaokrouhlí na celé číslo)

Pokud je číslo přesně uprostřed (např. 2.5 nebo 3.5), zaokrouhluje k nejbližšímu sudému číslu.

    round(2.5) -> 2
    round(3.5) -> 4
    
---

**Bonus: formátovací specifikátor - zaokrouhlí číslo přímo při výpisu**

Nula na konci (Zásadní rozdíl!):
*    round(10.5, 2) vypíše: **10.5** (Python nepotřebné nuly maže)
*    f"{10.5:.2f}" vypíše: **10.50** (Vypadá to jako peníze).
    
Zápis s dvojtečkou je sice šifra, ale je kratší.
*    print(f"Zaplatíte {round(cena, 2)} Kč a zbývá {round(zbytek, 2)} Kč.")    
*    print(f"Zaplatíte {cena:.2f} Kč a zbývá {zbytek:.2f} Kč.")

:.2f číslo **nezmění**. V paměti však zůstává super přesné (třeba 10 desetinných míst), ale uživatel na obrazovce vidí jen ty dvě. Je to jen "maska".
round() to číslo skutečně **změní**. Pokud ho pak použijete v dalším výpočtu, počítáte už s tím "ořezaným".

---

## Úkoly v main.py

1. **Zvětšovač:** Uživatel zadá číslo. Pomocí zkráceného zápisu `+=` k němu přičti 10 a výsledek vypiš.
2. **Útrata v hospodě:** Zeptej se na celkovou sumu účtu a počet lidí. Vypiš, kolik má každý zaplatit, ale zaokrouhli to na **2 desetinná místa**.
3. **Plocha kruhu:** Uživatel zadá poloměr `r`. Spočítej plochu ($S = 3.14 * r^2$). Výsledek vypiš zaokrouhlený na **celé číslo**.
