import json
import argparse
CLI=argparse.ArgumentParser()

cslFile = 'TestCSL.json'
CLI.add_argument(f"--cslFile",nargs="?",type=str,default=cslFile)
known, unknown = CLI.parse_known_args()
cslFile = known.cslFile
outputName = cslFile.split('.json')[0]+'_autofmt.json'

Me = {'family':'Skeeter','given':'June'}

with open(cslFile, 'r', encoding='utf-8') as f:
    data = json.load(f)

document = []
existing = {}

sorted = []
for ix,rec in enumerate(data):
    name = rec['author'][0]['family'].lower()
    kw = [n for n in rec['title'].lower().split(' ') if len(n)>3]
    kw1 = kw[0]
    kw2 = kw[1]
    year = rec['issued']['date-parts'][0][0]
    id = f"{rec['author'][0]['family'].lower()}_{kw1}_{kw2}_{year}"
    sorted.append([name,year,kw1,kw2,id,ix])
sorted.sort()
for ox in sorted:
    ix = ox[-1]
    rec = data[ix]
    j = 0
    id = f"{ox[-2]}_{chr(97+j)}"
    while id in existing:
        j += 1
        id = f"{ox[-2]}_{chr(97+j)}"
    existing[id] = ix
    document.append(rec)

with open(outputName, 'w', encoding='utf-8') as f:
    json.dump(document, f, indent=4, ensure_ascii=False)