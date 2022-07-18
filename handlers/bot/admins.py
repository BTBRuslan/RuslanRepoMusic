# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 |
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.command import commandpro
from helpers.filters import other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)


PAUSED = "https://telegra.ph/file/e1baf2c6dde1534acb45f.jpg"
RESUMED = "https://telegra.ph/file/6d861ec0c75efe088d043.jpg"
SKIPPED = "https://telegra.ph/file/ec4cb3823e85bd9bb6022.jpg"
END = "https://telegra.ph/file/30525f90e119bf95d9d80.jpg"

BUTTON = [
    [
        InlineKeyboardButton(text="Sohbet", url=f"https://t.me/Sohbetimalfa"),
        InlineKeyboardButton(text="🗑️kapat", callback_data="close"),
        InlineKeyboardButton(text="Sahibim", url=f"https://t.me/Samilben"), 
    ],
]

ACTV_CALLS = []

@Client.on_message(commandpro(["/pause", "!pause", "durdur", "/durdur", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    
    await message.reply_photo(
        photo=PAUSED,
        caption=f"Müzik durduruldu durduran {message.from_user.mention} 🥀\n\n✦ /devam :- müziği devam ettir",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/resume", "!resume", "devam", "/devam", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    
    await message.reply_photo(
        photo=RESUMED,
        caption=f"müzik devam ediyor {message.from_user.mention} 💫.\n\n✦ /durdur :- şarkıyı duraklat!!",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/end", "!end", "/stop", "!stop", "/son", "son", "stop", "end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chut_id = message.chat.id
    if int(chut_id) not in ACTV_CALLS:
        await message.reply_text(
            "Şu an şarkı çalmıyor   💫",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    
        await message.reply_photo(
            photo=END,
            caption=f"Akış sona erdi iyi günler 🙃 {message.from_user.mention} \n Sesli sohbetten ayrılıyorum güle güle  👋🏻",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    

@Client.on_message(commandpro(["/skip", "!skip", "atla", "/atla", "skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        
        await message.reply_text(
            "Atlamam için şarkı çalmam gerekiyor  💫",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    
    await message.reply_photo(
        photo=SKIPPED,
        caption=f"Sıradaki şarkıya geçildi \nŞarkı atlatıldı{message.from_user.mention}🌟",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()
