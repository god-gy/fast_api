import uuid

from app.apis.utils.base62 import Base62
from app.tortoise_models.meeting import MeetingModel


async def service_create_meeting_mysql() -> MeetingModel:
    return await MeetingModel.create_meeting(Base62.encode(uuid.uuid4().int))


async def service_get_meeting_mysql(url_code: str) -> MeetingModel:
    return await MeetingModel.get_by_url_code(url_code)
