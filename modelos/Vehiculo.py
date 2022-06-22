import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Vehículo para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se asignan las llaves foráneas
    Se crea el camino bidireccional con la tabla persona y con la tabla revisión
    Se crea el constructor de la clase 
    Se crea método para retornar el id de un vehículo
"""
class Vehiculo(bd.Base):

    __tablename__ = 'vehiculos'

    id_vehiculo = Column('id_vehiculo', Integer, primary_key=True, autoincrement=True)
    placa = Column('placa', String(10), nullable=False)
    tipo_vehiculo = Column('tipo_vehiculo', String(10), nullable=False)
    dueño_id = Column('dueño_id', Integer, ForeignKey('personas.id_persona', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    mecanico_id = Column('mecanico_id', Integer, ForeignKey('personas.id_persona', onupdate='CASCADE', ondelete='CASCADE'))
    
    personas = relationship('Persona', back_populates='vehiculos')
    revisones = relationship('Revision', back_populates='vehiculos')

    def __init__(self, id_vehiculo, placa, tipo_vehiculo, dueño_id):
        self.id_vehiculo = id_vehiculo
        self.placa = placa
        self.tipo_vehiculo = tipo_vehiculo
        self.dueño_id = dueño_id

    def __repr__(self):
        return f"<Vehiculo {self.id_vehiculo}>"