from app.gqlapi.types.observation import Observation, ObservationInput
from app.repositories.observation_repository import ObservationRepository


class ObservationService:
    def __init__(self, repository: ObservationRepository):
        self.repository = repository

    async def retrieve_observation(self, observation_id: int) -> Observation | None:
        observation_model = await self.repository.get_observation_by_id(observation_id)
        if observation_model:
            return Observation(
                id=observation_model.id,
                name=observation_model.name,
                description=observation_model.description,
                wavelength=observation_model.wavelength
            )
        else:
            return None

    async def retrieve_all_observations(self) -> list[Observation]:
        observation_models = await self.repository.get_all_observations()
        return [
            Observation(
                id=str(obs.id),
                name=obs.name,
                description=obs.description,
                wavelength=obs.wavelength
            )
            for obs in observation_models
        ]

    async def create_observation(self, input: ObservationInput) -> Observation:
        db_observation = await self.repository.create(input)
        return Observation(
            id=db_observation.id,
            name=db_observation.name,
            description=db_observation.description,
            wavelength=db_observation.wavelength
        )
