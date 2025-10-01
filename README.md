## TP2- Introducción al desarrollo de software (TB022)- Catedra Lanzillotta
Este proyecto consiste en el desarrollo de una página web utilizando Flask como framework principal, junto con Python, HTML y CSS. De forma complementaria, se evalúa la incorporación de JavaScript para ampliar las funcionalidades del frontend.

El objetivo principal es adquirir experiencia práctica en el diseño y construcción de interfaces web, priorizando la presentación visual y la interacción con el usuario.

Este trabajo se enmarca en la cátedra del profesor Bruno Lanzillota, correspondiente a la materia Introducción al Desarrollo de Software.

## Integrantes del grupo

- [Valentín Gabriel Somoza 109188](https://github.com/ValentinSomoza)
- [Ronny Mamani Torrez 114779](https://github.com/MTRony)
- [Alvaro Ricardo Avalos Aguilar 114565](https://github.com/Alvaro17-max)


## Dependencias
Para la realizacion del proyecto se utilizo Python 3.12.
Para poder arrancar este proyecto se necesitan las siguientes bibliotecas de Python:
- **Flask** → framework principal
- **Flask-Mail** → para el envio de correos electronicos
- **python-dotenv** → manejo de variables de entorno


```bash
pip install flask Flask-Mail python-dotenv
```

## Cómo ejecutar el proyecto en modo debug:

## crear entorno virtual
- Ejecutamos: `pipenv install flask`
  Esto instalara Flask y crea un entorno virtual con Pipenv, gestionando las dependencias en Pipfile.
 `pipenv shell` activa nuestro entorno virtual para trabajar dentro de él.
  Para desaactivarlo ejecuta `deactivate`

## Instalar dependencias
Con el entorno virtual activado, instalamos las dependencias del proyecto

- Ejecuta `pip install -r requirements.txt`

Esto instala todas las dependencias necesarias para ejecutar el proyecto

## Seteo de variables para correr flask
`export FLASK_APP=app.py`
`export FLASK_DEBUG=1`
`flask run` Esto te permite ver y probar tu aplicación en un navegador.
```bash
pipenv shell
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```