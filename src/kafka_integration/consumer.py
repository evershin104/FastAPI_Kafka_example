import asyncio
import json
import logging 

from aiokafka import AIOKafkaConsumer

from settings import CONFIG

logger = logging.getLogger(__name__)


async def consume(topic: str) -> None:
    """Consume messages via Kafka by topics

    Args:
        topic (str): topic to consume
    """
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=CONFIG.KAFKA_BOOTSTRAP_SERVERS,
    )
    await consumer.start()
    logger.info(f"Consumer on '{topic}' started.")
    try:
        async for msg in consumer:
            serialized = json.loads(msg.value)
            logger.info(f"MSG ({topic}): '{serialized}'.")
    finally:
        await consumer.stop()
        logger.info(f"Consumer on '{topic}' started.")
