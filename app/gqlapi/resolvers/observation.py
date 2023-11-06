from app.gqlapi.types.observation import ObservationInput
import strawberry
from sqlalchemy.future import select
from app.gqlapi.types.observation import Observation
from app.models.observation import ObservationModel
from app.core.database import get_async_session


@strawberry.type
class Query:
    @strawberry.field(
        description="Retrieves an observation by its ID. Returns the observation details if found, or `None` if no "
                    "observation with the given ID exists."
    )
    async def get_observation(self, id: strawberry.ID) -> Observation | None:
        async with get_async_session() as session:
            observation_id = int(id)
            stmt = select(ObservationModel).where(ObservationModel.id == observation_id)
            result = await session.execute(stmt)
            observation = result.scalar_one_or_none()

            if observation:
                return Observation(
                    id=observation.id,
                    name=observation.name,
                    description=observation.description,
                    wavelength=observation.wavelength
                )
            else:
                return None

    @strawberry.field(description="Retrieve all observations from the database.")
    async def get_observations(self) -> list[Observation]:
        async with get_async_session() as session:
            result = await session.execute(select(ObservationModel))
            observation_models = result.scalars().all()
            return [
                Observation(
                    id=str(obs.id),
                    name=obs.name,
                    description=obs.description,
                    wavelength=obs.wavelength
                )
                for obs in observation_models
            ]


@strawberry.type
class Mutation:
    @strawberry.mutation(
        description="Creates a new Observation entity in the database using the provided input data. Returns the "
                    "created Observation with its new ID and data."
    )
    async def create_observation(self, input: ObservationInput) -> Observation:
        async with get_async_session() as session:
            db_observation = ObservationModel(
                name=input.name,
                description=input.description,
                wavelength=input.wavelength
            )
            session.add(db_observation)
            await session.commit()
            await session.refresh(db_observation)
        return Observation(
            id=db_observation.id,
            name=db_observation.name,
            description=db_observation.description,
            wavelength=db_observation.wavelength
        )
