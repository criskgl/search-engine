import psycopg2
import os
import csv
from bs4 import BeautifulSoup
from bs4 import Comment
import nltk
nltk.download('punkt')


directory = '/home/kublai/Desktop/UC3M/rai/practica2-vectorial-metricas/docsAllInOne/'

conn = psycopg2.connect("postgres://xathfpjtdrhfhm:b98247bf3cd6168c3b2a6cbeb757bd063d467dd5b6f5654637a484affc57c2aa@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/dd0l074vj489qf") 
cur = conn.cursor()

cur.execute("delete from corpus")
conn.commit()

cur.execute("select * from corpus;")
corpus = cur.fetchall() 
print("Successfully retrieved ", len(corpus), " documents from database.")

with open('htmls.csv', 'w') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["id", "name", "data"])
    
    for idx, filename in enumerate(os.listdir(directory)):
        print(idx)
        f = open('/home/kublai/Desktop/UC3M/rai/practica2-vectorial-metricas/docsAllInOne/'+filename)
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]
        [script.extract() for script in soup('script')]
        [style.extract() for style in soup('style')]
        tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(soup.getText())#['Sewer', 'Global', 'Buyers', 'importers']
        contentClean = ' '.join(tokens).encode('utf-8').strip()#'Sewer Global Buyers importers'
        writer.writerow([str(idx), filename, contentClean])
        continue
 


    
  