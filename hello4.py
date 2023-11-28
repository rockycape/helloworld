from pydantic import BaseModel, EmailStr, field_validator

class UserModel(BaseModel):
    name: str
    email: EmailStr
    account_id:int

print(
    UserModel(
        name='Apple',
        email='apple@apple.com',
        account_id=1234,
    )
)