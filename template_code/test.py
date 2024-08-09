import aiohttp
import asyncio
import json
import logging
import os
import pandas as pd

async def generate(lst_text):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for text in lst_text:
            await call_api(text, session)
        

async def call_api(text, session: aiohttp.ClientSession):
    try:
        # Simulate a call to the API
        async with session.get("http://127.0.0.1:1234") as response:
            if response.status == 200:
                data = await response.json()
                # Handle the response data
                print(data)  # or do something else with it
            else:
                logging.error(f"Request failed: {response.status}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

async def main():
    # Load data
    df = pd.read_csv('test.csv')
    lst_text = df['text'].tolist()
    task = asyncio.create_task(generate(lst_text))
    await task
    
if __name__ == '__main__':
    asyncio.run(main())


