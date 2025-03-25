#IMPORTS ----------------
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
# app.permanent_session_lifetime = timedelta(minutes=1)

#Editor enriquecido
ckeditor = CKEditor(app)

# SQLITE3 DB ------------
# -----------------------
# /::::::::::::::::::::/
# -----------------------
app = Flask(__name__)
#Editor enriquecido
ckeditor = CKEditor(app)

##########################################################################
##########################################################################
##########################################################################

# DB SQLITE
# import os
# dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/db.db" #CONECTOR - RUTA ABSOLUTA

# app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
# 	host = "LaTribuHiking.mysql.pythonanywhere-services.com",
# 	user = "LaTribuHiking",
# 	password = "latribu1977",
# 	database = "LaTribuHiking$db"


#DB MYSQL LOCAL
				 #-U  -P  -UBICACION -NOMBRE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/db"

											                   # -U          -P                 -UBICACION                             -NOMBRE DB
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://LaTribuHiking:CR129x7848n@LaTribuHiking.mysql.pythonanywhere-services.com/LaTribuHiking$db"
###########################################################################


# OTRA CONFIGURACIÓN
db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app,db,render_as_batch=True)

# CLAVE SECRETA
bcrypt 	= Bcrypt(app)
pw_hash = bcrypt.generate_password_hash("SECRET_KEY")
bcrypt.check_password_hash(pw_hash, "SECRET_KEY")
app.config['SECRET_KEY'] = pw_hash
# print(f"La Clave secreta es {pw_hash}")
# -----------------------

# MANEJO DE SESIONES ----
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" # 
login_manager.login_message = u"Primero necesitas iniciar sesión"
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
# MANEJO DE SESIONES ----

#FOLDER DE IMAGENES QUE FUNCIONA CON LO QUE SE SUBE A TRAVES DE FORMULARIOS DE SUBIDA.
# SI SE CAMBIA LA RUTA avatars TAMBIEN SE DEBE CAMBIAR EN LAS VISTAS HTML
UPLOAD_FOLDER ="static/avatars"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#FOLDER DE IMAGENES QUE FUNCIONA CON LO QUE SE SUBE A TRAVES DE FORMULARIOS DE SUBIDA.
# SI SE CAMBIA LA RUTA avatars TAMBIEN SE DEBE CAMBIAR EN LAS VISTAS HTML
UPLOAD_FOLDER_IMG ="static/img"
app.config['UPLOAD_FOLDER_IMG'] = UPLOAD_FOLDER_IMG



#FOLDER DE IMAGENES QUE FUNCIONA CON LO QUE SE SUBE A TRAVES DE FORMULARIOS DE SUBIDA.
# SI SE CAMBIA LA RUTA avatars TAMBIEN SE DEBE CAMBIAR EN LAS VISTAS HTML
# UPLOAD_FOLDER_POST ="static/ImgPost"
# app.config['UPLOAD_FOLDER_POST'] = UPLOAD_FOLDER_POST


##########################################################################
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

#TABLAS -----------------
# -----------------------
# /::::::::::::::::::::/
# -----------------------

class User(db.Model, UserMixin):
	#Al agregar un campo hay que migrarlo a la DB y aquí se crean los campos del usuario
	id 					=	db.Column(db.Integer, 		primary_key=True)
	username 			= 	db.Column(db.String(20),	unique=False, 	nullable=False)
	apellido 			= 	db.Column(db.String(20),	unique=False,	nullable=True)
	apellido2 			= 	db.Column(db.String(20),	unique=False,	nullable=True)
	residencia 			= 	db.Column(db.String(120),	unique=False,	nullable=True)
	email 				= 	db.Column(db.String(120),	unique=True, 	nullable=False)
	telefono			= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	telefonoE			= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	celular				= 	db.Column(db.String(15),	unique=False, 	nullable=True)
	password 			= 	db.Column(db.String(60),	unique=False, 	nullable=False)
	confirmpassword		= 	db.Column(db.String(60),	unique=False, 	nullable=False)
	alergias			= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	tiposangre 			= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	cronico				= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	medicamentos		= 	db.Column(db.String(100),	unique=False, 	nullable=True)
	nacimiento			= 	db.Column(db.String(20),	unique=False, 	nullable=True)
	avatar				= 	db.Column(db.Text,			nullable=False, default="default.png")
	date_added			= 	db.Column(db.DateTime,		nullable=False,	default=datetime.utcnow)
	# El usuario puede tener muchos posts y "Posts" es el nombre de la clase a la que se va a referenica
	posts_ref 			= 	db.relationship("Posts", 	backref="user")

	#Al agregar un campo hay que migrarlo a la DB y también agregarlo en esta fila con la misma sintaxis y orden
	def __repr__(self):
		return f"User('{self.username}',{self.apellido}',{self.apellido2}','{self.residencia}','{self.email}','{self.telefono}','{self.celular}','{self.password}','{self.confirmpassword}','{self.alergias}','{self.cronico}','{self.nacimiento}','{self.medicamentos}','{self.avatar}')"

