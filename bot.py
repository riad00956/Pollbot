from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from config import BOT_TOKEN, SUPER_ADMINS
from commands import polls, votes, admin

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

updater.start_polling()
updater.idle()
