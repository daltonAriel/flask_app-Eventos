from sqlalchemy import Column, create_engine, engine, desc, asc
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///actividades.db")
DB = declarative_base(engine)
session = sessionmaker(engine)

class actividad(DB):
    __tablename__ = 'actividad'
    idActividad = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    fechaCreacion = Column(DateTime, nullable=False, default=datetime.now())
    
    def __init__(self, nombreActividad):
        self.nombre = nombreActividad

    def __int__(self):
        return self.idActividad
