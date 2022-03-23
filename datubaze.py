import sqlite3

def savienot():
  DB = sqlite3.connect('top.db')
  return DB.cursor()
  

def top():
  SQL = savienot()
  SQL.execute("SELECT * FROM rezultati")
  rezultati = SQL.fetchall()
  dati = []
  for rez in rezultati:
    dati.append({
      "id":rez[0],
      "vards":rez[1],
      "vecums":rez[2],
      "laiks":rez[3],
      "klikski":rez[4],
      "datums":rez[5],
      "piezimes":rez[6],
      "skola":rez[7]
    })

  # print(dati)
  return dati

def pievienot(dati):
  SQL = savienot()
  SQL.execute("INSERT INTO rezultati (vards, vecums, laiks, klikski, datums, piezimes, skola) VALUES (:vards, :vecums, :laiks, :klikski, :datums, :piezimes, :skola)", {'vards': dati['vards'], 'vecums': dati['vecums'], 'laiks':dati['laiks'], 'klikski':dati['klikski'], 'datums':dati['datums'], 'piezimes':dati['piezimes'], 'skola':dati['skola']})