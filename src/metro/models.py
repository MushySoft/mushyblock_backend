from src.database import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Station(Base):
    __tablename__ = "station"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    connections = Column(Integer, ForeignKey("line.id"))
    line = relationship("Line", back_populates="station")

class Line(Base):
    __tablename__ = "line"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    station = relationship("Station", back_populates="line")