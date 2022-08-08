import requests
import re

from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup as bs


def to_str(l):
    s = ''
    for i in l:
        s =s+i+' '
    return s

def download_paper(doi, name):
    #download papers form scihub using doi
    url = f'https://sci-hub.se/{doi}'
    print(url)
    response = requests.get(url)
    soup = bs(response.content)
    url =  soup.find('div', id= 'buttons').button['onclick'].split("'")[1].replace('//','')
    print('before editing', url)
    if url.startswith('zero.sci-hub.se') or url.startswith('twin.sci-hub.se'):
      url = 'http://' + url
      response = requests.get(url)
      open(name, "wb").write(response.content)
    else:
      url = 'https://sci-hub.se/' + url
      print('after editing: ',url)
      response = requests.get(url)
      open(name, "wb").write(response.content)


    
    
def get_email(file):
    #extract emails from pdfs
    pattren = '\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b'
    reader = PdfFileReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    match = re.findall(pattren,text)
    print(match)
    return match

def ishundred(num):
  if num%100 == 0:
    return True
