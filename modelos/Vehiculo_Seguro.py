from site import venv
import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Vehículo_Seguro para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se asignan las llaves foráneas
    Se crea el camino bidireccional con la tabla vehículo y con la tabla seguro
    Se crea el consturctor de la clase 
    Se crea método para retornar el id de un vehículo_seguro
"""
class Vehiculo_Seguro(bd.Base):

    __tablename__ = 'vehiculos_seguros'

    id_vehiculo_seguro = Column('id_vehiculo_seguro', Integer, primary_key=True, autoincrement=True)
    vehiculo_id = Column('vehiculo_id', Integer, ForeignKey('vehiculos.id_vehiculo', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    seguro_id = Column('seguro_id', Integer, ForeignKey('seguros.id_seguro', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    inicio_vigencia = Column('inicio_vigencia', DateTime, server_default=func.now(),nullable=True)
    fin_vigencia = Column('inicio_vigencia', DateTime, nullable=True)
    
    vehiculos = relationship('Vehiculo', back_populates='vehiculos_seguros')
    seguros = relationship('Seguro', back_populates='vehiculos_seguros')

    def __init__(self, id_vehiculo_seguro, vehiculo_id, seguro_id, inicio_vigencia, fin_vigencia):
        self.id_vehiculo_seguro = id_vehiculo_seguro
        self.vehiculo_id = vehiculo_id
        self.seguro_id = seguro_id
        self.inicio_vigencia = inicio_vigencia
        self.fin_vigencia = fin_vigencia

    def __repr__(self):
        return f"<Vehiculo_Seguro {self.id_vehiculo_seguro}>"