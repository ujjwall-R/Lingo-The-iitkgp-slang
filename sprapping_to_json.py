from re import S
import requests
from bs4 import BeautifulSoup
import json

f=open('output.json','w')
url="https://wiki.metakgp.org/w/Lingo_of_IIT_Kharagpur"
r=requests.get(url)
r=r.content
r=BeautifulSoup(r, 'html.parser')

all_words_dict={}
all_words_list=[]
for i in r.find_all("ul"):
    string_=str(i.text)
    if string_[0]!="\n":
        print(string_.split()[0])
        all_words_dict[string_.split()[0]]=str(i.text)
    
all_words_list.append(all_words_dict)

f.write(json.dumps(all_words_dict ,indent=2))
f.close()