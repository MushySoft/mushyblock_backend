from src import Base
from sqlalchemy import Table, Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


MetroMatch = Table(
    'metro_match',
    Base.metadata,
    Column('line_id', Integer, ForeignKey('line.id')),
    Column('station_id', Integer, ForeignKey('station.id'))
)


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    line = relationship("Line", secondary=MetroMatch, back_populates="station")


class Line(Base):
    __tablename__ = "line"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)

    station = relationship("Station", secondary=MetroMatch, back_populates="line")
