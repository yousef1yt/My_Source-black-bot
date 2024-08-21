import asyncio
import os
from pyrogram.types import CallbackQuery
from YousefMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YousefMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command(["• الاوامر •", "الميوزك", "الاوامر"]))

async def سبارك_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/248700971ed421a3dc2db.jpg",
        caption=f"""*⩹━★⊷━⌞ ˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس  \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        ". 𝖠 ' 𝟣𝟣𝟣 .", url=f"https://t.me/cecrr"),
                ],

            ]

        ),

    )

    

@app.on_callback_query(filters.regex("ch"))
async def سبارك_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .
★¦ اهلا بك عزيزي في قسم اوامر  في الجروبات
★¦ تاك لعمل تاك للكروب
★¦ الرابط لجلب رابط الكروب
★¦ همسه برد ع شخص
★¦ رفع مشرف مع منع تصفية
★¦ كشف المجموعه لعرض معلومات المجموعه
★¦ تثبيت برد ع رساله يثبت رساله بلكروب
★¦ غادر يغادر بوت تلقائي من كروب بواسطه مطور بوت
★¦ يوت او تنزيل+اسم اغنيه لتنزيل الاغنيه
★¦ حجره للعب حجره ورا مقص
★¦ ابراج لتحليل برجك
★¦ اكبتلي + اكتب اي شيئ ليكتبلك عبر ذكاء الاصتناعي
★¦ قولي + اكتب اي شيئ يقولها بمقطع صوتي عبر ذكاء الاصتناعي
★¦ المطور لعرض معلومات المطور
★¦ تلجراف + برد ع صوره 
★¦ نسبه الرجوله لعرض معلومات رجولتك
★¦ لعبه انصحني
★¦ كتابات
★¦ اوقات الصلاه
★¦ تفعيل /تعطيل الادعيه ينشر ادعيه تلقائي بلكروب
★¦ افلام لعرض افلام تقدر تشاهد
★¦ لعبه الاحرف ب امر /احرف
★¦ فتح الكول لفتح الكول ب الكروب
★¦ مين في الكول لعرض من متواجدين ب الكول
★¦ اعلان البوت / لعمل اعلان للبوت
★¦ لو خيروك /خيروك
★¦اسال / س/ سوال
★¦ ص /صراحه
★¦ تشغيل + اسم الاغنيه
˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def سبارك_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .
★¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
★¦ رفع ثانوي
★¦ تنزيل ثانوي
★¦ قائمة الثانويين
★¦ رفع ادمن
★¦ تنزيل ادمن
★¦ قائمة الادمن
★¦ حظر
★¦ الغاء الحظر
★¦ المحظورين
★¦ حظر عام
★¦ الغاء الحظر العام
★¦ المحظورين عام
★¦ اونلاين
★¦ اذاعه
★¦ تحديث
★¦ logger
★¦ ريلود
★¦ وقف
★¦ كمل
★¦ اسكت
★¦ اتكلم
★¦ ايقاف
★¦ تخطي
★¦ @all
★¦ all stop
★¦ يوتيوب / تنزيل
★¦ playing
★¦ القائمه
★¦ حذف القائمه
★¦ تحديث
★¦ الاحصائيات
★¦ لايف
★¦ مساعده
★¦ الاعدادت
★¦ بينج

˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="zzzback"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def سبارك_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/248700971ed421a3dc2db.jpg",
        caption=f"""˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس سبارك \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━★⊷━⌞˛ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗹𝗮𝗰𝗸 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        ". 𝖠 ' 𝟣𝟣𝟣 .", url=f"https://t.me/cecrr"),
                ],

            ]

        ),

    )

