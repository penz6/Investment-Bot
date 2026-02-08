#imports
from chatterbot import ChatBot
from importlib.metadata import version

def main():
    #init
    print("Starting")
    print("Using Chatterbot Version: ", version("Chatterbot"))
    #create the bot
    chatbot = ChatBot(
    'Investment God',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///my_bot_data.sqlite3')
