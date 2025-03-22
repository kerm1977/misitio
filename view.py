from controller import *

#*********************************************************************
# Decorador y ruta
#*********************************************************************

@app.route("/") 	
def index():
	title = "Inicio" 
	return render_template("index.html", title=title)

@app.route("/saludo")
def saludo():
	title = "Pruebas"
	return render_template("hola.html", title=title)

@app.route("/login")
def login():
	title = "Ingresar"
	return render_template("login.html", title=title)



# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


