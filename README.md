
# Retrieve http links

Chrome blocks the downloads of some resources. These resources are external and their URL is in HTTP and not HTTPS. More details about the change in Chrome here: https://blog.chromium.org/2020/02/protecting-users-from-insecure.html

This happens only for resources which should be downloaded by the browser (if the resource is a web page, e.g. for a documentation, the problem does not happen)
The idea is to find all resources with an external URL in HTTP. 

1. Connect to the mongodb host.
2. Run this `mongo --quiet udata --eval 'printjson(db.dataset.find({"resources.url":/^http:/}, {slug:1, _id:1, title:1, "resources.url":1}).toArray())' > output_http.json`
3. Get the generated json in your workspace (`scp mongodb_host:output_http.json .`)
4. Edit the file to replace all regexes `[^\s]+\("(.+?)"\)` by `"$1"`. This will remove the unsupported by json ObjectID and ISODate objects by their values.
5. Make sure the script `scripts/filterhttp.py` is in the same place as the json, and run it `python filterhttp.py`. This will generate the `output_http_parsed.json`, which you can reformat with an IDE.

When the list is available, it can be filtered thanks to some heuristics:
- remove all private datasets
- all rest webservices can be removed (it is very rare to force the download on such a webservice)
- check URLs by extension: all xml, pdf files and all webpages rarely force download, they are displayed in the browser, and it is not an issue for Chrome.

# Retrieve broken links

These broken links are based on Croquemort. Some false positives are possible (some websites block bots), and some false negative too, for example when an old url on a website is redirected to the homepage without 404.

1. Connect to the mongodb host.
2. Run this `mongo --quiet udata --eval 'printjson(db.dataset.find({"resources.extras.check:available":false}, {slug:1, _id:1, title:1, "resources.extras":1}).toArray())' > output.json`
3. Get the generated json in your workspace (`scp mongodb_host:output.json .`)
4. Edit the file to replace all regexes `[^\s]+\("(.+?)"\)` by `"$1"`. This will remove the unsupported by json ObjectID and ISODate objects by their values.
5. Make sure the script `scripts/filterlinks.py` is in the same place as the json, and run it `python filterlinks.py`. This will generate the `brokenlinks.json`, which you can reformat with an IDE.

Don't forget to remove from the list all private datasets.

