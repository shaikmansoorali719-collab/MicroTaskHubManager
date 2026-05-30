from pydantic import BaseModel

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    retypepassword: str

class SigninSchema(BaseModel):
    username: str
    password: str
    
class UserSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status: int