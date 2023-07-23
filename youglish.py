from bs4 import BeautifulSoup
import requests

# HTML From url
# url = "https://youglish.com/lesson/word/23-07-2023/fcgifegeiei"
# result = requests.get(url).text
# doc = BeautifulSoup(result, "html.parser")

# HTML From File
with open("D:\Work\youglish_parser\index.html", "r",encoding="utf8") as f:
	doc = BeautifulSoup(f, "html.parser")

word = doc.find("span", {"id": "wod"}).string
definitions = doc.find("div", {"class":"w_id_def"}).ol.contents
synonymsUls = doc.find("div", {"class":"d_syno"}).find_all("ul")
 
print("WORD - ",word)

print("Definitions:")
for idx,definition in enumerate(definitions):
	print(idx+1,definition.string)

print("Synonyms:")
for ul in synonymsUls:
    for li in ul.contents:
        synonymsString = ""
        for a in li.contents:
            synonymsString += a.string
        print(synonymsString)
