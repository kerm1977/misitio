
#*********************************************************************
# "INSTALAR EL FRAMEWORK WEB FLASK Y CREAR EL ENTORNO VIRTUAL" 
#*********************************************************************

Antes de crear la carpeta, tener PYTHON INSTALADO con el PATH debidamente configurado y el gestor de paquete --> pip que se instala al mismo tiempo con el instalador de Python. Desde la consola llegar al directorio Desktop y ahí seguir los siguientes pasos. 

	C:\Users\MINIOS\Desktop\  <--DEBES ESTAR AQUI

	----------------------------------
	|Pasos de instalación desde CMD: |
	----------------------------------
	md flaskapp	
	<-- crear una carpeta llamada flaskapp
	------------------------------

	cd flaskapp
	<-- acceder a la carpeta llamada flaskapp
	------------------------------

	python -m venv env 
	<-- crear un entorno virtual llamado env
	------------------------------

	echo "CURSO DE FLASK" > README.md 
	<-- crear un archivo README.md que contieneinstrucciones de algo determinado










------------------------------
------------------------------
------------------------------

#*********************************************************************
#Activar el entorno virtual: |
#*********************************************************************

El entorno virtual es una forma de tener instalado todas las dependecias y librerías que va a tener nuestro proyecto. Cuando activamos el entorno virtual, cada instalación que se realice para el proyecto, se va a guardar dentro de la carpeta "env" que se va a crear y no se va a instalar en la carpeta de Python de nuestro PC. Esto además de ser más seguro, permite la portabilidad del proyecto a otros equipos y luego reinstalar todo el contenido paquetes y librerías que ya van instalados dentro de esa misma carpeta "env". 

Instalar el entorno virtual es tan sencillo como utilizar el comando python -m venv env, Dentro de la carpeta creada llama flaskapp, ahora estando dentro de la carpeta flaskapp debe verse una llamada env....Para ingresar a ella se digita en la consola:

	cd env
	<-- para entrar a env
	------------------------------

	cd scripts
	<-- para entrar a scripts
	------------------------------

	activate
	<-- activar el entorno virtual
	------------------------------


si el prompt cambia de forma por ejemplo --> (env) λ ya estaría activado y con el entorno activado se instalan las librerías y paquetes de este proyecto. Está claro que eso solo afecta o se aplica a el proyecto flaskapp y no a otros proyectos flask creados a menos que todas las librerías estén tambíén isntaladas dentro del PC pero no es una práctica recomendable.










------------------------------
------------------------------
------------------------------

#*********************************************************************
# INSTALAR FLASK Y OTRAS DEPENDENCIAS: |
#*********************************************************************

	pip install flaskapp 
	<-- instala flask dentro de la carpeta
	------------------------------

	python.exe -m pip install --upgrade pip
	<-- Es posible que aparezca acualizar pip y solo se ejecuta si lo solicita. EN CASO CONTRARIO omitir este comando.

	pip list 
	<-- al finalizar la instalación de flask por  medio de este comando se verifica las dependencias creadas
	------------------------------

	pip freeze > requirements.txt 
	<-- crea un archivo con las dependencias creadas. 
	------------------------------

	pip install -r requirements.txt   <--SOLO PARA MIGRAR A OTRO EQUIPO
	<-- Esto hace una instalación de las librerias cuando se pasa el proyecto a otro equipo pero no es necesario aplicarlo apenas creado al app ya que eso solo es para recuperar o migrar el file a otro equipo.
	------------------------------

	pip freeze
	<-- Este comando muestra únicamente los paquete instalados de flask.
	------------------------------


DESDE CMD volver a la raíz del proyecto
Si te encuentras en la siguiente ruta --> \Desktop\flaskapp\env\Scripts debes volver a la raíz del proyecto  digitando cd..--> \Desktop\flaskapp,  este comando permite regresar un directorio  por lo que si lo digitaste una vez quedaría \Desktop\flaskapp\env. Si vuelves a digitar cd.., debe quedar en la raíz de flaskapp -- >\Desktop\flaskapp

Estando ya dentro de \Desktop\flaskapp la raíz debe quedar de la siguiente manera.

