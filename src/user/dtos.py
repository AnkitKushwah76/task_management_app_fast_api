from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    user_name: str
    password: str
    email: str

class UserResponseSchema(BaseModel):
    name: str
    user_name: str
    email: str
    id: int

class LoginSchema(BaseModel):
    user_name : str
    password : str