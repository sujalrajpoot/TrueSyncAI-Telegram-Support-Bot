# ================================
# bot/utils/decorators.py
# ================================

from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from config.settings import ADMIN_IDS

def admin_required(func):
    """Decorator to restrict access to admin users only"""
    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        
        if user_id not in ADMIN_IDS:
            await update.message.reply_text(
                "🚫 Access denied. This command is for administrators only."
            )
            return
            
        return await func(update, context)
    return wrapper
