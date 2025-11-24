import asyncio
from twscrape import API, gather

async def main():
    api = API()

    # search (latest tab)
    data = await gather(api.search("bitcoin", limit=20))  # list[Tweet]
    print(data)

    # change search tab (product), can be: Top, Latest (default), Media
    data = await gather(api.search("bitcoin", limit=20, kv={"product": "Top"}))
    print(data)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)