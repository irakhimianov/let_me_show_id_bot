from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from sqlalchemy.ext.asyncio import AsyncSession


class DBMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['error', 'update']

    def __init__(self, session: AsyncSession):
        super().__init__()
        self.session = session

    async def pre_process(self, obj, data, *args):
        data['session'] = self.session

    async def post_process(self, obj, data, *args):
        session: AsyncSession = data.get('session')
        await session.close()
