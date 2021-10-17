# In a trello board, click "Menu" -> "More" -> "Print & Export" -> "Export as JSON"
# Replace the filename in this script with the name of your file and run.
# The json is read and converted to a more human-readable text form.
# Only list names and card names are printed, no other info is kept in the output from this script.

import json

with open('trello-export-p6zU8Myv.json') as thefile:
    t = thefile.read()
    j = json.loads(t)
    lists = {}
    for l in j['lists']:
        lists[l['id']] = l['name']
    
    print('found lists:')
    for list_id, name in lists.items():
        print(list_id, name)
    
    json_cards = j['cards']

    for l, list_name in lists.items():
        print()
        print("#############################")
        print("Starting with list: " + list_name)
        print("#############################")
        print()
        for c in json_cards:
            if c['idList'] == l:
                print(c['name'])
