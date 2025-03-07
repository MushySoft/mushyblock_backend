from src import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


metro_match = Table(
    "metro_match",
    Base.metadata,
    Column("id_station", Integer, ForeignKey("station.id"), primary_key=True),
    Column("id_line" Integer, ForeignKey("line.id"), primary_key=True),
)


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)

    lines = relationship("Line", secondary=metro_match, back_populates="stations")


class Line(Base):
    __tablename__ = "line"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)

    stations = relationship("Station", secondary=metro_match, back_populates="lines")
