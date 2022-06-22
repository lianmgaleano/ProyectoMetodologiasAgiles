import basedatos.bd as bd
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Persona para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se crea el camino bidireccional con la tabla vehículo
    Se crea el constructor de la clase 
    Se crea método para retornar el id de la persona
"""
class Persona(bd.Base):

    __tablename__ = 'personas'

    id_persona = Column('id_persona', Integer, primary_key=True, autoincrement=True)
    documento = Column('documento', String(15), nullable=False)
    nombre_completo = Column('nombre_completo', String(100), nullable=False)
    tipo_persona = Column('tipo_persona', String(1), nullable=False)

    vehiculos = relationship('Vehiculo', back_populates='personas')
    
    def __init__(self, id_persona, documento, nombre_completo, tipo_persona):
        self.id_persona = id_persona
        self.documento = documento
        self.nombre_completo = nombre_completo
        self.tipo_persona = tipo_persona

    def __repr__(self):
        return f"<Persona {self.id_persona}>"