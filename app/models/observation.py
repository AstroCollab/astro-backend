from sqlalchemy import Column, Integer, String, Float
from . import Base


class ObservationModel(Base):
    __tablename__ = 'observations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    wavelength = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Observation(name={self.name}, wavelength={self.wavelength})>"
