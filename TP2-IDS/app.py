from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route("/")
def home():
    return render_template ('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template ('404.html'), 404

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    enviado = False
    if request.method == 'POST':
        nombre = request.form.get("fname")
        apellido = request.form.get("lname")
        dni = request.form.get("dni")
        carrera = request.form.get("carrera")
        correoUsuario = request.form.get("email")

        msg = Message(
            subject="Nueva inscripcion en la carrera",
            recipients=["vsomoza@fi.uba.ar", correoUsuario],
            body=f"Se registro el atleta llamado: {nombre} {apellido}\nDNI: {dni}\nCarrera: {carrera}"
        )

        try:
            mail.send(msg)
            enviado = True  # solo se activa el true si no hay error
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            enviado = False

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