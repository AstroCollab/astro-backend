from typing import Optional

import strawberry


@strawberry.type
class Observation:
    id: strawberry.ID
    name: str
    description: str
    wavelength: float


@strawberry.input
class ObservationInput:
    name: str
    description: Optional[str]
    wavelength: float

