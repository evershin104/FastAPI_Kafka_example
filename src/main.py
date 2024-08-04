from fastapi import FastAPI, Depends
import json
import asyncio
from contextlib import asynccontextmanager
import logging

from serializers.kafka_messages import KafkaMessage
from kafka_integration import AIOWebProducer, get_producer, consume

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Get FastAPI context manager to run 
        consumers via task
    Args:
        app (FastAPI)
    """
    loop = asyncio.get_event_loop()
    consumer_task = loop.create_task(consume(topic='registration'))
    yield

    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        pass


app = FastAPI(lifespan=lifespan)


@app.post("/")
async def send(
        message: KafkaMessage, 
        producer: AIOWebProducer = Depends(get_producer)
    ) -> None:
    """Example of API which recieves a message and 
        sends it to consumer
    Args:
        message (KafkaMessage): message with KafkaMessage structure
        producer (AIOWebProducer, optional): Producer instance. 
            Defaults to Depends(get_producer).
    """
    message_to_produce = json.dumps(message.model_dump()).encode(encoding="utf-8")
    await producer.send(value=message_to_produce)

