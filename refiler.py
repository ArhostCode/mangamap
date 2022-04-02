import json
t = {}
r = 1
while r < 1800:
    s = open(f"{r}-{r+59}.json", encoding="UTF-8")
    data = json.loads("".join(s.readlines()))
    r+=60
    for k in data['items']['data']:
        t[k['rus_name']] = k['slug']
k = open("all.json", "w", encoding="UTF-8")
k.write(json.dumps(t,ensure_ascii=False))