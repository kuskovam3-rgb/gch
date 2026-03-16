# ==========================================================
# ÚKOL: OPRAV ROZBITÝ AUTOMAT NA PITÍ
# Cíl: Automat musí vydat nápoj podle toho, kolik máš kreditů.
# V kódu je 5 chyb (v syntaxi i v logice). Najdi je!
# ==========================================================

# CENÍK: 
# Kola = 30 kreditů
# Voda = 15 kreditů
# Jinak = Nedostatek kreditů

kredity = input("Zadej počet svých kreditů: ")

# Tady začíná rozbitý kód:
if kredity > 30:
print("Vydávám chlazenou Kolu.")
elif kredity >= 15
    print("Vydávám čistou vodu.")
else
    print("Máš příliš málo kreditů na jakýkoliv nápoj.")

# Bonusová chyba: Na konci by měl program vypsat, kolik kreditů zbývá.
# zbytky = kredity - 30
# print("Zůstatek: " + zbytky)
