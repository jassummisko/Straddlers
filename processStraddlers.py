import pandas as pd, dataclasses

from sqlalchemy import false

BOOL_TAB = {
    "+": True,
    "-": False,
}

@dataclasses.dataclass
class Entry:
    language: str
    segment: str
    patternsSon: bool
    patternsObs: bool
    otherInfo: dict

data = pd.read_excel('data/thesisnotes.xlsx')

entries = []
for row in data.itertuples():
    lang = row[1]
    segment = row[4]
    patternsSon = BOOL_TAB.get(row[16], row[16])
    patternsObs = BOOL_TAB.get(row[17], row[17])
    extraInfo = {}
    for x in range(5, 16): extraInfo[data.columns[x]] = BOOL_TAB.get(row[x], row[x])

    entries.append(Entry(lang, segment, patternsSon, patternsObs, extraInfo))

with open("data/Sorted Languages.md","r") as file:
    allLines = file.readlines()

import itertools
segmentBuff = [line.split("|")[4] for line in allLines if len(line.split("|")) > 3]
segmentBuff = [seg.split() for seg in segmentBuff]
finalSeg = list(itertools.chain(*segmentBuff))
print(len(finalSeg))
    
#td = {}
#for entry in entries:
    #if entry.segment not in td:
        #td[entry.segment] = 0
    #if entry.patternsSon == True and entry.patternsObs == True:
        #td[entry.segment] += 1

#td = {k:v for (k,v) in td.items() if v > 0}
