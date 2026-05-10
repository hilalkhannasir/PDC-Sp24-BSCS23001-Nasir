from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge,webhooks
app = FastAPI()



class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-Student-ID"] = "BSCS23001"
        return response

app.add_middleware(CustomMiddleware)

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(challenge.router,prefix="/api")
app.include_router(webhooks.router,prefix="/webhooks")