import basedatos.bd as bd
from modelos.Persona import Persona
from modelos.Vehiculo import Vehiculo
from modelos.Revision import Revision
from datetime import datetime
from sqlalchemy import extract

#########################################################

#WELCOME
def get_welcome_message(bot_data):
    response = (
                f"Hola, soy *{bot_data.first_name}* "
                f"También conocido como *{bot_data.username}*.\n\n"
                "¡Estoy aquí para ayudarte a gestionar tus revisiones de vehículos!"
                )
    return response

#########################################################

#ABOUT
def get_about_this(VERSION):
    response = (
                f"Simple Expenses Bot (pyTelegramBot) v{VERSION}"
                "\n\n"
                "Desarrollado por: "
                "\n\n"
                "Julian Betancur, Natalia Castellanos y Libardo Morales"
                )
    return response

#########################################################

#HELP
def get_help_message ():
    response = (
                "Estos son los comandos y órdenes disponibles:\n"
                "\n"
                "*/start* - Inicia la interacción con el bot (obligatorio)\n"
                "*/help* - Muestra este mensaje de ayuda\n"
                "*/about* - Muestra detalles de esta aplicación\n"
                )
    return response

########################################################

#FALLBACK
def get_fallback_message (text):
    response = f"\U0001F648 No entendí lo que me acabas de decir"
    return response