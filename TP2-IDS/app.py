from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'
app.config['MAIL_PASSWORD'] = 'tu_contrasenia_app' 
app.config['MAIL_DEFAULT_SENDER'] = 'tu_correo@gmail.com'

mail = Mail(app)

@app.route("/")
def index():
    title = "Club Social y Deportivo Unidos por el Deporte"
    return render_template('index.html',page_title = title)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    enviado = False
    if request.method == 'POST':
        nombre = request.form.get("fname")
        apellido = request.form.get("lname")
        dni = request.form.get("dni")
        carrera = request.form.get("carrera")

        msg = Message(
            subject="Nueva inscripcion en la carrera",
            recipients=["destinatario@ejemplo.com"],
            body=f"Se registro {nombre} {apellido}\nDNI: {dni}\nCarrera: {carrera}"
        )

        mail.send(msg)

        enviado = True

    return render_template('registro.html', page_title="Registro Evento", enviado=enviado)


if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)

info_evento = {
1:  { "nombre": "Rally MTB 2025",
    "organizador": "Club Social y Deportivo Unidos por el Deporte",
    "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...",
    "fecha": "24 de Octubre de 2025",
    "horario": "8am",
    "lugar": "Tandil, Buenos Aires",
    "tipo_carrera": "MTB rural",
    "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"},
                        2: {"nombre": "Larga" ,"valor": "200"}},
    "Auspiciantes": ["ausp1","auspN"]
    }
}