class Posts(db.Model):
	id 					=	db.Column(db.Integer, primary_key=True)
	titulo 				= 	db.Column(db.String(255))
	descripcion			=	db.Column(db.Text)
	content				=	db.Column(db.Text)
	kilometros			=	db.Column(db.Float)
	altura				=	db.Column(db.Float)
	lugar				=	db.Column(db.Text)
	finaliza			=	db.Column(db.Text)
	etapa				=	db.Column(db.Integer)
	capacidad			=	db.Column(db.Integer)
	hora				=	db.Column(db.Integer)
	salida				=	db.Column(db.Text)
	dificultad			=	db.Column(db.Text)
	sinpe				=	db.Column(db.Integer)
	coordinador			=	db.Column(db.Text)
	precio				=	db.Column(db.Text)
	limite_pago			=	db.Column(db.DateTime)
	parqueo				= 	db.Column(db.Text)
	mascotas			=	db.Column(db.Text)
	duchas				= 	db.Column(db.Text)
	banos				= 	db.Column(db.Text)
	img 				= 	db.Column(db.Text, nullable=True, default="default.png")
	date_posted			=	db.Column(db.DateTime, default=datetime.utcnow)
	slug 				= 	db.Column(db.String(255))

	#Crear una llave foranea entre los Posts y los usuarios referenciado con la llave primaria del usuario
	# Donde user.id es la clase del modelo llamada  class User y .id el id de esa clase
	poster_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# AGREGAR ETIQUETAS EN FOMULARIO DEL CURSO HTML
class Tags(db.Model):
	#Al agregar un campo hay que migrarlo a la DB y aquí se crean los campos del usuario
	id 					=	db.Column(db.Integer, 	primary_key=True)
	etiqueta			= 	db.Column(db.Text, unique=False, nullable=False)
	descripcion			= 	db.Column(db.Text, unique=False,	nullable=True)
	atributos			= 	db.Column(db.Text, unique=False,	nullable=True)
	date_added			= 	db.Column(db.DateTime,	nullable=False,	default=datetime.utcnow)

class multimedia(db.Model):
	#Al agregar un campo hay que migrarlo a la DB y aquí se crean los campos del usuario
	id 					=	db.Column(db.Integer, 		primary_key=True)
	video				= 	db.Column(db.Text,	unique=False, 	nullable=False)
	usuario 			= 	db.Column(db.Text,	unique=False,	nullable=True)
	detalle				= 	db.Column(db.Text,	unique=False,	nullable=False)
	date_added			= 	db.Column(db.DateTime,		nullable=False,	default=datetime.utcnow)
	#Al agregar un campo hay que migrarlo a la DB y también agregarlo en esta fila con la misma sintaxis y orden
	poster_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	
	def __repr__(self):
		return f"('{self.video}',{self.usuario}','{self.detalle}')"

class imagenes(db.Model):
	#Al agregar un campo hay que migrarlo a la DB y aquí se crean los campos del usuario
	id 					=	db.Column(db.Integer, 		primary_key=True)
	foto				= 	db.Column(db.Text,	unique=False, 	nullable=False)
	usuario 			= 	db.Column(db.Text,	unique=False,	nullable=True)
	detalle				= 	db.Column(db.Text,	unique=False,	nullable=False)
	date_added			= 	db.Column(db.DateTime,		nullable=False,	default=datetime.utcnow)
	#Al agregar un campo hay que migrarlo a la DB y también agregarlo en esta fila con la misma sintaxis y orden
	poster_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	
	def __repr__(self):
		return f"('{self.foto}',{self.usuario}','{self.detalle}')"


