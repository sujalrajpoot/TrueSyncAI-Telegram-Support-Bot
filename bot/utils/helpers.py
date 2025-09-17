# ================================
# bot/utils/helpers.py
# ================================

import json
import aiofiles
from datetime import datetime
from typing import Dict, Any

async def save_user_data(user_id: int, data: Dict[str, Any]):
    """Save user data to JSON file"""
    try:
        filename = f"data/users/{user_id}.json"
        async with aiofiles.open(filename, 'w') as f:
            await f.write(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error saving user data: {e}")

async def load_user_data(user_id: int) -> Dict[str, Any]:
    """Load user data from JSON file"""
    try:
        filename = f"data/users/{user_id}.json"
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
            return json.loads(content)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading user data: {e}")
        return {}

def format_datetime(dt: datetime) -> str:
    """Format datetime for display"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def escape_markdown(text: str) -> str:
    """Escape markdown special characters"""
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    return text
