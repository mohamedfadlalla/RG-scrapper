#test and calculate preformance

##third party
from bs4 import BeautifulSoup as bs
from crossref_commons.iteration import iterate_publications_as_json
import pandas as pd

##built in


##local
import API 


filter = {'type': 'journal-article'}
queries = {#'query.title': 'Molecular Docking', 
           'query.affiliation': 'University of Khartoum'}

Data =[]

for p in iterate_publications_as_json(max_results=10, filter=filter, queries=queries):
  Data.append([p['DOI'], p['author'][0], p['title'][0]])


df = pd.DataFrame(Data, columns=['DOI', 'Authors', 'Title'])
df['Email'] = None

# df = pd.read_csv('/content/scrapped_emails.csv')
# df['Email'] = None
# API.Collect_Email(df)


df.to_csv('scrapped_emails.csv', index=False)

