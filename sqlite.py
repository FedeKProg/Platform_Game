import sqlite3

def crear_tabla():
		with sqlite3.connect("ranking_jueguito.db") as conexion:
			try:
				sentence = ''' create table players
								(
									id integer primary key autoincrement,
									nombre text,
									vidas integer,
									score integer,
									tiempo integer,
									lvl integer
								) 
							'''
							
				conexion.execute(sentence)
			except sqlite3.OperationalError:
				print("se creo la tablita")

def add_puntuacion(nombre,vidas,score, time,lvl):
		try:
			connect = sqlite3.connect("ranking_jueguito.db")
			cursor = connect.cursor()
			insert = """INSERT INTO players
			(nombre,vidas,score,tiempo,lvl) VALUES (?,?,?,?,?)"""

			cursor.execute(insert,(nombre,vidas,score,time,lvl))
			connect.commit()
			cursor.close()
			print(recibir_info())
		except sqlite3.OperationalError as error:
			print("Error ",error)

def recibir_info():
	with sqlite3.connect("ranking_jueguito.db") as conexion:
		select = "SELECT * FROM players ORDER BY score DESC LIMIT 5"
		cur = conexion.cursor()
		res = cur.execute(select)
		print("res",res.fetchall())
		return cur.execute(select).fetchall()


