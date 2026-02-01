from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from config import BOT_TOKEN, SUPER_ADMINS, WORKER_API_URL
from commands import polls, votes, admin
import threading
import requests
import time

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# -------- Example command: /startpoll --------
def startpoll(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    question = " ".join(context.args)
    options = ["Option 1", "Option 2"]  # later make dynamic
    result = polls.start_poll(chat_id, question, options, user_id)
    update.message.reply_text(f"Poll created with ID {result.get('poll_id')}")

# -------- Example: Voting callback --------
def vote_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data.split(":")  # e.g., "pollID:option"
    poll_id, option = int(data[0]), data[1]
    result = votes.submit_vote(poll_id, user_id, option)
    query.answer(text=f"Vote recorded: {option}")

dispatcher.add_handler(CommandHandler("startpoll", startpoll))
dispatcher.add_handler(CallbackQueryHandler(vote_callback))

# -------- Keep-alive function (every 14 min) --------
def keep_alive():
    while True:
        try:
            requests.get(f"{WORKER_API_URL}/ping")  # Worker API ping
            print("[KeepAlive] Ping sent to Worker API")
        except Exception as e:
            print("[KeepAlive] Ping failed:", e)
        time.sleep(14 * 60)  # 14 minutes

# Run keep_alive in background
threading.Thread(target=keep_alive, daemon=True).start()

# -------- Start the Bot --------
updater.start_polling()
updater.idle()
