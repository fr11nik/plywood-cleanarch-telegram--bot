from datetime import datetime
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters,CallbackQueryHandler
from handler.telegram_bot.handler import Handler
from use_case.interfaces import UseCase
from domain.entity.user_position import Position 
from domain.entity.user import User
from enum import StrEnum
import re



class Commands(StrEnum):
    Start = "start"
    Register = "Зарегистрироваться"
    RegisterIdentificationCodeRegex = r'^plwd_token:.{198}$'
    RegisterEmployeeRegex = r'1\. \b7\d{10}\b\n2\. \b\d{4}-\d{2}-\d{2}\b\n3\. plwd_token:.{198}'
    AmCustomer = "Я заказчик"



class ReplyMessages(StrEnum):
    PleaseInsertYourIdentificationCode = "Введите ваш идентификационный код. получить его можно у администрации"
    WelcomeMessage = "Вам доступны следующие функции:"
    NotCorrectTryAgain = "Код не верный повторите попытку"

class V1Handler(Handler):
    """Handler that handle commands"""

    def init(self,uc:UseCase):
        self.uc = uc

    def AddRoutes(self,app:Application):
        """Init handle routes"""
        app.add_handler(CommandHandler(Commands.Start, callback=
                                       self._start))
        app.add_handler(MessageHandler(filters.Regex(pattern=Commands.Register),
                                       callback=self._register_user))
        app.add_handler(MessageHandler(filters.Regex(pattern=Commands.RegisterEmployeeRegex),
                                       callback=self._register_empoyee))
        app.add_handler(MessageHandler(filters.Regex(re.compile(Commands.RegisterIdentificationCodeRegex)),
                                       callback=self._insert_code))
        app.add_handler(CallbackQueryHandler(pattern="^" + Commands.AmCustomer + "$",
                                             callback=self._register_customer))
        app.add_handler(CallbackQueryHandler(pattern="^" + Commands.Register + "$",
                                             callback=self._register_user))

    async def _start(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        ## check user is exists else ask user to register 

        response = self.uc.get_welcome_message().text

        tg_usr = update.effective_user
        usr = self.uc.get_user_by_id(tg_usr.id)
        if usr == None:
            keyboard = [
                [
                    InlineKeyboardButton("Зарегистрироваться", callback_data=str(Commands.Register)),
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(response, reply_markup=reply_markup)
            return  

        await update.message.reply_text(f"Welcome {usr}")


    async def _register_user(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        query = update.callback_query

        await query.answer()

        keyboard = [
            [
                InlineKeyboardButton("Я заказчик", callback_data=str(Commands.AmCustomer)),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            'Для регистрации необходимо указать следующие данные: \n'
            '1. Номер телефона (в формате 7xxxxxxxxxx)\n'
            '2. Дата рождения (в формате гггг-мм-дд)\n'
            '3. Идентификационный код\n',reply_markup=reply_markup
            )
   
    async def _register_empoyee(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        # Регулярное выражение для номера телефона
        phone_pattern = r'\b7\d{10}\b'

        # Регулярное выражение для даты рождения
        date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'

        identificationCode_pattern = r'plwd_token:.{198}$'
        # Поиск совпадений
        phones = re.findall(phone_pattern, update.message.text)
        dates = re.findall(date_pattern, update.message.text)
        identidicationCode = re.findall(identificationCode_pattern,update.message.text)
        print(phones,dates,identidicationCode)

        identidication = self.uc.get_user_identification(identidicationCode[0])
        if identidication == None:
            await update.message.reply_text(ReplyMessages.NotCorrectTryAgain)
            return

        tg_usr = update.effective_user

        pos = Position(id=identidication.position.id,name=identidication.position.name)
        usr = User(tg_usr.id,tg_usr.first_name,tg_usr.last_name,
                   position=pos,phone_number=phones[0],birth_date=datetime.strptime(dates[0],"%Y-%m-%d"))
        self.uc.create_user(usr)

        await update.message.reply_text(f"{ReplyMessages.WelcomeMessage}. Добро пожаловать {tg_usr.full_name}")


    async def _register_customer(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Register customer in the system"""
        query = update.callback_query

        await query.edit_message_text(
            'Для регистрации необходимо указать следующие данные: \n'
            '1. Номер телефона (в формате 7xxxxxxxxxx)\n'
            '2. Дата рождения (в формате гггг-мм-дд)\n'
            '3. Наименование организации\n'
            '4. Электронная почта\n'
            )

    async def _insert_code(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        identidication = self.uc.get_user_identification(update.message.text)
        if identidication == None:
            await update.message.reply_text(ReplyMessages.NotCorrectTryAgain)
            return

        await update.message.reply_markdown_v2(
            '*Для регистрации необходимо указать следующие данные:* \n'
            '1\. Номер телефона (в формате 7xxxxxxxxxx)\n'
            '2\. Дата рождения (в формате гггг-мм-дд)\n'
            )

        tg_usr = update.effective_user

        pos = Position(id=identidication.position.id,name=identidication.position.name)
        usr = User(tg_usr.id,tg_usr.first_name,tg_usr.last_name,position=pos)
        ##self.uc.create_user(usr)

        ##await update.message.reply_text(f"{ReplyMessages.WelcomeMessage}. Добро пожаловать {tg_usr.full_name}")


