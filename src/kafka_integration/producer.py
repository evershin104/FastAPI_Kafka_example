from aiokafka import AIOKafkaProducer
import asyncio
from settings import CONFIG

event_loop = asyncio.get_event_loop()

class AIOWebProducer:
    """Standard Producer. Lives as long as there's something to send"""
    def __init__(self):
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=CONFIG.KAFKA_BOOTSTRAP_SERVERS,
            loop=event_loop,
        )
        self.__produce_topic = CONFIG.TOPIC

    async def init_connection(self) -> None:
        await self.__producer.start()

    async def close_connection(self) -> None:
        await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        await self.init_connection()
        try:
            await self.__producer.send(
                topic=self.__produce_topic,
                value=value,
            )
        finally:
            await self.close_connection()

def get_producer() -> AIOWebProducer:
    """Returns producer instance

    Returns:
        AIOWebProducer: producer instance
    """
    return AIOWebProducer()
