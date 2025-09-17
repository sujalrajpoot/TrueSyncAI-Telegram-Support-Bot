# ================================
# bot/handlers/commands.py
# ================================

import logging
from telegram import Update
from telegram.ext import ContextTypes
from config.messages import (
    GUIDELINES_TEXT, COMMANDS_LIST, ABOUT_MESSAGE, CONTACT_MESSAGE
)
from config.settings import ADMIN_IDS, SYSTEM_PROMPT
from telegram.constants import ParseMode
# from bot.keyboards.inline import get_main_menu_keyboard
from bot.utils.decorators import admin_required
import json
import random
import requests
from typing import Union

def generate_response(prompt:str, timeout:int=60, model:str="meta-llama/Llama-3.3-70B-Instruct-Turbo", system_prompt:str=SYSTEM_PROMPT) -> Union[str, None]:
    url = "https://api.deepinfra.com/v1/openai/chat/completions"
    # Browser fingerprinting components
    FINGERPRINTS = {
        "accept_language": [
            "en-US,en;q=0.9", 
            "en-GB,en;q=0.8,en-US;q=0.6", 
            "es-ES,es;q=0.9,en;q=0.8",
            "fr-FR,fr;q=0.9,en;q=0.8", 
            "de-DE,de;q=0.9,en;q=0.8"
        ],
        "accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
        ]
    }
    # Use the fingerprint for headers (keep relevant ones)
    headers = {
        "Accept": random.choice(FINGERPRINTS["accept"]),
        "Accept-Language": random.choice(FINGERPRINTS["accept_language"]),
        "Content-Type": "application/json",
        "Cache-Control": "no-cache", # Keep Cache-Control
        "Origin": "https://deepinfra.com", # Keep Origin
        "Pragma": "no-cache", # Keep Pragma
        "Referer": "https://deepinfra.com/", # Keep Referer
        "Sec-Fetch-Dest": "empty", # Keep Sec-Fetch-*
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "X-Deepinfra-Source": "web-embed", # Keep custom headers
    }

    # Payload construction
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt.strip()},
        ],
        "stream": False
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            timeout=timeout,
        )
        response.raise_for_status() # Check for HTTP errors
        return response.json().get("choices", [{}])[0].get("message", {}).get("content")
    except: None

# Setup logging
logger = logging.getLogger(__name__)

async def handle_mentions(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle when bot is mentioned in messages"""
        if not update.message or not update.message.text:
            return

        message_text = update.message.text
        bot_username = f"@{context.bot.username}"
        
        # Check if bot is mentioned
        if bot_username.lower() in message_text.lower():
            user = update.effective_user
            
            # Extract the message after the bot mention
            user_message = message_text.replace(bot_username, "").strip()
            user_username = user.username or "Member has no username"
            user_id = user.id or "Member has no ID"
            user_first_name = user.first_name or "Member has no first name"
            user_last_name = user.last_name or "Member has no last name"
            user_type = "Admin" if user_id in ADMIN_IDS else "User"
            if not user_message:
                if user_id in ADMIN_IDS:
                    logger.info(f"Admin @{user_username} mentioned the bot without a message.")
                else:
                    logger.info(f"@{user_username} mentioned the bot without a message.")
                response = f"""
👋 Hello {user.first_name}! 

You mentioned me but didn't ask anything specific. Here's how you can interact with me:

**🔥 Quick Actions:**
• `/help` - Get comprehensive help
• `/rules` - View group rules
• `/commands` - See all available commands

**💬 Ask me anything:**
`@{context.bot.username} your question here`

*What can I help you with today?*
                """
            else:
                if user_id in ADMIN_IDS:
                    logger.info(f"Admin @{user_username} mentioned the bot: {user_message[:70]}...")
                else:
                    # Log user mention
                    logger.info(f"@{user_username} mentioned the bot: {user_message[:70]}...")  # Log first 70 chars for brevity
            try:
                # Generate contextual response based on user message
                response = await send_response(user_message, user_first_name, user_type)
                await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
                logger.info(f"Replied to {user_type} @{user_username} Message: {response[:70]}...\n")  # Log first 70 chars for brevity
            except Exception as e:
                logger.error(f"Error responding to mention: {e}")

async def send_response(user_message: str, user_name: str, user_type:str = "User") -> str:
    """Generate contextual responses to user messages"""
    reply = generate_response(prompt=f"{user_type}: {user_name}\nMessage: {user_message}")
    return reply or "Sorry, I couldn't process your request. Please try again later."

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    logger.info(f"User @{update.effective_user.username} started the bot.")
    # Send a welcome message with bot's purpose
    user = update.effective_user
    welcome_text = f"""
👋 Hello *{user.first_name}*!

I'm the group welcome bot, here to help make our community awesome! 🌟

🤖 *What I can do:*
• Welcome new members warmly
• Provide group guidelines and rules
• Show available commands
• Help with group information

Use the buttons below or type /help to get started!
    """
    
    await update.message.reply_text(
        welcome_text,
        # reply_markup=get_main_menu_keyboard(),
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    logger.info(f"User @{update.effective_user.username} requested help.")
    # Provide a list of all available commands
    await update.message.reply_text(
        COMMANDS_LIST,
        parse_mode='Markdown',
        # reply_markup=get_main_menu_keyboard()
    )

async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /rules command"""
    logger.info(f"User @{update.effective_user.username} requested group rules.")
    # Provide group rules
    await update.message.reply_text(
        GUIDELINES_TEXT,
        parse_mode='Markdown'
    )

async def commands_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /commands command"""
    logger.info(f"User @{update.effective_user.username} requested commands list.")
    # Provide a list of all available commands  
    await update.message.reply_text(
        COMMANDS_LIST,
        parse_mode='Markdown'
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /about command"""
    logger.info(f"User @{update.effective_user.username} requested about information.")
    # Provide information about the group
    await update.message.reply_text(
        ABOUT_MESSAGE,
        parse_mode='Markdown'
    )

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /contact command"""
    logger.info(f"User @{update.effective_user.username} requested contact information.")
    # Provide contact information for admins
    await update.message.reply_text(
        CONTACT_MESSAGE,
        parse_mode='Markdown'
    )

async def announcement_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /announcement command"""
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    if context.args:
        user_announcement_text = " ".join(context.args)
        logger.info(f"Admin @{update.effective_user.username} is making an announcement: {user_announcement_text[:70]}...")
        announcement = generate_response(prompt=f"Make an announcement about this given topic on behalf of Admin: {user_announcement_text}")
        # await update.message.reply_text(announcement, parse_mode=ParseMode.MARKDOWN)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"📢 *Announcement from @{update.effective_user.username}:*\n\n{announcement}",
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"Announcement sent by @{update.effective_user.username}: {user_announcement_text[:70]}...")  # Log first 70 chars for brevity
    else:
        await update.message.reply_text("Please provide an announcement message after the command. Only admins can use this command.")
