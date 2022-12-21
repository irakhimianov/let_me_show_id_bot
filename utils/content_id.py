from aiogram import types


def get_content_id(message: types.Message) -> str:
    content_id = ''
    if message.animation:
        content_id = f'🖼 <b>Animation ID</b>:\n <code>{message.animation.file_id}</code>'
    elif message.audio:
        content_id = f'🔊 <b>Audio ID</b>:\n <code>{message.audio.file_id}</code>'
    elif message.document:
        content_id = f'📂 <b>Document ID</b>:\n <code>{message.document.file_id}</code>'
    elif message.location:
        content_id = f'📍 <b>Location ID</b>:\n ' \
                     f'latitude: <code>{message.location.latitude} ' \
                     f'longtitude: <code>{message.location.longitude}</code>'
    elif message.photo:
        content_id = f'🖼 <b>Photo ID</b>:\n <code>{message.photo[-1].file_id}</code>'
    elif message.poll:
        content_id = f'👥 <b>Poll ID</b>:\n <code>{message.poll.id}</code>'
    elif message.sticker:
        content_id = f'💬 <b>Sticker ID</b>:\n <code>{message.sticker.file_id}</code>'
    elif message.video:
        content_id = f'🎥 <b>Video ID</b>:\n <code>{message.video.file_id}</code>'
    elif message.voice:
        content_id = f'📢 <b>Voice ID</b>:\n <code>{message.voice.file_id}</code>'
    return content_id
