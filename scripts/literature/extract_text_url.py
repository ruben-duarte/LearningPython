import urllib.request
from bs4 import BeautifulSoup

# here we have to pass url and path
# (where you want to save your text file)
urllib.request.urlretrieve("https://www.cervantesvirtual.com/obra-visor/maria--1/html/feddb01c-82b1-11df-acc7-002185ce6064_2.html#I_2_", "./text_file.txt")
 
file = open("text_file.txt", "r", encoding="utf8")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
 
f = open("test1.txt", "w")
 
# traverse paragraphs from soup
for data in soup.find_all("p"):
    sum = data.get_text()
    f.writelines(sum)
 
f.close()