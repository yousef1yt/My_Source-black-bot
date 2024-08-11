from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from config import YAFA_CHANNEL



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="**الـاوامر**",
                callback_data="zzzback",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="**الـاوامر**", callback_data="zzzback"
            )
        ],
        [
            InlineKeyboardButton(
                text="مطور السورس", url=f"https://t.me/y_o_v"
            ),
            InlineKeyboardButton(
                text=" مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة المطور", url=f"https://t.me/{YAFA_CHANNEL}"
            )
        ],
      
     ]
    return buttons
