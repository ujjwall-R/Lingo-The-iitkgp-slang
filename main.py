import json
from difflib import get_close_matches

f=open('output.json')
data= json.load(f)

def linear_search(word_):
    for item in data:
        if item.casefold()==word_.casefold():
            print(data[item])
            return 1
    return 0

word__=input("Enter Lingo: ")
if linear_search(word__)==0:
    print("Lingo not found!")
    simialar_words_list=get_close_matches(word__,data)
    if len(simialar_words_list)>0:
        para=1
        print("Did you mean?")
        for i in simialar_words_list:
            print(f"{para}.{i}   ", end=" ")
            para=para+1
        choice=input("\nPress N if No or enter choice number, (default is N) : ")
        if choice!='N' and choice!='n' and choice!='':
            choice=int(choice)-1
            linear_search(simialar_words_list[choice])

f.close()
