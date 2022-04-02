import json
import random

nodesPos = json.loads("".join(open("nodePositions.json", encoding="UTF-8").readlines()))
all = json.loads("".join(open("allMax.json", encoding="UTF-8").readlines()))
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
        # nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":allMax[z]['img'], "x": nodesPos[z]['x'], "y": nodesPos[z]['y']})
        nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":allMax[z]['img']})
    else:
        if z in allEn:
            nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":'camera.jpg'})
            # nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":'camera.jpg', "x": nodesPos[z]['x'], "y": nodesPos[z]['y']})
        else:
            nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":'camera.jpg'})
            # nodes.append({'id': z, 'shape': 'circularImage','label':z, "image":'camera.jpg', "x": nodesPos[z]['x'], "y": nodesPos[z]['y']})

t = {'nodes':nodes,"edges":r}

print(json.dumps(r, ensure_ascii=False))
