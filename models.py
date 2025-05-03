from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Registro(Base):
    __tablename__ = 'registros'

## ESTRUCTURA DE BASE DE DATOS ##
