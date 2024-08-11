from YousefMusic import app
from typing import Union
from pyrogram.types import InlineKeyboardButton
from config import YAFA_CHANNEL, OWNER_ID



def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/P_6_B"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
           InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?start=help",
            ),
           InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER_ID),
        )
        ],
        [
           InlineKeyboardButton(
                text=_["ST_B_3"],
                callback_data="LG"
            ),
           InlineKeyboardButton(
            text=_["S_B_4"],
            callback_data="zzzback"
        )
        ],
        [
             InlineKeyboardButton(
                text=_["S_B_9"],
                url=f"YAFA_CHANNEL",
            ),
            InlineKeyboardButton(
                text=_["S_B_6"],
                url="https://t.me/P_6_B"
            ),
        ],
    ]
    return buttons
