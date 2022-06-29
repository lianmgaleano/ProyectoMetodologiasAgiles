import basedatos.bd as bd
from modelos.Persona import Persona
from modelos.Vehiculo import Vehiculo
from sqlalchemy import extract, and_

class LogicaVehiculo:

    def registrar_vehiculo(placa, tipo_vehiculo, dueno):
        """ Registrar vehiculo: se verifica la existencia de la placa ingresado, tipo de vehículo y documento del dueño
            Si la placa ya se encuentra registrada se retorna mensaje con el detalle
            Si el tipo de vehículo no se encuentra dentro de los posibles se retorna un mensaje con el detalle
            Si el documento del dueño no se encuentra se retorna un mensaje con el detalle
            Se agrega el registro a la tabla vehiculos,
            Se hace commit y se retorna Mensaje """
        
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
    
    def asignar_mecanico(placa, mecanico):
        """ Asignar mecánico: se verifica la existencia de la placa ingresado y documento del mecánico
            Si la placa no se encuentra registrada se retorna mensaje con el detalle
            Si el documento del mecanico no se encuentra se retorna un mensaje con el detalle
            Se actualiza el registro en la tabla vehiculos,
            Se hace commit y se retorna Mensaje """
            
        vehiculo = bd.session.query(Vehiculo).filter(Vehiculo.placa == placa).first()
        bd.session.commit()
        
        if vehiculo == None:
            return "La placa "+ placa + " no se encuentra registrada"
        
        persona = bd.session.query(Persona).filter(and_(Persona.documento == mecanico, Persona.tipo_persona == "2")).first()
        bd.session.commit()
        
        if persona == None:
            return "El mecánico con documento " + mecanico + " no se encuentra registrado"
        
        bd.session.query(Vehiculo).filter(Vehiculo.placa == placa).update({'mecanico_id': persona.id_persona})
        bd.session.commit()
        
        return "Se ha asignado el mecánico al vehículo exitosamente"

#########################################################

#Verifica si el tipo de vehiculo pertenece al listado de tipos de vehículo permitidos
def check_vehicle(tipo):
    TIPOS_VEHICULO = ['microbus', 'buseta']
    return tipo in TIPOS_VEHICULO

#########################################################