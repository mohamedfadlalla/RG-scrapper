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

df = pd.DataFrame()


row = {}
filter = {'type': 'journal-article'}
queries = {#'query.title': 'Molecular Docking', 
           'query.affiliation': 'University of Khartoum'}
for p in iterate_publications_as_json(max_results=10, filter=filter, queries=queries):

  # print(p)
  row['doi'] = p['DOI']
  row['author'] = p['author']
  row['title'] = p['title']
  ## OPTIMAIZATION NEEDED
  df = df.append(row, ignore_index=True)

dois = df.doi.tolist()

emails = API.Collect_Email(dois)

df['emails'] = emails
df.to_csv('scrapped_emails.csv')

