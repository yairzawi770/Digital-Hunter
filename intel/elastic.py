from elasticsearch import Elasticsearch, helpers

from students_part_1.simulator import _connect_producer
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

es = Elasticsearch(["http://localhost:9200"])
if es.ping():
    logger.info("connected")
else:
    logger.info("faild to connect")

index_name = "intel"
mapping = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "signal_id": {"type": "keyword"},
            "entity_id": {"type": "keyword"},
            "reported_lat": {"type": "integer"},
            "reported_lon": {"type": "integer"},
            "signal_type": {"type": "text"},
            "priority_level": {"type": "integer"},
        }
    }
}
es.indices.create(index=index_name, body=mapping)

data = _connect_producer()

actions = []
for item in data:
    doc_id = item["signal_id"]
    doc_body = item.copy()
    del doc_body["signal_id"]
    actions.append({
        "_index": index_name,
        "_id": doc_id, 
        "_source": doc_body
    })
    
helpers.bulk(es, actions)
