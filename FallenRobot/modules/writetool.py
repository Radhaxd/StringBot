import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from FallenRobot import BOT_NAME, BOT_USERNAME
from FallenRobot import pbot as fallen


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "Please wait...,\n\nWriting your text..."
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ ᴡʀɪᴛᴛᴇɴ ʙʏ : [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
❄ ʟɪɴᴋ : {req}
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "Please wait...,\n\nWriting your text..."
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ ᴡʀɪᴛᴛᴇɴ ʙʏ : [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
❄ ʟɪɴᴋ : {req}
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )


help = """
 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite)

dispatcher.add_handler(WRITE_HANDLER)

mod_name = "WʀɪᴛᴇTᴏᴏʟ"
command_list = ["write"]
handlers = [WRITE_HANDLER]
