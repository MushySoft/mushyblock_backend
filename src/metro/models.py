from src import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class MetroMatch(Base):
    __tablename__ = "metro_match"

    id = Column(Integer, primary_key=True)
    id_line = Column(Integer, ForeignKey("line.id"))
    id_station = Column(Integer, ForeignKey("station.id"))

    line = relationship("Line", back_populates="metro_match")
    station = relationship("Station", back_populates="metro_match")


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)

    metro_match = relationship("MetroMatch", back_populates="station")


class Line(Base):
    __tablename__ = "line"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)

    metro_match = relationship("MetroMatch", back_populates="line")
