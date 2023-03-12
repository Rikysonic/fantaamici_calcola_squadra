import itertools

professori = {
    "Cuccarini": 180,  # 170
    "Celentano": 130,
    "Todaro": 180,  # 180
    # "Peparini": 100,
    "Arisa": 130,
    "Zerbi": 160,
    # "Pettinelli": 110
    "Emanuel Lo": 120
}

allievi = {
    # "Sissi": 250,
    # "Calma": 120,
    # "Serena": 180,
    # "LDA": 230,
    # "Alex": 250,
    # "Luigi": 190,
    # "Gio Montana": 120,
    # "Aisha": 160,
    # "Crytical": 150,
    # "Albe": 190,
    # "Dario": 200,
    # "Carola": 170,
    # "John Erik": 220,
    # "Michele": 170,
    # "Christian": 180,
    # "Leonardo": 120,
    # "Nunzio": 120,
    # "Alice": 140
    "Alessio": 170,
    "Angelina": 220,
    "Aaron": 180,
    "Federica": 160,
    "Gianmarco": 150,
    "Cricca": 140,
    "Isobel": 190,
    "Maddalena": 150,
    "Mattia": 220,
    "Megan": 130,
    "NDG": 130,
    "PiccoloG": 160,
    "Ramon": 180,
    "Samu": 190,
    "Wax": 210
}

allievi_fissati = {}

budget = 1000


def calcola_combinazioni(fixed=None, combination_number=5):
    global professori, allievi, allievi_fissati
    if fixed is not None:
        if fixed['professore'] != "":
            professori = {
                fixed['professore']: professori[fixed['professore']]
            }
        if len(fixed['allievi']) != 0 and len(fixed['allievi']) <= 4:
            combination_number = combination_number - len(fixed['allievi'])
            for allievo in fixed['allievi']:
                allievi_fissati[allievo] = allievi[allievo]
                del allievi[allievo]
        else:
            print("Troppi allievi fissati")
            return
        calcola_combinazioni(None, combination_number)
    else:
        list_allievi = allievi.keys()
        lista_combinazioni = list(itertools.combinations(list_allievi, combination_number))
        squadre_valide = {}
        for prof in professori:
            budget_allievi = budget - professori[prof]
            for allievo in allievi_fissati:
                budget_allievi = budget_allievi - allievi_fissati[allievo]
            for squadra_allievi in lista_combinazioni:
                budget_temp = budget_allievi
                for allievo in squadra_allievi:
                    budget_temp = budget_temp - allievi[allievo]
                if budget_temp >= 0:
                    squadra_finale = [prof, *allievi_fissati.keys(), *squadra_allievi]
                    squadre_valide[', '.join(squadra_finale)] = budget - budget_temp
        print(f"Squadre possibili: {len(squadre_valide)}")
        for squadra in squadre_valide:
            print(f"{squadra} - Costo totale squadra: {squadre_valide[squadra]}")


if __name__ == '__main__':
    fixed = {
        "professore": "",
        "allievi": [
            "Mattia",
            "Angelina"
        ]
    }
    if fixed['professore'] != "" or len(fixed['allievi']) != 0:
        calcola_combinazioni(fixed)
    else:
        calcola_combinazioni()
