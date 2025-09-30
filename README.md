# Tp2-IDS
Este proyecto consiste en el desarrollo de una página web, implementada utilizando Python y el framework Flask para la estructura general de la aplicación, junto con HTML, CSS y JavaScript como tecnologías principales para el frontend.

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

```bash
pipenv shell
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```