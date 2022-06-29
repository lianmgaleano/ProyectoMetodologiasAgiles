import basedatos.bd as bd
from logica import logic
from modelos.Vehiculo import Vehiculo
from modelos.Revision import Revision
from sqlalchemy import extract, and_

class LogicaRevision:

    def registrar_revision(user_id, placa, aceite, frenos, refrigerante, direccion):
        """ Registrar persona: se verifica la existencia del documento ingresado y del tipo de persona
            Si la persona ya se encuentra registrada se retorna False
            Si la persona no se encuentra registrada se crea el objeto persona,
            Se agrega el registro a la tabla personas,
            Se hace commit y se retorna True """
        
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