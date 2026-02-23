# ==========================================================
# PROJEKT: ZABEZPEČENÍ BUNKRU 51
# Zadání: Dokonči bezpečnostní protokol podle instrukcí níže.
# ==========================================================

# --- 1. ČÁST: GRAFICKÉ ZÁHLAVÍ ---
# Použij proměnnou a násobení řetězců k vytvoření oddělovače
cara = "-" * 45

print(cara)
print("!!! VAROVÁNÍ: VSTUPUJETE DO ZAKÁZANÉ OBLASTI !!!")
print(cara)


# --- 2. ČÁST: IDENTIFIKACE ---
# ÚKOL: Získej od uživatele jméno a ulož ho do proměnné 'jmeno'
jmeno = input("IDENTIFIKUJTE SE (Zadejte jméno): ")


# --- 3. ČÁST: AUTORIZAČNÍ KÓD ---
# ÚKOL: Získej od uživatele kód. 
# V otázce (v inputu) vypiš jeho jméno VELKÝMI PÍSMENY (použij .upper())
# Příklad: "ZADEJTE PŘÍSTUPOVÝ KÓD, BILLY: "

kod = input("ZADEJTE PŘÍSTUPOVÝ KÓD, " + jmeno.upper() + ": ")


# --- 4. ČÁST: POTVRZENÍ PŘÍSTUPU ---
# ÚKOL: Vypiš závěrečný protokol.
# Musí obsahovat oddělovací čáru, potvrzení o ověřování a přivítání se jménem.

print(cara)
print("PROBÍHÁ OVĚŘOVÁNÍ KÓDU: " + kod)
print("PŘÍSTUP POVOLEN! Vítejte zpět, " + jmeno + ".")
print(cara)


# ==========================================================
# Pokračuj dál a přidej další funkce do protokolu:
# 1. Zeptej se uživatele na aktuální čas a vypiš ho v protokolu.
# 2. Na úplný konec přidej otázku: "Chcete aktivovat zámek? (ano/ne): "
#    a výsledek vypiš jako: "STATUS ZÁMKU: [odpověď]"
# ==========================================================
