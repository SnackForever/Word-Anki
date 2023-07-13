upimport csv

wordDict = {}

with open("./word.csv", 'r', encoding='utf-8') as file_csv:
    csvreader = csv.reader(file_csv, delimiter=",")

    for ligne in csvreader:
        print(ligne)
        cle = ligne[0].strip()
        valeur = ligne[1].strip()

        if cle[0].islower():
            cle = cle[0].upper() + cle[1:]

        if valeur[0].islower():
            valeur = valeur[0].upper() + valeur[1:]

        wordDict[cle] = valeur

myKeys = sorted(wordDict.keys())
wordDict = {i: wordDict[i] for i in myKeys}

with open("./WordUpdated.csv", 'w', newline='', encoding='utf-8') as file_csv:
    csvwriter = csv.writer(file_csv)
    for cle, valeur in wordDict.items():
        csvwriter.writerow([cle, valeur])
