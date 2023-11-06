# Убедитесь, что вы установили strawberry-graphql с помощью pip
# pip install strawberry-graphql

import strawberry
from fastapi import FastAPI, Depends
from starlette.responses import HTMLResponse
from strawberry.fastapi import GraphQLRouter
from app.core.database import get_async_session
from app.gqlapi.resolvers.observation import Mutation as ObservationMutation
from app.gqlapi.resolvers.observation import Query as ObservationQuery


@strawberry.type
class Query(ObservationQuery):
    pass


@strawberry.type
class Mutation(ObservationMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/", include_in_schema=False)
async def root():
    # Можно вернуть HTML с информацией
    return HTMLResponse(content="<h1>GraphQL API is running</h1><p>Access the GraphQL interface at <a "
                                "href='/graphql'>/graphql</a></p>")
