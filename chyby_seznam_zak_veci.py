# Seznam zakázaných věcí
zakazane = ["nůž", "jed", "výbušnina"]

# Spuštění kontroly
bezi_kontrola = "ano"

while bezi_kontrola = "ano":
predmet = input("Co neseš v tašce? ").lower
    
    if predmet in zakazane
        print(f"ALARM! {predmet} je zakázaný!")
    else:
        print("V pořádku, můžeš jít.")
    
    bezi_kontrola = input("Chcete kontrolovat dál? (ano/ne)")

print("Rentgen vypnut.")
