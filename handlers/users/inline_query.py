import hashlib

from aiogram import types

from loader import dp


@dp.inline_handler()
async def inline_mode(inline_query: types.InlineQuery):
    result = types.InlineQueryResultArticle(
        id='.',
        title=f'Your User ID: {inline_query.from_user.id}',
        description='Send it to the current chat',
        input_message_content=types.InputTextMessageContent(
            message_text=f'My <b>User ID</b>: <code>{inline_query.from_user.id}</code>'
        )
    )
    await inline_query.answer(
        results=[result],
        cache_time=1,
        is_personal=True,
        switch_pm_parameter='1',
        switch_pm_text='Go to Bot 👉'
    )
