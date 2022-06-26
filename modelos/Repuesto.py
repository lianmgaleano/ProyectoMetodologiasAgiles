import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,func
from sqlalchemy.orm import relationship

"""Se crea la clase equivalente a la entidad Repuesto para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se crea el camino bidireccional con la tabla revisiones_respuestos
    Se crea el consturctor de la clase 
    Se crea método para retornar el id de un repuesto
"""
class Repuesto(bd.Base):

    __tablename__ = 'repuestos'

    id_repuesto = Column('id_repuesto', Integer, primary_key=True, autoincrement=True)
    referencia_repuesto = Column('referencia_repuesto', String(50), nullable=False)
    nombre_repuesto = Column('nombre_repuesto', String(50), nullable=False)

    revisiones_repuestos = relationship('Revision_Repuesto', back_populates='repuestos')
    
    def __init__(self, id_repuesto, referencia_repuesto, nombre_repuesto):
        self.id_repuesto = id_repuesto
        self.referencia_repuesto = referencia_repuesto
        self.nombre_repuesto = nombre_repuesto

    def __repr__(self):
        return f"<Repuesto {self.id_repuesto}>"