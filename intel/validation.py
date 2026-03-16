from pydantic import BaseModel, ConfigDict
from datetime import datetime, timezone
import uuid


class Intel(BaseModel):
    timestamp: str = datetime.now(timezone.utc).isoformat()
    signal_id: str = str(uuid.uuid4())
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int