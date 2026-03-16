import json
from kafka import KafkaConsumer
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

def connect_consumer(topic, bootstrap_servers: str):
        consumer = KafkaConsumer(topic, 
                                group_id='consumer', 
                                bootstrap_servers=[bootstrap_servers], 
                                auto_offset_reset='latest', 
                                value_deserializer=lambda m:json.loads(m.decode('utf-8')), 
                                max_poll_interval_ms=900000)



        consumer = KafkaConsumer(consumer)

        consumer.subscribe(["intel"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    logger.info("❌ Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")
                intel = json.loads(value)
                logger.info("recive topic", intel)
        except KeyboardInterrupt:
            logger.info("\n🔴 Stopping consumer")

        finally:
            consumer.close()