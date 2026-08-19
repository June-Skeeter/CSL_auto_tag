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
ix = 0
for rec in data:
    if 'issued' in rec.keys():
        name =  rec['title'].lower().split(' ')
        name = [n for n in name if len(n)>3]
        j = 0
        rec['id'] = f"{rec['author'][0]['family'].lower()}_{name[0]}_{rec['issued']['date-parts'][0][0]}_{chr(97+j)}"
        while rec['id'] in existing:
            j += 1
            rec['id'] = f"{rec['author'][0]['family'].lower()}_{name[0]}_{rec['issued']['date-parts'][0][0]}_{chr(97+j)}"
        existing[rec['id']] = ix
        document.append(rec)
        ix += 1

with open(outputName, 'w', encoding='utf-8') as f:
    json.dump(document, f, indent=4, ensure_ascii=False)