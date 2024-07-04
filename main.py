import os
from typing import Final

import mysql.connector
from discord import Intents, Client, Message
from dotenv import load_dotenv

from responses import get_response

# Load the Token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_BOT_TOKEN")

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
bot: Client = Client(intents=intents, command_prefix=".")

# Database Setup
HOST: Final[str] = os.getenv("DB_HOST", "localhost")
USER: Final[str] = os.getenv("DB_USER", "root")
DATABASE: Final[str] = os.getenv("DATABASE", "dungeons_and_dragons")
PASSWORD: Final[str] = os.getenv("DB_PASSWORD", "")
mydb = None


# Message Functionality
async def send_message(message: Message, user_message: str):
    if not user_message:
        print('Message was empty, intents were probably not enabled')
        return

    # := is the Walrus operator, it's just doing this in one line is_private = user_message[0] == "?"
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message.lower(), mydb, message.author)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Handle the startup for the bot
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    global mydb
    mydb = get_mysql_connection()


# Handle incoming message
@bot.event
async def on_message(message: Message):
    # The bot is the one who wrote the message, avoiding an endless loop
    if message.author == bot.user:
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    if user_message[0] != "#":
        return

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message[1:])


# Connect to database
def get_mysql_connection():
    global mydb
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        database=DATABASE,
        password=PASSWORD
    )
    if mydb.is_connected():
        print("Connected to MySQL!")
    return mydb


if __name__ == '__main__':
    bot.run(token=TOKEN)
