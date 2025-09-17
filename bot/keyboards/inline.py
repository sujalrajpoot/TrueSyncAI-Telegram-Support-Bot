# ================================
# bot/keyboards/inline.py
# ================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_welcome_keyboard():
    """Get welcome message inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📋 View Rules", callback_data="rules"),
            InlineKeyboardButton("🤖 Commands", callback_data="commands")
        ],
        [
            InlineKeyboardButton("ℹ️ About Group", callback_data="about"),
            InlineKeyboardButton("📞 Contact", callback_data="contact")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_main_menu_keyboard():
    """Get main menu inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📋 Rules", callback_data="rules"),
            InlineKeyboardButton("🤖 Commands", callback_data="commands")
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("📞 Contact", callback_data="contact")
        ],
        [
            InlineKeyboardButton("🔄 Refresh", callback_data="refresh")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_keyboard():
    """Get admin panel inline keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("📊 Statistics", callback_data="admin_stats"),
            InlineKeyboardButton("💬 Messages", callback_data="admin_messages")
        ],
        [
            InlineKeyboardButton("👥 Users", callback_data="admin_users"),
            InlineKeyboardButton("⚙️ Settings", callback_data="admin_settings")
        ],
        [
            InlineKeyboardButton("🔙 Back to Main", callback_data="main_menu")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
