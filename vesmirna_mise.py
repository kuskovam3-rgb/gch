# ==========================================================
# ÚKOL: UNIVERZÁLNÍ VESMÍRNÝ PLÁNOVAČ
# Cíl: Vytvořit program, který vypočítá cestu kamkoliv.
# ==========================================================

print("--- KONFIGURACE VESMÍRNÉ MISE ---")

# 1. ČÁST: VSTUPY OD UŽIVATELE
# ÚKOL: Získej všechna data pomocí input() a převeď je na int().

palivo_v_nadrzi = int(input("Kolik litrů paliva máš v nádrži? "))
vzdalenost_cile = int(input("Jak daleko je tvůj cíl (v km)? "))
spotreba_rakety = int(input("Kolik litrů tvoje raketa spotřebuje na 1 km? "))

# 2. ČÁST: VÝPOČTY
# Výpočet celkové spotřeby: vzdálenost * spotřeba
celkova_spotreba = vzdalenost_cile * spotreba_rakety

# Výpočet zbytku: nádrž - celková spotřeba
zbytek_v_nadrzi = palivo_v_nadrzi - celkova_spotreba

# 3. ČÁST: VÝSLEDKY (VÝPIS)
print("-" * 30)
print("VÝSLEDKY PLÁNOVÁNÍ:")
print("Celkem spotřebuješ: " + str(celkova_spotreba) + " litrů.")
print("V nádrži ti po příletu zůstane: " + str(zbytek_v_nadrzi) + " litrů.")
