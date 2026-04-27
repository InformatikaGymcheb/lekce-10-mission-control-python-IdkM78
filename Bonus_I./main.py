#Python není jen suchá tabulka, ale nástroj, kterým můžeme analyzovat i úplné hlouposti nebo zajímavosti z blízkého světa.
#len() funguje na text úplně stejně jako na seznamy čísel.

#Úloha: "Analýza tvého jména"
Věděli jste, že len() nefunguje jen na seznamy čísel, ale i na text?
jmeno = input("Zadej své jméno: ")
delka = len(jmeno)
print(f"Tvé jméno má {delka} písmen.")

# Vtipná vsuvka: Kolikrát bys musel jméno napsat, aby mělo 1 kilometr?
# (Předpokládejme, že jedno písmeno má 0.5 cm)
pocet_na_kilometr = 100000 / (delka * 0.5)
print(f"Abys svým jménem pokryl cestu od školy k nádraží (1 km), musel bys ho napsat {round(pocet_na_kilometr)} krát!")


#Úloha: "Detektor nálady ve třídě" 😊
#Vvytvoř "průměrnou náladu". Ohodnoť svůj dnešek číslem 1–10 (1 = chci spát, 10 = dneska ovládnu svět), k tomu přidej i ohodnecení ostatních.
nalady = [8, 5, 2, 9, 7, 4, 10, 6] 

prumer_tridy = sum(nalady) / len(nalady)
print(f"Aktuální nálada ve třídě je: {prumer_tridy:.1f} z 10.")

if prumer_tridy > 7:
    print("Dneska jsme v pohodě, můžeme kódovat!")
else:
    print("Měli bychom si dát pauzu na čaj.")

#Kdo ze třídy by se upsal nejméně? (Kdo má nejdelší jméno?)
