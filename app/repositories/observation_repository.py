from sqlalchemy import select

from app.core.database import get_async_session
from app.gqlapi.types.observation import ObservationInput
from app.models.observation import ObservationModel


class ObservationRepository:
    @staticmethod
    async def get_observation_by_id(observation_id: int) -> ObservationModel | None:
        async with get_async_session() as session:
            stmt = select(ObservationModel).where(ObservationModel.id == observation_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    @staticmethod
    async def get_all_observations() -> list[ObservationModel]:
        async with get_async_session() as session:
            result = await session.execute(select(ObservationModel))
            return result.scalars().all()

    @staticmethod
    async def create(observation_input: ObservationInput) -> ObservationModel:
        async with get_async_session() as session:
            result = ObservationModel(
                name=observation_input.name,
                description=observation_input.description,
                wavelength=observation_input.wavelength
            )
            session.add(result)
            await session.commit()
            await session.refresh(result)
            return result
