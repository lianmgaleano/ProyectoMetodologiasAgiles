import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Revisión para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se asignan las llaves foráneas
    Se crea el camino bidireccional con la tabla vehículo
    Se crea el consturctor de la clase 
    Se crea método para retornar el id de un vehículo
"""
class Revision(bd.Base):

    __tablename__ = 'revisiones'

    id_revision = Column('id_revision', Integer, primary_key=True, autoincrement=True)
    vehiculo_id = Column('vehiculo_id', Integer, ForeignKey('vehiculos.id_vehiculo', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    nivel_aceite = Column('nivel_aceite', Integer, nullable=False)
    nivel_liquido_frenos = Column('nivel_liquido_frenos', Integer, nullable=False)
    nivel_refrigerante = Column('nivel_refrigerante', Integer, nullable=False)
    nivel_liquido_direccion = Column('nivel_liquido_direccion', Integer, nullable=False)
    fecha = Column('fecha', DateTime, server_default=func.now(),nullable=True)

    vehiculos = relationship('Vehiculo', back_populates='revisiones')
    revisiones_repuestos = relationship('Revision_Repuesto', back_populates='revisiones')
    
    def __init__(self, id_revision, vehiculo_id, nivel_aceite, nivel_liquido_frenos, nivel_refrigerante, nivel_liquido_direccion, fecha):
        self.id_revision = id_revision
        self.vehiculo_id = vehiculo_id
        self.nivel_aceite  = nivel_aceite
        self.nivel_liquido_frenos = nivel_liquido_frenos
        self.nivel_refrigerante = nivel_refrigerante
        self.nivel_liquido_direccion = nivel_liquido_direccion
        self.fecha = fecha

    def __repr__(self):
        return f"<Revision {self.id_revision}>"