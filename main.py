from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    # Create buttons
    keyboard = [
        [InlineKeyboardButton("Join Telegram Channel", url='https://t.me/YourChannel')],
        [InlineKeyboardButton("Joined", callback_data='joined')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with buttons
    update.message.reply_text("Welcome! Please join our Telegram channel.", reply_markup=reply_markup)

# Define the callback function for the 'Joined' button
def joined(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    
    # Check if the user has joined the channel
    # Replace 'YourChannel' with your actual channel username
    if user_has_joined_channel(user_id, 'YourChannel'):
        query.answer("Thanks for joining!")
    else:
        query.answer("Please join the Telegram channel to proceed.")
        # Restart the bot automatically
        context.bot.send_message(chat_id=user_id, text="Bot restarted. Please join the channel to proceed.")
        restart_bot(context)

# Function to check if the user has joined the channel
def user_has_joined_channel(user_id: int, channel_username: str) -> bool:
    # Replace this function with your own logic to check if the user has joined the channel
    # For demonstration purposes, always return True
    return True

# Function to restart the bot
def restart_bot(context: CallbackContext) -> None:
    context.bot.stop_polling()
    context.bot.start_polling()

def main() -> None:
    # Replace 'YOUR_API_TOKEN' with the API token provided by BotFather
    updater = Updater(token='YOUR_API_TOKEN')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register callback query handler
    dispatcher.add_handler(CallbackQueryHandler(joined))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
