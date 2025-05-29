# A függvény készít egy sort a diagrammhoz, ahol a nap számát és a hőmérsékletet csillagokkal jelöli. 
def keszit_diagram_sort(nap_szama, homerseklet):
    # Egész számra alakít
    csillagok_szama = int(homerseklet)
    # Annyi csillagot generál amennyi az aktuális hőmérséklet.
    csillagok = '*' * csillagok_szama
    # A nap csillagok és hőmérséklet számát tartalmazó sor.
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    # Returnöli a sort
    return sor

# A függvény kirajzolja a diagrammot
def rajzolj_diagram(homersekletek):
    # Üdvözlő üzenet
    print("Napi átlaghőmérséklet diagram (°C)")
    # Elválasztó vonal
    print("-" * 40)
    
    # For ciklussal végigiterálunk a hőmérséklet listán
    for i in range(len(homersekletek)):
        # Napok számozása 1-től indul
        nap = i + 1 
        # Meghívja az első függvényt
        sor = keszit_diagram_sort(nap, homersekletek[i])
        # Kiírja az elkészült sort
        print(sor)


# A napi átlaghőmérsékletek listája
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# Meghívjuk a rajzolj_diagram függvényt
rajzolj_diagram(napi_atlaghomersekletek)


