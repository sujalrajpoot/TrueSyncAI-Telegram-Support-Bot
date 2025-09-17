# ================================
# config/messages.py
# ================================

import random

# Welcome messages templates
WELCOME_MESSAGES = [
    "🎉 Welcome to our awesome group, *{name}!* We're thrilled to have you join our community! ✨",
    "🌟 Hey there *{name}!* Welcome aboard! Get ready for some amazing discussions and fun! 🎊",
    "🚀 Welcome *{name}!* You've just joined something special. Let's make great things happen together! 💫",
    "🌈 Hi *{name}!* Welcome to our wonderful community. We're excited to see what you'll bring to the group! 🎭",
    "🎪 Welcome *{name}!* Step right up and join the fun. Our group just got even better! 🎨"
]

# Guidelines text
GUIDELINES_TEXT = """
📋 *Group Guidelines & Rules*

🌟 *Welcome to our community!* Here are our guidelines to ensure everyone has a great experience:

✅ *Do's:*
• Be respectful and kind to all members
• Stay on topic with relevant discussions  
• Use appropriate language
• Help newcomers feel welcome
• Share valuable content and insights
• Use proper channels for different topics

❌ *Don'ts:*
• No spam, self-promotion without permission
• No offensive, hateful, or discriminatory content
• No sharing of personal information
• No excessive use of caps lock
• No off-topic discussions in focused channels
• No harassment or bullying

🛠️ *Available Commands:*
Use /commands to see all available bot commands

📞 *Need Help?*
Contact our admins using /contact

🎯 *Group Purpose:*
This group is dedicated to creating a positive, supportive community where members can share ideas, learn, and grow together.

Thank you for being part of our community! 🙌
"""

# Command descriptions
COMMANDS_LIST = """
🤖 *Available Bot Commands:*

🔹 /start - Get started with the bot
🔹 /help - Show this help message  
🔹 /rules - Display group guidelines
🔹 /commands - Show all available commands
🔹 /about - Learn about this group
🔹 /contact - Contact group administrators
🔹 /admin - Access the admin panel *(admins only)*
🔹 /announcement - Send announcements to the group *(admins only)*

💡 *Tip:* Click on any command to use it instantly!
"""

# About group message
ABOUT_MESSAGE = """
ℹ️ *About Our Group*

Welcome to our vibrant community! This group was created to bring together like-minded individuals who share common interests and goals.

🎯 *Our Mission:*
To foster meaningful discussions, share knowledge, and build lasting connections among our members.

👥 *What We Offer:*
• Engaging discussions on various topics
• Knowledge sharing and learning opportunities  
• Networking with amazing people
• Support and encouragement from the community
• Regular events and activities

📈 *Group Stats:*
• Founded: [Add your founding date]
• Active Members: Growing daily!
• Topics: [Add your main topics]

🌟 *Join the Conversation:*
Don't be shy! Introduce yourself and start participating in our discussions.
"""

# Contact information
CONTACT_MESSAGE = """
📞 *Contact Information*

Need help or have questions? Here's how to reach us:

👑 *Group Administrators:*
• Use @admin to tag administrators
• Send a direct message to group admins
• Report issues using the report feature

💌 *For General Inquiries:*
• Post in the group with your questions
• Check our pinned messages for FAQs
• Use /help for common issues

🚨 *For Urgent Issues:*
• Contact administrators directly
• Use the report feature for violations
• Email: [your-email@example.com]

⏰ *Response Time:*
We typically respond within 24 hours during weekdays.

Thank you for being part of our community! 🙏
"""

def get_random_welcome_message():
    """Get a random welcome message"""
    return random.choice(WELCOME_MESSAGES)
