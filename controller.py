from flask import request, make_response, redirect, render_template, url_for, flash, Flask, abort, g
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SelectField, TimeField, SubmitField, BooleanField, HiddenField, EmailField, IntegerField, validators
from wtforms.validators import DataRequired, Length, Email,  EqualTo, ValidationError
from wtforms.widgets import TextArea
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from flask_ckeditor import CKEditor, CKEditorField #Editor enriquecido con instancia ckeditor = CKEditor(app)
from wtforms import validators
from time import sleep
from flask import Blueprint
from datetime import datetime, timedelta
from pytz import timezone
from flask import json
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename #trabaja con imagenes para subirlas a la DB

import uuid as uuid #trabaja con imagenes para subirlas a la DB
import os #trabaja con imagenes para subirlas a la DB
import pymysql.cursors
# from mysql.connector import
# print(now_time.strftime('%I:%M:%S %p'))
# pip uninstall -y -r  fichero





##########################################################################
##########################################################################
##########################################################################
app = Flask(__name__)
#Editor enriquecido
ckeditor = CKEditor(app)

# app.permanent_session_lifetime = timedelta(minutes=1)






#########################################################################
##########################################################################
##########################################################################
# SQLITE3 DB

import os
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/db.db" #CONECTOR - RUTA ABSOLUTA

#SOLO PARA USO LOCAL
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
host = "localhost",
user = "latribu",
password = "root",
database = "root"

##########################################################################
#DB MYSQL LOCAL
				 						 #-U    -P       -UBICACION     -NOMBRE DB
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/db"

#DB MYSQL PYTHONANYWHERE INSTALAR
#pip uninstall mysql-connector-python-8.0.6
#pip install mysql-connector-python
# pip3  install mysql-connector-python
# pip3  install mysql-connector	

#PARA USO REMOTO	
											                 #-U          -P                      -UBICACION                          -NOMBRE DB
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://LaTribuHiking:latribu1977@LaTribuHiking.mysql.pythonanywhere-services.com/LaTribuHiking$db"

#########################################################################
##########################################################################
##########################################################################






# OTRA CONFIGURACIÓN
db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app,db,render_as_batch=True)

#########################################################################
##########################################################################
##########################################################################
# CLAVE SECRETA
bcrypt 	= Bcrypt(app)
pw_hash = bcrypt.generate_password_hash("SECRET_KEY")
bcrypt.check_password_hash(pw_hash, "SECRET_KEY")
app.config['SECRET_KEY'] = pw_hash
# print(f"La Clave secreta es {pw_hash}")
# -----------------------






#########################################################################
##########################################################################
##########################################################################
# MANEJO DE SESIONES
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" # 
login_manager.login_message = u"Primero necesitas iniciar sesión"
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))






#########################################################################
##########################################################################
##########################################################################
#FECHA ------------------
#Permite pasar al idioma local las fechas y alertas

import locale
locale.setlocale(locale.LC_ALL, 'es_ES')
# -----------------------
@app.add_template_filter
def fecha(date):		
						
						# %a %H:%M %d/%m/%y <-- mié. 21:21 07/02/24
						# %H:%M:%S 
						# %A, %d. %B %Y %I:%M%p <-- miércoles, 07. febrero 2024 09:22p. m.
						# %d-%m-%Y  - formato de raya 
						# %d/%m/%Y  / formato de slash
	return date.strftime("%A, %d de %B %Y ")
# -----------------------





##########################################################################
##########################################################################
##########################################################################
# EJECUTA LA APLICACION
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