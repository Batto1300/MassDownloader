import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.dmmm.uniroma1.it/~romano.scozzafava/testiesame/")
soup = BeautifulSoup(html, 'html.parser')
#soup.prettify()
urls=[]
names=[]
for link in soup.find_all('a'):
    urls.append("http://www.dmmm.uniroma1.it/~romano.scozzafava/testiesame/" + link.get('href'))
urls = urls[5:urls.__len__()]   # cleaning urls
print(urls)
directory= 'C:/Users/Batto1300/Desktop/Compiti'
pattern = '(?<=testiesame/).+pdf'   # using regex makes me feel so smart
for url in urls:    # finding compiti's name
    names.append(re.findall(pattern, url))
for link, name in zip(urls, names):
    pat = os.path.join(directory, name[0])  # paths cannot be concatenated like strings
    file = open(pat, "wb")  # wb is for byte-like objects like pdf
    file.write(requests.get(link).content)  # requesting the url and getting the content which is a byte object
    file.close()
print("DONE")