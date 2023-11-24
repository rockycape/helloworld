# import json
# import pydantic    
from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id:int
    
@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value
    
user = User(name="jack", email="jack@jack.com", account_id=1234)
print(user)
user_json_str = user.model_dump_json()
print(user_json_str)
json_str = '{"name': "jack, "email": "jack@jack.com", "account_id": 1234}'
user = User.parse_raw(json_str)