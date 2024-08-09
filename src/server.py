import asyncio

from fastapi import FastAPI
from fastapi import Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Note: the route decorator must be above the limit decorator, not below it
@app.get("/")
@limiter.limit("100/1 second")
async def homepage(request: Request):
    await asyncio.sleep(2)
    return {"message": "Hello World"}