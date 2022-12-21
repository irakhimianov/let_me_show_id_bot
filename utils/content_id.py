from aiogram import types


def get_content_id(message: types.Message) -> str:
    content_id = ''
    if message.animation:
        content_id = f'🖼 <b>Animation ID</b>: <code>{message.animation.file_id}</code>'
    elif message.audio:
        content_id = f'🔊 <b>Audio ID</b>: <code>{message.audio.file_id}</code>'
    elif message.document:
        content_id = f'📂 <b>Document ID</b>: <code>{message.document.file_id}</code>'
    elif message.location:
        content_id = f'📍 <b>Location ID</b>:\n ' \
                     f'latitude: <code>{message.location.latitude} ' \
                     f'longtitude: <code>{message.location.longitude}</code>'
    elif message.photo:
        content_id = f'🖼 <b>Photo ID</b>: <code>{message.photo[-1].file_id}</code>'
    elif message.poll:
        content_id = f'👥 <b>Poll ID</b>: <code>{message.poll.id}</code>'
    elif message.sticker:
        content_id = f'💬 <b>Sticker ID</b>: <code>{message.sticker.file_id}</code>'
    elif message.video:
        content_id = f'🎥 <b>Video ID</b>: <code>{message.video.file_id}</code>'
    elif message.voice:
        content_id = f'📢 <b>Voice ID</b>: <code>{message.voice.file_id}</code>'
    return content_id
