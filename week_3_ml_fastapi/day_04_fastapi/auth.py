# Dependency Injection
# JWT
# Password Hashing
# Protected Routes
# Background Tasks


from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    BackgroundTasks
)

from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

users = {}
tasks = []

class User(BaseModel):
    username: str
    password: str

def send_welcome_email(username):

    print(
        f"Welcome email sent to {username}"
    )

def create_token(username):

    return jwt.encode(
        {"sub": username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload["sub"]

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

@app.post("/register")
def register(
    user: User,
    bg_tasks: BackgroundTasks
):

    hashed_password = pwd_context.hash(
        user.password
    )

    users[user.username] = hashed_password

    bg_tasks.add_task(
        send_welcome_email,
        user.username
    )

    return {
        "message": "User Registered"
    }

@app.post("/login")
def login(user: User):

    stored_password = users.get(
        user.username
    )

    if not stored_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    if not pwd_context.verify(
        user.password,
        stored_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    token = create_token(
        user.username
    )

    return {
        "access_token": token
    }

@app.post("/tasks")
def create_task(
    task: str,
    token: str
):

    username = verify_token(token)

    tasks.append({
        "task": task,
        "owner": username
    })

    return {
        "message": "Task added"
    }

@app.get("/tasks")
def get_tasks(token: str):

    username = verify_token(token)

    return [
        task
        for task in tasks
        if task["owner"] == username
    ]