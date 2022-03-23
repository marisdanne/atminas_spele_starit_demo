import sqlite3
import json

JSON = 'static/cits/rezultati.json'

DB = sqlite3.connect('top.db')
SQL = DB.cursor()

SQL.execute("""CREATE TABLE IF NOT EXISTS rezultati ( 
              id INTEGER NOT NULL UNIQUE,
              vards TEXT,
              vecums INTEGER,
              laiks INTEGER,
              klikski INTEGER,
              datums TEXT,
              piezimes TEXT,
              skola TEXT,
              PRIMARY KEY("id" AUTOINCREMENT)
           )""")

with open(JSON, 'r', encoding="UTF-8") as f:
  dati = f.read()
  datiJson = json.loads(dati)

  for dati in datiJson:
    SQL.execute("INSERT INTO rezultati (vards, vecums, laiks, klikski, datums, piezimes, skola) VALUES (:vards, :vecums, :laiks, :klikski, :datums, :piezimes, :skola)", {'vards': dati['vards'], 'vecums': dati['vecums'], 'laiks':dati['laiks'], 'klikski':dati['klikski'], 'datums':dati['datums'], 'piezimes':dati['piezimes'], 'skola':dati['skola']})


DB.commit()

SQL.execute("SELECT * FROM rezultati")

print(SQL.fetchall())
    