from pydantic import BaseModel, ConfigDict
from datetime import datetime, timezone
import uuid


class Attack(BaseModel):
    timestamp: str = datetime.now(timezone.utc).isoformat()
    attack_id:  str = str(uuid.uuid4())
    entity_id: str
    result: str
