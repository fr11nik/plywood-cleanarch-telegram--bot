import logging
from telegram.ext import Application
from telegram import Update
from dataclasses import dataclass
from .handler import Handler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


@dataclass
class Bot:
    """Telegram bot"""
    app:Application

    def __init__(self,token:str):
        # Create the Application and pass it your bot's token.
        application = Application.builder().token(token).build()

        ## attach tg_bot_api to class
        self.app = application

    def WithHandler(self,h:Handler):
        ##init handler and attach routes
        h.AddRoutes(self.app)
        
    def Run(self):
        # Run the bot until the user presses Ctrl-C
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


