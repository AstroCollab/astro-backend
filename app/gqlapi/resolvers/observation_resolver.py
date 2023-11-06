import strawberry
from app.gqlapi.types.observation import ObservationInput
from app.gqlapi.types.observation import Observation
from app.repositories.observation_repository import ObservationRepository
from app.services.observation_service import ObservationService

observation_service = ObservationService(ObservationRepository())


@strawberry.type
class Query:
    @strawberry.field(
        description="Retrieves an observation by its ID. Returns the observation details if found, or `None` if no "
                    "observation with the given ID exists."
    )
    async def get_observation(self, id: strawberry.ID) -> Observation | None:
        observation_id = int(id)
        return await observation_service.retrieve_observation(observation_id)

    @strawberry.field(description="Retrieve all observations from the database.")
    async def get_observations(self) -> list[Observation]:
        return await observation_service.retrieve_all_observations()


@strawberry.type
class Mutation:
    @strawberry.mutation(
        description="Creates a new Observation entity in the database using the provided input data. Returns the "
                    "created Observation with its new ID and data."
    )
    async def create_observation(self, observation_input: ObservationInput) -> Observation:
        return await observation_service.create_observation(observation_input)
