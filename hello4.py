from typing import Annotated, Dict, List, Literal, Tuple

from annotated_types import Gt

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: EmailStr
    account_id:int


print(
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)