carpeta(flaskapp)
	carpeta(env)
	archivo(README.md)
	archivo(requeriments.txt)

ejemplo:

	flaskapp
		--env
		--README.md
		--requeriments.txt

AHORA ABRIR LA CARPETA EN EL EDITOR DE TEXTO 

	sublimetext
	Visual Studio Code
	notepad++
	Atom()
	brackets
	vim









------------------------------
------------------------------
------------------------------

#*********************************************************************
# AL AGREGAR A UN EDITOR DE CÓDIGO  |
#*********************************************************************
Para iniciar La carpeta debe quedar de la siguieten forma. Claro está que conforme el proyecto va creciendo la el contenido del proyecto va cambiando un poco.


	flaskapp 			<-- Nombre de la carpeta base
		--env			<-- Esta carpeta se creo cuando se creo el entorno virtual
		--README.md 	<-- Información  
		--requeriments.txt 	<-- Estas son dependencias que se crearon al ejecutar 
								pip freeze > requirements.txt 


Todos esos archivos se encuentran dentro de la raíz del proyecto osea al mismo nivel
aqui se van a crear otras carpetas y el archivo de configuración que puede ser llamado 
app.py o main.py, pero solo iniciaremos creando el archivo main.py

flaskapp 			*<-- Nombre de la carpeta base
	--env			*<-- Esta carpeta se creo cuando se creo el entorno virtual
	--README.md 	*<-- Información  
	--requeriments.txt 	*<-- Estas son dependencias que se crearon al ejecutar 
						pip freeze > requirements.txt 
	--main.py 		*<-- Este archivo va a contener cierta información de configuración del 						proyecto
	


------------------------------
------------------------------
------------------------------

#*********************************************************************
# PRIMER HOLA MUNDO  |
#*********************************************************************
Luego de haber instalado flask y las dependencias citadas arriba además con el entorno virtual activado, que se vea similar a este--> (env) λ dentro del editor de texto en el archivo anteriormente creado main.py se importa flask. El siguiente ejemplo es un programa completamente básico pero muestra en el navegaro la plabra hola mundo.....


from flask import Flask *<--Importa dentro de main.py la librería flask. flask es el módulo y 								la clase de ese módulo se llama Flask

