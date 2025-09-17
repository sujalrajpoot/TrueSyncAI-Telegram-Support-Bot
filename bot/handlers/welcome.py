# ================================
# bot/handlers/welcome.py
# ================================

import logging
from telegram import Update
from telegram.error import Forbidden
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from config.messages import get_random_welcome_message, GUIDELINES_TEXT
# from bot.keyboards.inline import get_welcome_keyboard

logger = logging.getLogger(__name__)

async def handle_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle new members joining the group"""
    try:
        message = update.message
        new_members = message.new_chat_members
        
        for member in new_members:
            if member.is_bot:
                continue  # Skip bots
                
            # Get member's name
            name = f"{member.first_name} {member.last_name or ''}".strip()
            if not name:
                name = "New Member"
            
            if member.username:
                name = f"{name} (@{member.username})"
            
            # Create welcome message
            welcome_text = get_random_welcome_message().format(name=name)
            
            # Add quick guidelines preview
            quick_guidelines = """
            
🎯 *Quick Start Guide:*
• Read our /rules for complete guidelines
• Use /commands to see what I can help with
• Feel free to introduce yourself!
• Have fun and be respectful! 😊
            """
            
            full_message = welcome_text + quick_guidelines
            
            # # Send welcome message with inline keyboard
            # await message.reply_text(
            #     full_message,
            #     # reply_markup=get_welcome_keyboard(),
            #     parse_mode='Markdown'
            # )

            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=full_message,
                parse_mode=ParseMode.MARKDOWN
            )
            
            logger.info(f"Welcomed new member: {name} (ID: {member.id})")
            
    except Exception as e:
        logger.error(f"Error handling new members: {e}")

async def handle_member_left(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle when a member leaves the group."""
    try:
        message = update.message
        left_member = message.left_chat_member

        if left_member:
            # Get user details
            username = f"@{left_member.username}" if left_member.username else f"{left_member.first_name} {left_member.last_name or ''}".strip()
            chat_id = message.chat.id

            log_msg = f"{username} left the group. Chat ID: {chat_id}"
            update_text = f"👋 Hey {username}, we're sad to see you leave the group!\n\nIf it was a mistake or you ever want to come back, you’re always welcome. 💙"
            # await message.reply_text(update_text, parse_mode='Markdown')
            await context.bot.send_message(
                chat_id=chat_id,
                text=update_text,
                parse_mode=ParseMode.MARKDOWN
            )
            logger.info(log_msg)

    except Exception as e:
        logger.error(f"Error handling member leave event: {e}")
