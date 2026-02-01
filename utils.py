# utils.py
def format_poll_options(options):
    """
    Format poll options for inline keyboard
    """
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    keyboard = []
    for opt in options:
        keyboard.append([InlineKeyboardButton(text=opt, callback_data=opt)])
    return InlineKeyboardMarkup(keyboard)
