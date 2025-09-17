# ================================
# main.py
# ================================

import logging
from telegram import __version__ as TG_VER
# from telegram.error import NetworkError
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import BOT_TOKEN, SERVER_RESTART_INTERVAL
from bot.handlers.welcome import handle_new_members, handle_member_left
from bot.handlers.commands import (
    start_command, help_command, rules_command, 
    commands_command, about_command, contact_command, handle_mentions, announcement_command
)
from bot.handlers.admin import admin_panel
from bot.utils.logger import setup_logging

def main():
    """Main function to start the bot"""
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # Check Telegram version compatibility
    logger.info(f"Using Telegram API version: {TG_VER}")
    
    # Create application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules_command))
    app.add_handler(CommandHandler("commands", commands_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("contact", contact_command))
    app.add_handler(CommandHandler("announcement", announcement_command))
    app.add_handler(CommandHandler("admin", admin_panel))
    
    # Message handlers
    app.add_handler(MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS, 
        handle_new_members
    ))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_mentions))
    app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, handle_member_left))

    # Start polling
    logger.info("Starting bot...")
    app.run_polling(allowed_updates=["message", "chat_member"])
    
if __name__ == "__main__":
    main()
