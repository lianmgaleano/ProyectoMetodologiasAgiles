import basedatos.bd as bd
from modelos.Persona import Persona
from sqlalchemy import extract, and_

class LogicaPersona:

    def registrar_persona(numero_documento, nombre_completo, tipo):
        """ Registrar persona: se verifica la existencia del documento ingresado y del tipo de persona
            Si la persona ya se encuentra registrada se retorna False
            Si la persona no se encuentra registrada se crea el objeto persona,
            Se agrega el registro a la tabla personas,
            Se hace commit y se retorna True """
        persona = bd.session.query(Persona).filter(and_(Persona.documento == numero_documento, Persona.tipo_persona == tipo)).first()
        bd.session.commit()

        if persona == None:
            persona = Persona(
                numero_documento, 
                nombre_completo, 
                tipo)
            bd.session.add(persona)
            bd.session.commit()
            return True
        return False

