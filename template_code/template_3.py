import aiohttp
import asyncio
import json
import logging
import os
import pandas as pd

async def generate(lst_text):
    async with aiohttp.ClientSession() as session:
        tasks = set()
        n_concurrent = 2
        for text in lst_text:
            if len(tasks) >= n_concurrent:
                _, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            tasks.add(asyncio.create_task(call_api(text, session)))
        
        
        await asyncio.wait(tasks)
        


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


if __name__ == '__main__':
    # Load data
    df = pd.read_csv('test.csv')
    lst_text = df['text'].tolist()

    import time
    start = time.time()
    asyncio.run(generate(lst_text))
    print(f"Time taken: {time.time() - start}")