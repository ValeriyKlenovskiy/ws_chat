from sqlalchemy import insert, select

from app.database import async_session_maker
from app.chat.models import Messages

class ChatService:

    @classmethod
    async def get_last_messages(cls):
        async with async_session_maker() as session:
            query = select(Messages).order_by(Messages.id.desc()).limit(5)
            messages = await session.execute(query)
            return messages.mappings().all()

    @classmethod
    async def add_messages_to_database(cls, message: str):
        async with async_session_maker() as session:
            stmt = insert(Messages).values(message=message)
            await session.execute(stmt)
            await session.commit()