app = flask(__name__) *<--Instancia que crea la aplicación El método __ init__ es un 									constructor que inicializa atributos para objetos en los que el 								archivo __ init__.py dentro de una carpeta. le dice a Python que 								interprete o considere esta carpeta como un paquete de Python en lugar 							de una carpeta simple (es una especie de constructor para inicializar 							una carpeta como un paquete y es el nombre del módulo Python actual. La 						aplicación necesita saber dónde se encuentra para configurar 									algunas rutas y __name__es una forma conveniente de decirle a la app 							que donde se encuentre esta línea es nuestro archivo principal. para 							que todos los archivos estáticos plantillas y demás módulos sepan donde 						tienen que ir a buscar


@app.route("/hola") *<-- Esta ruta tiene que estar relacionada a una función#
					se puede decir para mejor comprensión que esta es la url 
					del navegador. En flask esa línea se llama decorador
					y el /hola va seguido de la dirección ya que apunta a la función relacionada llamada  hola() que es la siguiente.


def hola(): *<--Esta es la función llamada hola() representa una vista una función*
	return ("Hola Mundo") *<-- y esta función debe retornar retorna una vista con un mensaje*


# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
if __name__ == "__main__":
	app.run(
	debug 	= True,  *<--Permite realizar los cambios cuando se salva el proyecto sin necesidad 					de reinicial el servidor* 
	port 	= 3000 	*<--El archivo se ejecuta en el puerto 3000 o el que se seleccione para 						evitar conflictos con servidores ya utilizados por otrs servicios* 
	) 


Ahora cuando este mini programa se salva en el CMD o consola con el entorno virtual encendido y a la misma altura donde se encuentran la carpeta env, y los archivos README.md, requieriments.txt, se ejecuta un servidor integrado que debe ser utilizado únicamente para desarrollo y no producción
>>python main.py

Tiene que aparecer algo similar a esto:

	C:\Users\MINIOS\Desktop\cursoflask
	(env) λ python main.py
	 * Serving Flask app 'main'
	 * Debug mode: on
	WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
	 * Running on http://127.0.0.1:3000
	Press CTRL+C to quit
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 717-600-841

ahora se copia la dirección que vemos en el texto anterior seguido del nombre de la función que creamos "hola" http://127.0.0.1:3000/hola y se coloca en la barra de búsqueda del navegador que utilices. Claro está que del mismo equipo donde estamos trabajando. LOCAL

En el navegador ya se debe visualizar el hola mundo.


































------------------------------
------------------------------
------------------------------
---------------------------------------
| 	OTROS DETALLES DE FLASK 		  |
---------------------------------------

#*********************************************************************
#FILTROS
#*********************************************************************

# Los filtros permiten procesar y transformar valores antes de ser mostrados en pantalla
# y se aplican directamente en la plantilla y eso se hace directamente 

# Existen filtros para pasar texto a mayuscula, minuscula, revertir listas 

	# POR EJEMPO UN LISTA EN LAS FUNCIONES DE APP.PY SE DECLARA LA LISTA
	# DE LA FUNCIÓN DE ARRIBA LLAMADA INDEX CON LA LISTA AMIGOS Y EN LA PLANTILLA
	# HTML SE CREA EL FOR DONDE SE PASA EL FILTRO | UPPER
	

	# <!-- reverse invierte el orden de la lista -->
	# {%for i in amigos | reverse%} 
	# 	<p>{{i | upper}}</p><br>
	# {%endfor%}




#*********************************************************************
# FILTROS PERSONALIZADOS
#*********************************************************************

	# from datetime import datetime
	# date time debe ser llamado para que funciones horas y fechas
	# Para que esto trabaje debajo de la declaración de la función
	
	# ejemplo
		# @app.route("/pepino") 					<-- Esta ruta tiene que estar relacionada a una función
		# def pepino(): 							<-- Y esta representa una vista
		#	date = datetime.now()  					<-- llama la fecha de hoy en día*******************
		# 	return ("Hola Mundo", date = date) 		<-- y se llama dentro de return separado por , e =

		# y en html se llama como {{date | today}}

	# y se llama igual en html se coloca entre llaves {{date}}

	# También se puede crear una fecha y hora más detallada a través de una función
		# @app.add_template_filter 					<-- Agrega este filto today a los filtros de la app o se puede utilizar la opcion de abajo
		# def today(date):							
		#	return date.strftime("%d-%m-%Y")
		# app.add_template_filter(today, "today")	<-- Esta también registra el filtro o la de arriba --- @app.add_template_filter--- ambas funcionan 





#*********************************************************************
#OTROS FILTROS PERSONALIZADOS ------------------------
#*********************************************************************

	# Esta funcion multiplica el string s por n 

	# @app.add_template_global  <-- si se escribe esto ya no es necesario invocarlo en --> render_template( repeat = repeat )
	# def repeat(s,n):
	# 	return s*n

	# app.add_template_global(repeat, "repeat") <--aqui abajo  es otra forma de utilizar y no se necesita el decorador arriba ---->   @app.add_template_global 






	# y REPEAT puede ser llamada dentro de otras funciones ----------------
		# 	@app.route("/index")
		# 	def index():
		# 		......
									                                                         # v       v
		# 		return render_template ("index.html", variableX = variableX, amigos=amigos repeat = repeat) 


		#  y en HTML SE LLAMA DE LA SIGUENTE FORMA-------------------
		# 		<p>{{repeat("hola",3)}}</p>








#*********************************************************************
#  MYSQL CONECTOR ------------------------
#*********************************************************************

MYSQL CONECTOR
Descargar Mysql desde  Instalarlo
	https://dev.mysql.com/downloads/ 

	o en el enlace directo
	https://dev.mysql.com/downloads/installer/   <-Windows

	CONFIGURAR E INSTALAR EN EL ENV LOS CONECTORES 
	# pip uninstall mysql-connector
	# pip install mysql-connector-python	

	EJECUTAR create_db.py y crear una nueva base de datos
