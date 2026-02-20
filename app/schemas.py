from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# class Post(BaseModel):
#     id: str
#     caption: Optional[str] = None
#     url: str
#     file_type: str
#     file_name: str
#     created_at: datetime

class Post(BaseModel):
    content: str
    title: str