import json
import random

all = json.loads("".join(open("all-mangas-parsed.json", encoding="UTF-8").readlines()))
allEn = json.loads("".join(open("all.json", encoding="UTF-8").readlines()))
allMax = json.loads("".join(open("allMax.json", encoding="UTF-8").readlines()))
r = []
a = []
i = 0
for k in all:
    if k not in a:
        a.append(k)
    for j in all[k]['similar']:
        if j not in a:
            a.append(j)
        r.append({'from': k, 'to': j})

nodes = []
for z in a:
    if z in allMax:
        nodes.append({'id': z, 'fill': {'src': allMax[z]['img']}, "url":"mangalib.me/"+allMax[z]['name']})
    else:
        if z in allEn:
            nodes.append({'id': z, 'url':"mangalib.me/"+allEn[z]})
        else:
            nodes.append({'id': z, 'url': "mangalib.me/"})

t = {'nodes':nodes,"edges":r}

print(json.dumps(t, ensure_ascii=False))
