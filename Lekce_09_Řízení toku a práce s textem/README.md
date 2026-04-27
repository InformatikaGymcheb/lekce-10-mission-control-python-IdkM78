# Lekce 09: Řízení toku a práce s textem

Pro ovládání cyklů a efektivní spojování textu.

---

## 1. Příkazy pro řízení toku programuPři práci s cykly (for, while) často potřebujeme změnit jejich přirozený běh – například cyklus předčasně ukončit nebo přeskočit určitou část.

### break – okamžité ukončení

Příkaz break úplně přeruší běh smyčky a program pokračuje prvním příkazem za tělem cyklu. 

Příklad:
  
    for i in range(5):
      if i == 3:
          break    # Ukončí smyčku, jakmile i dosáhne hodnoty 3
      print(i)     # Výstup: 0, 1, 2 

### continue – přeskočení iterace

Příkaz continue přeruší pouze aktuální krok (iteraci) smyčky, zbytek kódu v těle cyklu pro tuto hodnotu vynechá a okamžitě přejde k další položce. 

Příklad:
    
    for i in range(5):
      if i == 3:
          continue    # Přeskočí i == 3 a pokračuje číslem 4
      print(i)        # Výstup: 0, 1, 2, 4 

### pass – prázdná operace

Příkaz pass slouží jako zástupný symbol (placeholder). Používá se tam, kde syntaxe vyžaduje blok kódu, ale my v něm zatím nechceme provádět žádnou akci. Pomáhá zabránit chybám u prázdných cyklů nebo funkcí. 

Příklad:

    for x in [0, 1, 2]:
        pass     # Dočasně nic nedělá, ale kód nespadne


## 2. Práce s časem (Pauza v programu)
V Pythonu neexistuje přímý vestavěný příkaz pause. Pokud chceme program na určitou dobu zastavit, používáme funkci sleep() z modulu time. 

Import a použití:

    import time [cite: 29]

    print("Začátek...")
    time.sleep(2)     # Zastaví běh programu na 2 sekundy
    print("Pokračujeme po pauze!")


## 3. Metoda join(): Spojování řetězců
Metoda join() je užitečný nástroj, který umožňuje spojit prvky seznamu nebo n-tice do jednoho textového řetězce pomocí zadaného oddělovače (separatoru). 

### Základní vlastnosti:

#### Oddělovač: 
Specifikujete vlastní znak (např. mezera, čárka, pomlčka), který se vloží mezi prvky. 

#### Datové typy: 
Funguje na seznamech, n-ticích nebo i jednotlivých znacích řetězce. 

#### Omezení: 
Nelze přímo použít na čísla (např. seznam [1, 2, 3]). Metoda vyžaduje pouze textová data, jinak dojde k chybě. 

<br>

***Praktické příklady:***


Spojení slov do věty (mezera):

    slova = ["Ahoj", "jak", "se", "máš"]
    veta = " ".join(slova)    # Výstup: Ahoj jak se máš

Oddělení položek čárkou:

    ovoce = ["jablko", "hruška", "banán"]
    seznam = ", ".join(ovoce)    # Výstup: jablko, hruška, banán

Vytvoření textu na více řádků (\n):

    radky = "\n".join(["První", "Druhý", "Třetí"])    # Každý prvek na novém řádku

Rozdělení slova znakem:

    slovo = "Python"
    rozdeleni = "-".join(slovo)    # Výstup: P-y-t-h-o-n


### 4. Logika cyklů a blok else 
Zajímavou vlastností Pythonu je možnost použít blok else přímo za cyklem for. 
Pravidlo: Blok else se provede pouze tehdy, pokud cyklus doběhl přirozeně do konce (nebyl přerušen příkazem break). 

***Příklady k procvičení:***

Příklad A: Cyklus doběhne do konce

    for i in range(1, 10, 3):
        print(i)
    else:
        print('Hotovo!')     # Výsledek: 1, 4, 7, Hotovo! 

Příklad B: Cyklus je přerušen

    for i in range(1, 10, 3):
      print(i)
      if i > 5:
          break
    else:
          print('Hotovo!')     # Výsledek: 1, 4, 7 (Text 'Hotovo!' se nevypíše, protože došlo k break). 
