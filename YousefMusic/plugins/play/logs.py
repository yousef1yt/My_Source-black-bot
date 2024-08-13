from YousefMusic import app
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import json
import os

# استيراد المتغيرات من ملف التكوين
from config import OWNER_ID

# دالة لإرسال رسالة
async def new_message(chat_id: int, message: str, reply_markup=None):
    await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

# دالة لحفظ معلومات المجموعة في ملف JSON
def save_group_info(group_id, group_title):
    group_data = {"group_id": group_id, "group_title": group_title}
    with open("mazen.json", "a") as file:
        json.dump(group_data, file)
        file.write("\n")

# دالة لتحميل معلومات المجموعات من ملف JSON
def load_group_info():
    filename = "mazen.json"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("[]")
    with open(filename, "r") as file:
        return [json.loads(line) for line in file]

# دالة لنسخ المجموعات (دالة وهمية، قم بتعديلها بالمنطق الفعلي للنسخ الاحتياطي)
def backup_groups():
    group_info = load_group_info()
    for group in group_info:
        group_id = group['group_id']
        group_title = group['group_title']
        # قم بتنفيذ المنطق الخاص بالنسخ الاحتياطي هنا
        # على سبيل المثال، يمكنك إرسال النسخة الاحتياطية للمالك أو حفظها في تخزين سحابي

# معالج لحدث دخول أعضاء جدد
@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: app, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "مستخدم غير معروف"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        riruru = f"<b><u>~ تم اضافة البوت الى مجموعة جديدة</u></b>:\n\n~ الأيدي : {chat_id}\n~ المستخدم: {username}\n~ اسم المجموعة: {title}\n\n~ بواسطة: {added_by}"
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(message.from_user.first_name, user_id=message.from_user.id)]
        ])
        
        save_group_info(chat_id, title)
        
        await new_message(OWNER_ID, riruru, reply_markup)

# معالج لحدث مغادرة البوت للمجموعة
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: app, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        removed_by = message.from_user.mention if message.from_user else "مستخدم غير معروف"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        rirurubye = f"<b><u>~ تم ازالة البوت من مجموعة جديدة</u></b>:\n\n~ الأيدي : {chat_id}\n~ رابط المجموعة : {username}\n~ اسم المجموعة : {title}\n\n~ بواسطة : {removed_by}"
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(message.from_user.first_name, user_id=message.from_user.id)]
        ])
        
        await new_message(OWNER_ID, rirurubye, reply_markup)

# أمر لإنشاء نسخة احتياطية
@app.on_message(filters.command("إنشاء_نسخة_احتياطية") & filters.user(OWNER_ID))
async def create_backup(client: app, message: Message):
    backup_groups()
    
    # اسم الملف للنسخة الاحتياطية
    backup_filename = "mazen.json"
    
    # التأكد من وجود الملف
    if os.path.exists(backup_filename):
        # إرسال الملف إلى المالك
        await client.send_document(
            chat_id=OWNER_ID,
            document=backup_filename,
            caption="تم إنشاء نسخة احتياطية للمجموعات"
        )
    else:
        await message.reply_text("حدث خطأ أثناء إنشاء النسخة الاحتياطية.")

# أمر لرفع نسخة احتياطية
@app.on_message(filters.command("رفع_نسخة_احتياطية") & filters.user(OWNER_ID))
async def upload_backup(client: app, message: Message):
    # قم بتنفيذ المنطق الخاص برفع النسخة الاحتياطية هنا
    pass

# تشغيل العميل
if __name__ == "__main__":
    app.run()
