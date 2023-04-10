import csv, random

with open("./data/finalSet.tsv", "r") as file:
    data = []
    for row in csv.reader(file, delimiter="\t"):
        if row[6] != 'NA': data.append(row)
    data = data[1:]

macroAreas = set([lang[6] for lang in data])
splitByMacroArea: dict = {}
for level in macroAreas:
    splitByMacroArea[level] = [lang for lang in data if lang[6] == level]

finalChoice={}
for area in splitByMacroArea:
    finalChoice[area] = []
    for _ in range(5):
        while len(finalChoice[area]) < 5:
            c = random.choice(splitByMacroArea[area])
            doAdd = True
            for lang in finalChoice[area]:
                if lang[5] == c[5]:
                    doAdd = False
                    continue
            if doAdd:
                finalChoice[area].append(c)

for area in finalChoice:
   print(f"Area: {area}")
   for lang in finalChoice[area]:
       print(f"{lang[0]} | {lang[1]} | {lang[2]} | {lang[3]} | {lang[5]}") 