from fastapi import FastAPI
from web.ticket import router as ticket_router
from security.security import router as security_router

app = FastAPI()

app.include_router(ticket_router)
app.include_router(security_router);

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
