import aiohttp
import asyncio
import json
import logging
import os

async def generate(lst_text):
    tasks = []
    for text in lst_text:
        # create a session for each request
        async with aiohttp.ClientSession() as session:
            # call the API
            task = asyncio.create_task(call_api(text, session))
            tasks.append(task)
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

async def call_api(text, session: aiohttp.ClientSession):
    # simulate a call to the API
    await asyncio.sleep(2)
    print(text)

if __name__ == '__main__':
    # load data
    import pandas as pd
    df = pd.read_csv('test.csv')
    lst_text = df['text'].tolist()
    
    asyncio.run(generate(lst_text))