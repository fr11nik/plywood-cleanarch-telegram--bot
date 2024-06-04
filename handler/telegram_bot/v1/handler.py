from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters
from handler.telegram_bot.handler import Handler
from use_case.interfaces import UseCase
from domain.entity.user import User

class V1Handler(Handler):
    """Handler that handle commands"""

    def init(self,uc:UseCase):
        self.uc = uc

    def AddRoutes(self,app:Application):
        """Init handle routes"""
        app.add_handler(CommandHandler("start", self._start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,self._echo))

    async def _start(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        ## check user is exists else ask user to register 

        response = self.uc.GetWelcomeMessage().text

        usr = update.effective_user
        usr = self.uc.get_user_by_id(usr.id)
        usr_identification = self.uc.get_user_identification('dfdfdwf13r3\kjp~_kjldf1')

        keyboard = [
            [
                InlineKeyboardButton("Зарегистрироваться", callback_data=str("Зарегистрироваться")),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        ##Send message with text and appended InlineKeyboard
        await update.message.reply_text(response, reply_markup=reply_markup)

    async def _echo(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(update.message.text)