# -----------------------

##########################################################################
##########################################################################
##########################################################################
# MODELOS FORMULARIO TABLAS 
# -----------------------
# /::::::::::::::::::::/
# -----------------------
# Formulario de Registro
class formularioRegistro(FlaskForm):

	# Para agregar un campo a la DB se agrega dentro de este formulario, también 
	# en el modelo y la función _repr_ del modelo, Además del formulario registro 
	# y en  los formularios que se van a representar el campo. luego se migra  el 
	# nuevo campo con los pasos que están aquí mismo en la última línea  comentada
	# llamada migracion en ----RUN----- y en actualizar contactos

	#Estos son los campos que van a crearse al momento de crear la base de datos
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES	
	username 			= 	StringField		('username', validators=[DataRequired(), Length(min=3, max=20)]) 
	apellido 			= 	StringField		('apellido', validators=[Length(min=3, max=20)]) 
	apellido2 			= 	StringField		('apellido2', validators=[Length(min=3, max=20)])
	residencia			= 	SelectField		('residencia', choices=[("Cartago"),("San José"),("Alajuela"),("Heredia"),("Limón"),("Guanacaste"),("Puntarenas")])
	email 				= 	EmailField		('email', 	validators=[DataRequired(message="Digite un Email")])
	telefono			= 	StringField		('telefono', [validators.NumberRange(message="Digite un Teléfono")])
	telefonoE			= 	StringField		('emergencia', [validators.NumberRange(message="Digite un Teléfono de emergencia")])
	celular				= 	StringField		('celular', [validators.NumberRange(message="Digite un Celular")])
	password 			= 	PasswordField	('password',validators=[DataRequired(message='Se Requiere Password'), Length(min=8, max=20)]) 
	confirmpassword 	= 	PasswordField	('confirmpassword',validators=[DataRequired(message='Se Requiere Confirmación de Password'), EqualTo('password', message='Password No Coincide')], id="confirmpassword")
	alergias			= 	StringField		('alergias', validators=[Length(min=3, max=100)])
	tiposangre 			= 	SelectField		("sangre", validators=[DataRequired()], choices=[("No Indico"),("No Recibo Transfuciones"),("A+"),("A-"),("B+"),("B-"),("AB+"),("AB-"),("O+"),("O-")],)
	cronico				= 	StringField		('cronica', validators=[ Length(min=3, max=100)])
	medicamentos		= 	StringField		('medicamentos', validators=[Length(min=3, max=100)])
	nacimiento			= 	StringField		('nacimiento', validators=[Length(min=3, max=60)])
	avatar				=	FileField		('Avatar')
	submit 				= 	SubmitField		('Registrarme')

	def validate_email(self, email):
		#user es la variable que almacena el primer email de contenido de la db
		user = User.query.filter_by(email.email.data).first()
		#Si la variable o si el email existe
		if user:
			#Advierte que el Email ya fue tomado.
			flash("El email ya fue tomado. Use otro ")

# Formularios de Login
class formularioLogin(FlaskForm):
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES
	email 				= 	StringField		('email', validators=[DataRequired(), Email()])
	password 			= 	PasswordField	('password', validators=[DataRequired()]) 
	rememberme 			= 	BooleanField	('checkbox')
	submit  			= 	SubmitField		('Ingresar')

