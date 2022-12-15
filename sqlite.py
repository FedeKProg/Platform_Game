import sqlite3

def crear_table():
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
				print("table")
			except sqlite3.OperationalError:
				print("se creo la tablita")

def add_puntuacion(nombre,vidas,score, time,lvl):
		try:
			sqlConnect = sqlite3.connect("ranking_jueguito.db")
			cursor = sqlConnect.cursor()
			sql_insert_query = """INSERT INTO players
			(nombre,vidas,score,tiempo,lvl) VALUES (?,?,?,?,?)"""

			cursor.execute(sql_insert_query,(nombre,vidas,score,time,lvl))
			sqlConnect.commit()
			cursor.close()
			print(recibir_info())
		except sqlite3.OperationalError as error:
			print("Error ",error)

def recibir_info():
	with sqlite3.connect("ranking_jueguito.db") as conexion:
		sql_select = "SELECT * FROM players ORDER BY score DESC LIMIT 5"
		cur = conexion.cursor()
		res = cur.execute(sql_select)
		print("res",res.fetchall())
		return cur.execute(sql_select).fetchall()


