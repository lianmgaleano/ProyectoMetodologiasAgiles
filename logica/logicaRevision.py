import basedatos.bd as bd
from logica import logic
from modelos.Vehiculo import Vehiculo
from modelos.Revision import Revision
from sqlalchemy import extract, and_

class LogicaRevision:

    def registrar_revision(user_id, placa, aceite, frenos, refrigerante, direccion):
        """ Registrar persona: se verifica si es mecánico y tiene permiso para realizar revisiones
             Si no tiene los permisos se retorna un mensaje notificando que no tiene permitido realizar revisiones
             Si el vehiculo no existe se retorna un mensaje diciendo que el vehiculo no existe
             Se hace el registro a la tabla revisiones
             Se hace commit y se retorna Mensaje"""
        
        id_persona = logic.get_mechanic(str(user_id))
        
        if not id_persona:
            return "No tienes permitido realizar revisiones"
        
        vehiculo = bd.session.query(Vehiculo).filter(and_(Vehiculo.placa == placa, Vehiculo.mecanico_id == id_persona)).first()
        bd.session.commit()
        
        if vehiculo == None:
            return "No es posile realizar la revisión, vehiculo no existente o asignado a otro mecánico"
        
        rev = Revision(
            vehiculo.id_vehiculo, 
            aceite, 
            frenos,
            refrigerante,
            direccion
        )
        bd.session.add(rev)
        bd.session.commit()
        
        return "Se ha agregado la revision del vehiculo " + placa + " exitosamente"