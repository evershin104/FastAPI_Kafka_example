from pydantic import BaseModel


class KafkaMessage(BaseModel):
    """Default message serializer"""
    body: str
    id: int
