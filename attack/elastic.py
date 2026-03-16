from elasticsearch import Elasticsearch, helpers

from students_part_1.simulator import _connect_producer

es = Elasticsearch(["http://localhost:9200"])
if es.ping():
    print("connected")
else:
    print("faild to connect")

index_name = "attack"
mapping = {
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "attack_id": {"type": "keyword"},
            "entity_id": {"type": "keyword"},
            "weapon_type": {"type": "text"},
        }
    }
}
es.indices.create(index=index_name, body=mapping)

data = _connect_producer()

actions = []
for item in data:
    doc_id = item["attack_id"]
    doc_body = item.copy()
    del doc_body["attack_id"]
    actions.append({
        "_index": index_name,
        "_id": doc_id, 
        "_source": doc_body
    })
    
helpers.bulk(es, actions)