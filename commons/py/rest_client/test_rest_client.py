import asyncio
from unittest import IsolatedAsyncioTestCase, main
from commons.py.request.rest_client import RestClient


class TestRequest(IsolatedAsyncioTestCase):
    async def test_request(self):
        async with RestClient() as request:
            response = await request.get("https://dummy.restapiexample.com/api/v1/employees")
            self.assertEqual("test", response)

if __name__ == "__main__":
    main()
