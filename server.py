import aiohttp
import asyncio

origin = 'http://127.0.0.1:8000/'
async def edge_server():
    async with aiohttp.ClientSession() as session:
        async with session.get(origin) as response:
            