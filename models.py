import motor.motor_asyncio
from beanie import Document, init_beanie


class Doc(Document):
    text: str
    tag: str


async def init():
    uri = "mongodb://test:test@localhost:27017"
    cli = motor.motor_asyncio.AsyncIOMotorClient(uri)
    await init_beanie(cli.leagues, document_models=[Doc])
