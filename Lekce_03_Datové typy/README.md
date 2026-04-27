# Lekce 3: Pasti datových typů (String vs. Integer)

Dnes si zahrajeme na detektivy. Python je někdy až moc chytrý a místo toho, aby nahlásil chybu, udělá něco, co nečekáte.

### Teorie (Pamatuj!)
1. `input()` vrací VŽDY text (String).
2. `text + text` = spojení textů (např. "1" + "1" = "11").
3. `text * cislo` = opakování textu (např. "A" * 3 = "AAA").
4. `text - cislo` = **CHYBA (TypeError)**. Python neumí odečítat od textu.

---

## 🔥 Úkoly: Programátorské hádanky
V souboru `main.py` vyřeš následujících 5 úloh. U každé úlohy musíš zajistit, aby program nespadl a počítal matematicky správně.

### 1. Úloha: Sčítací past
Uživatel zadá dvě čísla. Program je musí **sečíst**.
*Pozor:* Pokud nezměníš datový typ, tak z 5 a 3 vznikne 53!

### 2. Úloha: Opakovač jména
Zeptej se uživatele na **jméno** a na **číslo**. Program vypíše jméno tolikrát, kolikrát určuje číslo, a to v jednom řádku.
*Hádanka:* Tady budeš potřebovat jeden vstup jako text a druhý jako číslo.

### 3. Úloha: Rok narození (Pozor na chybu!)
Zeptej se uživatele, kolik mu je let. Program vypíše: "Narodil ses přibližně v roce [rok]".
*Tip:* Aktuální rok (2026) je v kódu jako číslo. Věk od uživatele je text. Musíš je srovnat!

### 4. Úloha: Výplata v hotovosti
Zeptej se na **hodinovou mzdu** (např. 200) a **počet odpracovaných hodin**. Vypiš celkovou odměnu.
*Extra výzva:* Zkus, co se stane, když zapomeneš převést mzdu na číslo a vynásobíš ji hodinami. Pak to oprav!

### 5. Úloha: "Magická" matematika
Uživatel zadá číslo. Program vypíše výsledek tohoto vzorce: `(číslo + 10) * 2`.
*Příklad:* Zadám-li 5, výsledek musí být 30. (Nikoliv 510510).
