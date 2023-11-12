import aiohttp


class RestClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()

    def validateResponse(self, response: aiohttp.ClientResponse) -> None:
        pass

    async def get(self, url: str, headers: dict = None, params: dict = None) -> str:
        async with self.session.get(url, headers=headers, params=params) as response:
            self.validateResponse(response)

            return await response.text()

    async def post(self, url: str, params: dict = None, headers: dict = None) -> str:
        async with self.session.post(url, headers=headers, params=params) as response:
            self.validateResponse(response)

            return await response.text()

    async def put(self, url: str, params: dict = None, headers: dict = None) -> str:
        async with self.session.put(url, headers=headers, params=params) as response:
            self.validateResponse(response)

            return await response.text()
