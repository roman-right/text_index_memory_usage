import asyncio

from models import Doc, init


async def main():
    await init()
    res = await Doc.aggregate(
        [
            {
                "$match": {
                    "$expr": {
                        "$eq": ["$tag", "8"]
                    },
                    "$text": {"$search": "good"}
                }
            },
            {
                "$limit": 10
            }
        ]
    ).to_list()

    print(res)


asyncio.run(main())
