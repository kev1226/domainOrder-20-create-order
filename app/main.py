from fastapi import FastAPI, Request
from ariadne.asgi import GraphQL
from app.graphql.schema import schema
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
graphql_app = GraphQL(schema, debug=True)
app.mount("/graphql", graphql_app)


@app.get("/")
async def root():
    return {"message": "Create Order Service running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=int(os.getenv("PORT")), reload=True
    )
