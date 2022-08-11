import json
import codecs


with codecs.open("output_http.json", "r", encoding="utf-8") as f:
    data = json.load(f)


parsed = []

for row in data:
    dataset = {
        "id": row["_id"],
        "title": row['title'],
        "slug": row['slug'],
        "http_resources": [] 

    }
    links = []

    for resource in row["resources"]:
        try:
            url = resource["url"]
        except KeyError:
            continue
        if url[:5] == "http:":
            links.append(url)
        
    if len(links) > 0:
        dataset["http_resources"] = links
        parsed.append(dataset)


with codecs.open("output_http_parsed.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False)
