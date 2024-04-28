from main.models import *

from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

import os, django, logging, warnings, uuid
warnings.filterwarnings("ignore")

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


@sync_to_async
def user_get_by_update(update: Update):
    """
        Функция обработчик, возвращающая django instance пользователя
    """

    if update.message:
        message = update.message
    else:
        message = update.callback_query.message

    if not message.chat.username:
        username = "Anonymous"
    else:
        username = message.chat.username

    instance, created = CustomUser.objects.update_or_create(
        username = username,
        telegram_chat_id = message.chat.id,
    )

    token = Token.objects.get_or_create(user=instance)
    
    return instance, created, token[0].key

async def start(update: Update, context: CallbackContext) -> None:
    """
        Обработчик команды /start
    """
    usr, _, _ = await user_get_by_update(update)
    
    if usr.verified_usr:
        await context.bot.send_video(
            usr.telegram_chat_id,
            "https://media1.giphy.com/media/G3Hu8RMcnHZA2JK6x1/giphy.gif?cid=ecf05e47qybjqyrdm7j9unlomb839p3w2u2mloamu2lcx5qu&rid=giphy.gif&ct=g",
            caption=f"С возвращением, <b>{usr.username}</b> 😽\nДанные обновлены 💼",
            parse_mode="HTML",
        )
    else:

        await context.bot.send_message(
            usr.telegram_chat_id,
            f"<b>{usr.username}</b>, вы не зарегистрированы в нашей системе 😳\n\nДля того, чтобы зарегистрироваться, необходимо:\n⚫ <i>Нажать на кнопочку ниже</i>\n⚫ <i>Ответить на несколько вопросов</i>\n⚫ <i>Ожидать ответ администратора</i>",
            parse_mode="HTML",
        )

    return ConversationHandler.END

def main() -> None:
    """Run the bot."""

    application = Application.builder().token(os.environ.get("ACCOUNT_BOT_TOKEN")).build()
    
    application.add_handler(CommandHandler("start", start)) 
    application.add_handler(CallbackQueryHandler(start, "main_menu"))

    application.add_handler(MessageHandler("Меню 📥", start))

    application.run_polling()


class Command(BaseCommand):
    help = 'Команда запуска телеграм бота'

    def handle(self, *args, **kwargs):        
        main()

        
        
        
