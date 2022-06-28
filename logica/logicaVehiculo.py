import basedatos.bd as bd
from modelos.Persona import Persona
from modelos.Vehiculo import Vehiculo
from sqlalchemy import extract, and_

class LogicaVehiculo:

    def registrar_vehiculo(placa, tipo_vehiculo, dueno):
        """ Registrar vehiculo: se verifica la existencia del documento ingresado y del tipo de persona
            Si la persona ya se encuentra registrada se retorna False
            Si la persona no se encuentra registrada se crea el objeto persona,
            Se agrega el registro a la tabla personas,
            Se hace commit y se retorna True """
        
        vehiculo = bd.session.query(Vehiculo).filter(Vehiculo.placa == placa).first()
        bd.session.commit()
        
        if vehiculo:
            return "La placa "+ placa + " ya se encuentra registrada"
        
        if check_vehicle(tipo_vehiculo) == False:
            return "El tipo de vehiculo no pertenece a ninguno permitido, microbus ó buseta"
        
        persona = bd.session.query(Persona).filter(and_(Persona.documento == dueno, Persona.tipo_persona == "1")).first()
        bd.session.commit()
        
        if persona == None:
            return "El dueño con documento " + dueno + " no se encuentra registrado"
        
        vehicle = Vehiculo(
            placa, 
            tipo_vehiculo, 
            persona.id_persona
        )
        bd.session.add(vehicle)
        bd.session.commit()
        
        return "Se ha agregado el vehículo exitosamente"

#########################################################

#Verifica si el tipo de vehiculo pertenece al listado de tipos de vehículo permitidos
def check_vehicle(tipo):
    TIPOS_VEHICULO = ['microbus', 'buseta']
    return tipo in TIPOS_VEHICULO

#########################################################