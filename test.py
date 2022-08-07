#test and calculate preformance

##third party
import selenium_setup
from bs4 import BeautifulSoup as bs
from crossref_commons.iteration import iterate_publications_as_json
import pandas as pd

##built in
import sqlite3
from datetime import datetime

##local
import extraction as ex
import db.setup as db
from db.insert import InsertError
import API 


filter = {'type': 'journal-article'}
queries = {#'query.title': 'Molecular Docking', 
           'query.affiliation': 'University of Khartoum'}

Data =[]

for p in iterate_publications_as_json(max_results=100, filter=filter, queries=queries):
  Data.append([p['DOI'], p['author'][0], p['title'][0]])

df = pd.DataFrame(Data, columns=['DOI', 'Authors', 'Title'])


dois = df.doi.tolist()

emails = API.Collect_Email(dois)

df['emails'] = emails
df.to_csv('scrapped_emails.csv')

