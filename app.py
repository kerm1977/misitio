from controller import *
from view import *


# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
if __name__ == "__main__":

	db.create_all()
	# db.upgrade_all()
	# db.drop_all()	#Solo se ejecuta para migrar nuevos campos a la db pero borra el contenido
	app.run(debug = True, port=3000) 



# Migraciones Cmder
	# set FLASK_APP=main.py 	<--Crea un directorio de migraciones
	# flask db init 			
	# $ flask db stamp head
	# $ flask db migrate
	# $ flask db migrate -m "mensaje x"
	# $ flask db upgrade

	# ----------------------------------------------
	# SI HAY ERRORES DE BASE DE DATOS CON alembic 
	# ---------------------------------------------- 
	# Can't locate revision identified by 'y la versiónxxx'

	# 	1.ingresar por medio de heidisql y borrar la tabla creada alembic_version
	# 	2.borrar la carpeta migraciones dentro del proyecto-Cmder
	#   3.Volver a setear Flask, inicializarlo, migrarlo etc.. osea pasos de arriba
	# 	4.Migrar <-- Agrega a la db y luego upgrade <-- guarda el cambio
	# PYTHONANYWHERE
	# LaTribuHiking
	# latribu1977
	# drop database LaTribuHiking$db
	
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------