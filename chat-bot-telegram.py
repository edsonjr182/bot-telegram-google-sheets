import os
import datetime
import random
import logging
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update, ForceReply, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from telegram.ext import DispatcherHandlerStop
from google.oauth2 import service_account
from googleapiclient.discovery import build




# Ative o logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


# Credenciais do Google Sheets
SERVICE_ACCOUNT_FILE = 'keys/arquivo_chaves.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE).with_scopes(SCOPES)


# IDs das planilhas do Google Sheets
MOTIVATIONAL_QUOTES_SPREADSHEET_ID = '1cejP_qNU1oIAvODlo2v5ENcMtCmNk0IQshcNCgrRA6I'
BANNED_WORDS_SPREADSHEET_ID = '1_Upek2ISUcVais4v6m-fREjb0vxh2e90rU-UYzFyHMU'
MEMBERS_SPREADSHEET_ID = '1O23oBTFMZHW_jkEmyxIgme7zTYt-ETB1CT6wftiRDsI'

# Inicialize a API do Google Sheets
sheets_api = build('sheets', 'v4', credentials=creds)

# Token do bot do Telegram
TELEGRAM_API_TOKEN = '5927484467:AAEscLY8ucuyDgN5nPi5zWEwGAoSC86SI-g'







def main() -> None:
    updater = Updater(TELEGRAM_API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))  # Removendo Filters.chat_type.groups
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    dispatcher.add_handler(CallbackQueryHandler(handle_inline_button))




    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
