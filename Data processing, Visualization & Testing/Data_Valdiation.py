import requests
from pydantic import BaseModel, ValidationError


response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

try:
    validated = Post(**data)
    print("Validated post:", validated)
except ValidationError as e:
    print("Validation error:", e)
