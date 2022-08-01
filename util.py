

def to_str(l):
    s = ''
    for i in l:
        s =s+i+' '
    return s

def download_paper(doi, name):
    #download papers form scihub using doi
    name = name + '.pdf'
    url = f'https://sci-hub.se/{doi}'
    response = requests.get(url)
    soup = bs(response.content)
    url = 'http:' + soup.find('div', id= 'buttons').button['onclick'].split("'")[1]
    response = requests.get(url)
    open(name, "wb").write(response.content)
