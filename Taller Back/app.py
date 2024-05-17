from flask import render_template, request, redirect, url_for, session # noqa: F401
from conexion import app, db  # noqa: F401
from models import Usuarios, Notas  # noqa: F401

@app.route('/')

def index():
    nombre = "Sebastian"
    return render_template("index.html", nombre=nombre)

@app.route("/registrar", methods = ['POST', 'GET'])

    
def registrar():

    if request.method =='POST':

        nombre = request.form['nombre']  
        apellido = request.form['apellido']  
        cedula = request.form['cedula']  
        correo = request.form['correo']    # noqa: F841

        # Creamos un objeto de la clase usuario con los datos obtenidos
        datos_usuario = Usuarios(nombre, apellido, cedula, correo)

        db.session.add(datos_usuario)

        db.session.commit() #Metodo para confirmar todas las operaciones registradas en la sesion

        session["usuario_id"] = datos_usuario.id
        
        return render_template("cargar_notas.html")

    return render_template("registrar.html")

@app.route('/cargar_notas',methods = ['POST', 'GET'])

def cargar_notas():
    if request.method == 'POST':
        fecha = request.form['fecha']
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        usuario_id = session.get("usuario_id")  # noqa: F821

        notas_registradas = Notas(fecha, titulo, descripcion, usuario_id)

        db.session.add(notas_registradas)
        db.session.commit()

        return render_template("cargar_notas.html")
    return render_template("cargar_notas.html")


@app.route('/ver_notas', methods = ['POST','GET'])

def ver_notas():
    usuario_id = session.get("usuario_id")

    notas = Notas.query.filter_by(usuario_id=usuario_id).all()

    return render_template('ver_notas.html', notas=notas)

if __name__ == "__main__":
    app.run(debug = True)
