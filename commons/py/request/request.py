import aiohttp


class Request():
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def get(self, url: str, headers: dict = None, params: dict = None) -> str:
        async with self.session.get(url, headers=headers, params=params) as response:
            print(response)

    async def post(self, url: str, params: dict = None, headers: dict = None) -> str:
        pass

    async def put(self, url: str, params: dict = None, headers: dict = None) -> str:
        pass
