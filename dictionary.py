import json 
from difflib import get_close_matches
#load JSON data
data = json.load(open('data.json'))

search = input('Enter word to search:')

def getMeaning(w):
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print('Did you mean %s instead? Enter Y if yes or N if no:' % close_match)
        choice= input()
        choice =choice.lower()
        if choice =='y':
            return data[close_match]
        elif choice == 'n':
            return 'The word doesn\'t exists'
        else:
            return 'Wrong choice'
    else:
        return 'The word doesn\'t exists' 
result = getMeaning(search)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)