import json
import codecs


with codecs.open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)


parsed = []

for row in data:
    for resource in row["resources"]:
        try:
            extras = resource["extras"]
        except KeyError:
            continue


        try:
            if extras["check:status"] >= 200 and extras["check:status"] < 300:
                continue
            extras['title'] = row['title']
            extras['slug'] = row['slug']
            extras['_id'] = row['_id']
            parsed.append(extras)
        except KeyError:
            continue


with codecs.open("brokenlinks.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False)
