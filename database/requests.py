from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy import select

from database import User


async def get_user(user_id: int, session: AsyncSession) -> User:
    user = await session.get(User, user_id)
    return user


async def get_users(*, session: AsyncSession) -> ChunkedIteratorResult:
    users = await session.execute(select(User))
    return users.scalars().all()


async def add_user(
        *,
        user_id: int,
        session: AsyncSession
):
    user = await get_user(user_id=user_id, session=session)
    if user is None:
        user = User(user_id=user_id)
        session.add(user)
        await session.commit()


async def update_user(
        user_id: int,
        session: AsyncSession,
        **kwargs
):
    user = await get_user(user_id=user_id, session=session)
    [setattr(user, key, value) for key, value in kwargs.items()]
    session.add(user)
    await session.commit()
