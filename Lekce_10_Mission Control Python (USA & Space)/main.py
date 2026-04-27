# =============================================================
# MISE APOLLO 11 - PROGRAMOVACÍ VÝZVA
# =============================================================
# Tvým úkolem je dokončit software pro lunární modul Eagle.
# NASA spoléhá na tvůj kód!
# =============================================================

def vypocet_vahy(vaha_na_zemi, teleso="mesic"):
    """
    Vypočítá váhu astronauta na jiném tělese.
    Měsíc: 16.5 % váhy na Zemi (koeficient 0.165)
    Mars: 38 % váhy na Zemi (koeficient 0.38)
    """
    # BONUS: Sem doplň kontrolu, zda vaha_na_zemi není záporná.
    # Pokud ano, vypiš varování nebo vrať 0.
    
    # TODO: Pomocí podmínek if/elif/else spočítej výslednou váhu
    vysledek = 0 
    
    return vysledek


def simulator_pristani():
    """
    Simulátor přistání modulu na povrchu Měsíce.
    """
    vyska = 100       # počáteční výška v metrech
    rychlost = 10     # počáteční rychlost klesání (m/s)
    palivo = 50       # jednotky paliva
    gravitace = 2     # kolik rychlosti přibude každou sekundu pádem
    
    print("\n--- ZAČÍNÁ PŘISTÁVACÍ MANÉVR ---")
    
    # TODO: Uprav podmínku cyklu, aby běžel, dokud je modul nad zemí (vyska > 0)
    while False: 
        print(f"Výška: {vyska}m | Rychlost: {rychlost}m/s | Palivo: {palivo}j")
        
        # TODO: Získej od uživatele sílu zážehu motorů (vstup od 0 do 10)
        # Nezapomeň převést vstup na celé číslo (int).
        zazeh = 0      # místo nuly bude vstup od uživatele a dojde ke zpomalení pádu
        
        # TODO: Odečti použitý zážeh od paliva, musíme zařídit, aby „nádrž“ modulu postupně ubývala (pozor, nesmí jít do mínusu!)
        
        # --- FYZIKÁLNÍ VÝPOČET ---
        # TODO: Aktualizuj rychlost (přičti gravitaci, odečti zážeh)
        # TODO: Aktualizuj výšku (odečti aktuální rychlost od výšky)
        
        # Jen pro přehlednost v terminálu
        print("-" * 20)

    # --- VYHODNOCENÍ ---
    print(f"\nDopadová rychlost: {rychlost} m/s")
    
    # TODO: Doplň podmínku - pokud je rychlost menší než 5, mise je úspěšná.
    # Jinak modul havaroval.
    print("Výsledek mise: ...")


# === HLAVNÍ PROGRAM ===
# Zde si student vyzkoušej své funkce
moje_vaha = 80
print(f"Moje váha na Měsíci: {vypocet_vahy(moje_vaha, 'mesic')} kg")

# Spuštění simulátoru
# simulator_pristani()
