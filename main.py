from flask import Flask, render_template, request, url_for, redirect
from flask.globals import session
from connection import session, actividad

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        items = []
        try:
            sesion = session()
            items = sesion.query(actividad).order_by(actividad.fechaCreacion).all()
        except:
            return render_template('index.html', items=items)
        return render_template('index.html', items=items)
    elif request.method == 'POST':
        GetNombre = request.form['nombre'].strip()
        if GetNombre == "":
            return redirect('/')
        else:
            sesion = session()
            nuevaActividad = actividad(GetNombre)
            sesion.add(nuevaActividad)
            sesion.commit()
            print(int(nuevaActividad))
            return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        try:
            sesion = session()
            item = sesion.query(actividad).filter(actividad.idActividad == id).one()
            return render_template('update.html', item=item)
        except:
            return 'Dato no disponible'

    if request.method == 'POST':
        try:
            sesion = session()
            item = sesion.query(actividad).filter(actividad.idActividad == id).one()
            item.nombre = request.form['nombre'].strip()
            if item.nombre == '':
                return 'No lleno el campo nombre!'
            
            sesion.commit()
            return redirect('/')
        except:
            return 'Error al modificar!'


@app.route('/delete/<int:id>')
def delete(id):
    try:
        sesion = session()
        item = sesion.query(actividad).filter(actividad.idActividad == id).one()
        print(int(item))
        sesion.delete(item)
        sesion.commit()
        return redirect('/')
    except:
        return 'Error al eliminar'


if __name__ == '__main__':
    app.run()