# Formulario de posteo
class PostForm(FlaskForm):
	titulo 				= 	StringField		("Titulo", validators=[DataRequired()])
	descripcion 		= 	StringField		("Breve Descripción", validators=[DataRequired()])	
	# content 			= 	StringField		("Contenido", validators=[DataRequired()], widget=TextArea())
	content 			= 	CKEditorField	("Contenido", validators=[DataRequired()])
	kilometros 			= 	IntegerField	("Distancia | Millas", validators=[DataRequired()])
	altura 				= 	IntegerField	("Altimetría")
	lugar				= 	StringField		("Nombre del Lugar", validators=[DataRequired()])
	finaliza			= 	StringField		("Finaliza", validators=[DataRequired()])
	etapa				= 	SelectField		("Etapa #", validators=[DataRequired()], choices=[("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9"),("10"),("11"),("12"),("13"),("14"),("15"),("16")])
	capacidad			= 	IntegerField	("Capacidad de Transporte", validators=[DataRequired()])
	hora				= 	TimeField		("Hora de Inicio", validators=[DataRequired()])
	salida				= 	StringField		("Salimos de:", validators=[DataRequired()]) 
	dificultad			= 	StringField		("Dificultad:", validators=[DataRequired()])
	capacidad			= 	IntegerField	("Capacidad de Transporte", validators=[DataRequired()])
	sinpe				= 	IntegerField    ("Número Sinpe Autorizado", validators=[DataRequired()])
	coordinador 		= 	StringField		("Guía", validators=[DataRequired()])	
	precio				= 	IntegerField	("Capacidad de Transporte", validators=[DataRequired()])
	limite_pago			= 	IntegerField	("Capacidad de Transporte", validators=[DataRequired()])
	parqueo 			= 	SelectField		("Parqueo", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	mascotas			= 	SelectField		("Acepta Mascotas", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])				
	duchas				= 	SelectField		("Hay Duchas", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	banos				= 	SelectField		("Servicios Sanitarios", validators=[DataRequired()], choices=[("SI"),("NO"),("NO APLICA")])
	img 				=	FileField		('Imagenes')
	poster_id 			= 	StringField		("Autor", validators=[DataRequired()])
	slug 				= 	StringField		("Detalle", validators=[DataRequired()])
	submit 				= 	SubmitField		("Crear")

# Formulario de Registro
class TagForm(FlaskForm):
	etiqueta 			= 	StringField		('etiqueta', validators=[DataRequired()]) 
	descripcion			= 	CKEditorField	('descripcion', validators=[DataRequired()]) 
	atributos 			= 	StringField		('atributos', validators=[DataRequired()])			
	submit 				= 	SubmitField		("Crear")

# Multimedia
class multimForm(FlaskForm):
	video				= 	CKEditorField	('video', validators=[DataRequired()])
	usuario 			= 	StringField		('usuario', validators=[DataRequired()])  
	detalle 			= 	StringField		('detalle', validators=[DataRequired()])
	submit 				= 	SubmitField		("Crear")

# Fotos
class imagenForm(FlaskForm):
	foto				= 	FileField		('foto', validators=[DataRequired()])
	usuario 			= 	StringField		('usuario', validators=[DataRequired()])  
	detalle 			= 	StringField		('detalle', validators=[DataRequired()])
	submit 				= 	SubmitField		("Crear")

# Formulario de búsqueda
class SearchForm(FlaskForm):
 # CAMPOS EN DB			   TIPO DE DATO		NOMBRE DE CAMPO EN HTML Y VALIDACIONES
  	searched			= 	StringField		('Buscar', validators=[DataRequired()])	

# -----------------------

##########################################################################
##########################################################################
##########################################################################
# #VIEWS ------------------
# Viables que se pueden utilizar en jinja
# safe, capitalize, lower, upper, title,trim,striptags
#trim Elimina los espacios finales

# HOME
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
	title = "INICIO"
	return render_template("index.html",title=title)

# CONTACTENOS
@app.route("/contact")
def contact():
	title = "CONTACTENOS"
	return render_template("contact.html",title=title)

# CAMINATAS
@app.route("/caminatas")
def caminatas():
	title = "CAMINATAS"
	return render_template("caminatas.html",title=title)


# LOGIN
@app.route("/login")
def login():
	title = "LOGIN"
	return render_template("login.html",title=title)

# REGISTRO
@app.route("/register")
def register():
	title = "REGISTRARME"
	return render_template("register.html",title=title)





# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# ALERTA DE ERRORES
# Error URL Invalida
@app.errorhandler(404)
# Error página no encontrada
def page_not_found(e):
	return render_template('./include/404.html'), 404

# Error Servidor Interno
@app.errorhandler(500)
# Servidor no encontrada
def server_not_found(e):
	return render_template('./include/500.html'), 500
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------






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