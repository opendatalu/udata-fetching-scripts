
# Retrieve http links

1. Connect to the mongodb host.
2. Run this `mongo --quiet udata --eval 'printjson(db.dataset.find({"resources.url":/^http:/}, {slug:1, _id:1, title:1, "resources.url":1}).toArray())' > output_http.json`
3. Get the generated json in your workspace (`scp mongodb_host:output_http.json .`)
4. Edit the file to replace all regexes `[^\s]+\("(.+?)"\)` by `"$1"`. This will remove the unsupported by json ObjectID and ISODate objects by their values.
5. Make sure the script `scripts/filterhttp.py` is in the same place as the json, and run it `python filterhttp.py`. This will generate the `output_http_parsed.json`, which you can reformat with an IDE.


# Retrieve broken links

1. Connect to the mongodb host.
2. Run this `mongo --quiet udata --eval 'printjson(db.dataset.find({"resources.extras.check:available":false}, {slug:1, _id:1, title:1, "resources.extras":1}).toArray())' > output.json`
3. Get the generated json in your workspace (`scp mongodb_host:output.json .`)
4. Edit the file to replace all regexes `[^\s]+\("(.+?)"\)` by `"$1"`. This will remove the unsupported by json ObjectID and ISODate objects by their values.
5. Make sure the script `scripts/filterlinks.py` is in the same place as the json, and run it `python filterlinks.py`. This will generate the `brokenlinks.json`, which you can reformat with an IDE.
