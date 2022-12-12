import sqlite3


class Sqlite():
	def __init__(self):
		with sqlite3.connect("players data/players_score.db") as conexion:
			try:
				sentencia = ''' create  table jugadores
								(
										id integer primary key autoincrement,
										nombre text,
										vidas interger,
										puntos interger,
										tiempo interger
								)
							'''
				conexion.execute(sentencia)
				print("Se creo la tabla personajes")                       
			except sqlite3.OperationalError:
				print("La tabla personajes ya existe")  
	def agregar_score(self,nombre,vida,score,tiempo):
		with sqlite3.connect("players data/players_score.db") as conexion:
			if self.modificar_score(nombre) != []:
				try:
					conexion.execute("UPDATE jugadores SET vidas=?,puntos=?,tiempo=? WHERE nombre=?"),(vida,score,tiempo,nombre)
					conexion.commit()
				except sqlite3.OperationalError as error:
					print("ERROR: ", error)
			else: 
				try:
					conexion.execute("insert into jugadores(nombre,vidas,puntos,tiempo) values (?,?,?,?)",(nombre,vida,score,tiempo))
					conexion.commit
				except sqlite3.OperationalError as error:
					print("ERROR: ", error)

	def modificar_score(self,nombre):
		nombre = nombre
		with sqlite3.connect("players data/players_score.db") as conexion:
			sentencia = "SELECT * FROM jugadores WHERE nombre=?"
			cursor = conexion.execute(sentencia,(nombre,))
		return cursor.fetchall()

	def select(self):
		with sqlite3.connect("players data/players_score.db") as conexion:
			cursor = conexion.execute("SELECT * FROM jugadores")
			for fila in cursor:
				print(fila)


