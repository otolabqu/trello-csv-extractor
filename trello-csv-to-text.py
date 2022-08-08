# In a trello board, click "Menu" -> "More" -> "Print & Export" -> "Export as JSON"
# Replace the filename in this script with the name of your file and run.
# The json is read and converted to a more human-readable text form.
# Only list names and card names are printed, no other info is kept in the output from this script.

import json

with open('XPfA74Iz.json') as thefile:
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
                name_raw = c['name']
                # We want to keep the text on one line, not using the carriage return characters that Trello produces.
                # Otherwise long card names with line breaks will be broken after sorting the text file.
                # It might still be useful to be able to see where the line break was, so let's replace it.
                name_mod = name_raw.replace('\r', '_r_')
                print(name_mod)
