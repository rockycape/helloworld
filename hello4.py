from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id:int

print(
    User(
        name='Apple',
        email='apple@apple.com',
        account_id=1234,
    )
)