# الكود لأول مره على الهيروكو مشرف مع اللقب 
# كتابتي @y_o_v
# محتاج اي كود حكيني :*
import os
from YousefMusic import app
from pyrogram import Client, filters


BOT_TOKEN = os.getenv("BOT_TOKEN")


if not BOT_TOKEN:
    raise ValueError("يرجى تحديد التوكن عبر متغير البيئة 'BOT_TOKEN'")


def command_without_slash(command):
    return filters.regex(f"^{command}( |$)")


@app.on_message(command_without_slash("مشرف") & filters.reply)
def promote_member(client, message):
    try:

        parts = message.text.split(maxsplit=1)

        if len(parts) > 1:
            title = parts[1]

            target_user = message.reply_to_message.from_user


            client.promote_chat_member(
                chat_id=message.chat.id, 
                user_id=target_user.id
            )


            client.set_administrator_title(
                chat_id=message.chat.id, 
                user_id=target_user.id, 
                title=title
            )


            message.reply_text(f'تم رفع {target_user.first_name} مشرفاً!\nولقبه هو: {title}')
        else:
            message.reply_text('يرجى استخدام الأمر بالشكل الصحيح: مشرف [اللقب]')
    except Exception as e:
        print(f"Error: {str(e)}")
        message.reply_text(f'حدث خطأ: {str(e)}')

if __name__ == "__main__":
    app.run()
