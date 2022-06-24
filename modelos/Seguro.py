import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Seguro para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se crea el camino bidireccional con la tabla vehículo_seguro
    Se crea el consturctor de la clase 
    Se crea método para retornar el id de un seguro
"""
class Seguro(bd.Base):

    __tablename__ = 'seguros'

    id_seguro = Column('id_seguro', Integer, primary_key=True, autoincrement=True)
    nombre_seguro = Column('nombre_seguro', String(50), nullable=False)

    vehiculos_seguros = relationship('Vehiculo_Seguro', back_populates='seguros')
    
    def __init__(self, id_seguro, nombre_seguro):
        self.id_seguro = id_seguro
        self.nombre_seguro = nombre_seguro

    def __repr__(self):
        return f"<Seguro {self.id_seguro}>"