## 1. Výstup dat: print()

Funkce print() posílá informace z počítače na obrazovku.

    Text (String): Musí být vždy v uvozovkách (jedno ' nebo dvojité ").
    Čísla: Píšou se přímo.
    Více věcí najednou: Oddělujeme je čárkou.

print("Ahoj světe!")         # Vypíše text
print(42)                    # Vypíše číslo
print("Výsledek je:", 10+5)  # Vypíše text a hned za ním výpočet (15)


## 2. Vstup dat: input()

Zastaví program a čeká na uživatele.

    Zlaté pravidlo: Vše, co vyleze z input(), je pro Python TEXT (String). I kdyby uživatel napsal 123, Python to vidí jako slovo "123".

jmeno = input("Jak se jmenuješ? ")
print("Ahoj", jmeno)


## 3. Převod typů (Casting)

Abychom mohli s číslem od uživatele počítat, musíme ho „přebalit“ z textu na celé číslo pomocí int().
| Funkce |	Co dělá	| Příklad |
| -------- | --------- | -------- |
int() |	Změní text na celé číslo |	int("10") -> 10 |
str() |	Změní cokoli na text |	str(10) -> "10" |
float() |	Pro desetinná čísla	float("3.14") -> 3.14 |

## 4. F-stringy (Elegantní vypisování)

Místo složitého spojování pomocí čárek nebo znamének + používáme f-stringy. Stačí dát před uvozovky písmeno f a proměnné vložit do složených závorek { }.

vek = 18
print(f"Příští rok Ti bude {vek + 1} let.")
print(f"Ahoj { jmeno }") -> Mezery v závorkách nejsou chyba, ale vypadá to nehezky.
print("Příští rok Ti bude ", věk + 1, " let.") ← Tohle je "stará škola"

## 5. Komentáře

Vše za znakem mřížky # Python ignoruje. Slouží pro komentáře nebo poznámky.

**# Tohle je poznámka, program ji přeskočí**

## Časté chyby

    **Velká a malá písmena:** Python je citlivý. Print() nefunguje, musí být print(). Vek a vek jsou dvě různé proměnné.
    **Chybějící uvozovky:** print(Ahoj) skončí chybou NameError, protože Python si myslí, že Ahoj je proměnná, kterou jste zapomněli definovat.
    **Desetinná tečka:** V Pythonu nepoužíváme čárku, ale tečku (např. 3.14).
    
