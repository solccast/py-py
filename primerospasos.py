from flask import Flask, render_template, request, jsonify # type: ignore #Clase importada #Render template es parte de Flask 

app = Flask(__name__) #Crea un objeto de tipo flask

@app.route('/')
def index():
    return "Hola mundo!"

@app.route('/sobreRenderizar/<nombre>/<int:edad>') #Decorador
def probando_render(nombre, edad):
    print('Esta es la informacion que se recibe por parametros: ', nombre, edad)
    cursos = ['Php', 'Java', 'JavaScript', 'Kotlin', 'Ruby']
    data={
        'title':'index',
        'bienvenida': '¡Saludos!',
        'cursos': cursos,
        'length' : len(cursos)
    }

    return render_template("jinja.html", data=data) #Renderización de una plantilla. A la plantilla le paso el diccionario data

def query_STRING():
    print(request)
    print(request.args)
    print(request.args.get('clave')) #con el método get obtenemos el valor del param
    print(request.args.get('vacio')) #Flask no se rompe cuando no se envia determinado parámetro --> objeto None
    return "Hola!"

def pagina_no_encontrada(error):
    return "Ups, esta page no existe :(", 404 #Enviando un error 

def apiJson():
    data = {
        'message': 'ok',
        'data': {
            'nombre': 'Juan',
            'apellido': 'Perez con pan'
        }
    }
    return jsonify(data)

app.add_url_rule('/query', view_func=query_STRING) #Así asociamos una función con una función
app.add_url_rule('/apibasic', view_func=apiJson)
app.register_error_handler(404, pagina_no_encontrada)

if __name__ == "__main__":
    app.run(debug=True, port=5000) #Debug para no tener que reiniciar el server ante cualquier cambio y el puerto que podemos modificarlo. 