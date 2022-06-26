import basedatos.bd as bd
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from datetime import timedelta

"""Se crea la clase equivalente a la entidad Revisión_Repuesto para posteriormente ser creada en la base de datos
    Se asigna el nombre a la tabla
    Se crean cada uno de los campos con sus respectivos tipos de datos y condicionales.
    Se asignan las llaves foráneas
    Se crea el camino bidireccional con la tabla revisión y con la tabla respuesto
    Se crea el consturctor de la clase 
    Se crea método para retornar el id de un revisión_repuesto
"""
class Revision_Repuesto(bd.Base):

    __tablename__ = 'revisiones_repuestos'

    id_revision_repuesto = Column('id_revision_repuesto', Integer, primary_key=True, autoincrement=True)
    revision_id = Column('revision_id', Integer, ForeignKey('revisiones.id_revision', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    repuesto_id = Column('repuesto_id', Integer, ForeignKey('repuestos.id_repuesto', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    cantidad_repuesto = Column('cantidad_repuesto', Integer, nullable=False)
    
    revisiones = relationship('Revision', back_populates='revisiones_repuestos')
    repuestos = relationship('Repuesto', back_populates='revisiones_repuestos')

    def __init__(self, id_revision_repuesto, revision_id, repuesto_id, cantidad_repuesto):
        self.id_revision_repuesto = id_revision_repuesto
        self.revision_id = revision_id
        self.respuesto_id = repuesto_id
        self.cantidad_repuesto = cantidad_repuesto        

    def __repr__(self):
        return f"<Revision_Repuesto {self.id_revision_repuesto}>"