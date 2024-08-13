from pyrogram.types import InlineKeyboardButton

import config YAFA_CHANNEL,OWNER_CHANNEL,OWNER_ID,SUPPORT_CHAT
from YousefMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_8"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text=_["S_B_7"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=config.YAFA_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], user_id=config.OWNER_CHANNEL),
        ],
    ]
    return buttons
