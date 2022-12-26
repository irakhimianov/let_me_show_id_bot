import logging
from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                      CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter, MessageCantBeEdited,
                                      CantParseEntities, MessageCantBeDeleted, MessageToEditNotFound,
                                      ChatNotFound, ChatIdIsEmpty)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, CantDemoteChatCreator):
        logging.exception("Can't demote chat creator")
        return True

    if isinstance(exception, MessageNotModified):
        logging.exception('Message is not modified')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.exception('Message cant be deleted')
        return True

    if isinstance(exception, MessageCantBeEdited):
        logging.exception('Message cant be edited')
        return True

    if isinstance(exception, MessageToEditNotFound):
        logging.exception('Message to edit not found')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.exception('Message to delete not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception('MessageTextIsEmpty')
        return True

    if isinstance(exception, Unauthorized):
        logging.exception(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, ChatNotFound):
        logging.exception(f'Chat not found: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, ChatIdIsEmpty):
        logging.exception(f'Chat id is empty: {exception} \nUpdate: {update}')
        return True


    logging.exception(f'Update: {update} \n{exception}')
