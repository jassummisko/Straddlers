# Combine familydata and offendingLanguages data
import csv, dataclasses

@dataclasses.dataclass
class FamilyDataEntry():
    name:   str
    code:   str
    family: str
    area:   str
    
def rowToFamilyDataEntry(row):
    return FamilyDataEntry(*row)

@dataclasses.dataclass
class FinalDataEntry():
    LanguageName:           str
    Glottocode:             str
    SpecificDialect:        str
    OffendingSegments:      str
    ReasonsForInclusion:    str
    LanguageFamily:         str
    Macroarea:              str

def makeFinalDataEntry(row, familyDataEntries):
    code = row[1]
    family = "NA"
    area = "NA"
    for entry in familyDataEntries:
        if entry.code == code:
            family = entry.family
            area = entry.area
    
    return FinalDataEntry(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        family,
        area
    )

def cleanRow(row):
    for idx, _ in enumerate(row):
        if (row[idx] == None) or row[idx] == "":
            row[idx] = "NA"
    return row

if __name__ == '__main__':
    with open("data/familydata.tsv") as f:
        familyData = [rowToFamilyDataEntry(cleanRow(row)) for row in csv.reader(f, delimiter="\t")][1:]

    with open("data/offendingLanguages.tsv") as f:
        offendingLanguages = [cleanRow(row) for row in csv.reader(f, delimiter="\t")][1:]
    
    finalSet = [makeFinalDataEntry(row, familyData) for row in offendingLanguages]

with open("data/finalSet.tsv", "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["Language Name", "Glottocode", "Specific Dialect", "Offending segments", "ReasonsForInclusion", "Language Family", "Macroarea"])
    for entry in finalSet:
        row = [
            entry.LanguageName,
            entry.Glottocode,
            entry.SpecificDialect,
            entry.OffendingSegments,
            entry.ReasonsForInclusion,
            entry.LanguageFamily,
            entry.Macroarea,
        ]
        writer.writerow(row)