# Lekce 07: Želví grafika a ASCII umění

Dnes opustíme černobílý svět textu a naučíme se kreslit! Python má v sobě zabudovaného umělce – knihovnu **Turtle**. Kromě toho se podíváme na to, jak tvořit obrazy pomocí pouhých písmen (**ASCII Art**).

---

## 1. Knihovna `turtle`: Kreslíme kódem

Představte si malou želvu s perem na břiše, která běhá po vašem monitoru. Kam ji pošlete, tam zanechá barevnou stopu.

### Jak začít?
Nejprve musíme želvu "pozvat" do našeho programu:

    import turtle

    t = turtle.Turtle()  # Vytvoříme naši želvu (říkejme jí 't')

    t.shape("turtle")    # Změníme šipku na skutečnou želvu

    t.speed(3)           # Nastavíme rychlost (1 = pomalá, 10 = rychlá)

### Základní pohyby želvy

    t.forward(100) – jde dopředu o 100 kroků.

    t.right(90) – otočí se doprava o 90 stupňů.

    t.left(45) – otočí se doleva o 45 stupňů.

    t.backward(50) – couvá.

### Barvy a výplně

    t.color("red") – změní barvu čáry.

    t.begin_fill() – začne si pamatovat tvar pro vybarvení.

    t.end_fill() – ukončí tvar a vybarví ho zvolenou barvou.

### Základní pohyby pera
    t.penup() – zvedne pero (želva se hýbe, ale nekreslí).

    t.pendown() – položí pero (začne znovu kreslit).
    
### Kreslení trojúhelníku
    for i in range(3):
      t.forward(100)
      t.left(120)

### Udrží okno otevřené i po dokreslení
    turtle.done()

## 2. ASCII Art: Umění z písmenek

ASCII umění je způsob vytváření obrázků pomocí znaků na klávesnici (tečky, lomítka, mřížky). Je to základní kámen digitálního designu v terminálu.
Jak vypsat ASCII obrázek správně?

Aby se obrázek v Pythonu nerozsypal, používáme tzv. vícenásobné uvozovky """, které zachovají všechny řádky přesně tak, jak je napíšete:

    kocka = ```
```
    /\_/\
    
   ( o.o )
   
    > ^ <
    ```    
```
    print(kocka)

Tip: Skvělou sbírku těchto obrázků najdeš na (asciiart.eu). Stačí zkopírovat a vložit do ``` (tři zpětné apostrofy).
