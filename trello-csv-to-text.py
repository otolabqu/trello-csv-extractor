# In a trello board, click "Menu" -> "More" -> "Print & Export" -> "Export as JSON"
# Replace the filename in this script with the name of your file and run.
# The json is read and converted to a more human-readable text form.
# Only list names and card names are printed, no other info is kept in the output from this script.

import json

with open('XPfA74Iz.json') as thefile:
    j = json.loads(thefile.read())
    out_lists = {}
    for in_list in j['lists']:
        out_lists[in_list['id']] = in_list['name']
    
    print('found lists:')
    for list_id, name in out_lists.items():
        print(list_id, name)
    
    json_cards = j['cards']

    for list_id, list_name in out_lists.items():
        print()
        print("#############################")
        print("Starting with list: " + list_name)
        print("#############################")
        print()
        current_list = []
        for c in json_cards:
            if c['idList'] == list_id:
                name_raw = c['name']
                desc = c['desc']
                if desc is not None and 'http' in desc:
                    name_raw = desc + " " + name_raw
                # We want to keep the text on one line, not using the carriage return characters that Trello produces.
                # Otherwise long card names with line breaks will be broken after sorting the text file.
                # It might still be useful to be able to see where the line break was, so let's replace it.
                name_mod = name_raw.replace('\r', '_r_')
                current_list.append(name_mod)
        current_list.sort()
        for x in current_list:
            print(x)
