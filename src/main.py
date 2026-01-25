from fastapi import Depends, status, FastAPI, HTTPException
from web.ticket import router as ticket_router
from starlette.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from security.security import (
    User,
    get_user_from_token,
    oauth2_scheme,
    UserInDB,
    fake_token_generator,
    fakely_hash_password,
    fake_users_db
)


app = FastAPI()

app.include_router(ticket_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)



@app.get("/users/me", response_model=User)
def read_users_me(
    current_user: User = Depends(get_user_from_token),
):
    return current_user

def get_user_from_token(
    token: str = Depends(oauth2_scheme),
) -> UserInDB:
    user = fake_token_resolver(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=(
                "Invalid authentication credentials"
            ),
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@app.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    
    user = UserInDB(**user_dict)
    hashed_password = fakely_hash_password(
        form_data.password
    )
    
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
        
    token = fake_token_generator(user)
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }
