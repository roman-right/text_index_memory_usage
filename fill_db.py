import asyncio

import pymongo

from models import init, Doc


async def main():
    await init()

    # any big text file here. I use "20000 leagues under the sea"
    with open("book.txt", "r") as f:
        text = f.read()

    docs = []
    counter = 1
    inserted = 0
    page_size = 20000
    for i in range(380000):
        if counter + page_size > len(text):
            counter = 1
        doc = Doc(
            text=text[counter:counter + page_size],
            tag=str(i % 10)
        )
        counter += page_size

        docs.append(doc)

        if len(docs) == 100:
            await Doc.insert_many(documents=docs)
            docs = []
            inserted += 100
            print(f"Inserted: {inserted}")

    Doc.get_motor_collection().create_index([("text", pymongo.TEXT)])


asyncio.run(main())
