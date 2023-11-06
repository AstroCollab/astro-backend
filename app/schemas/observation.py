from pydantic import BaseModel


class ObservationSchema(BaseModel):
    id: int
    name: str
    description: str | None = None
    wavelength: float

    class Config:
        orm_mode = True


class ObservationCreate(BaseModel):
    name: str
    description: str | None = None
    wavelength: float
