# ππππ ππππ ππππ πππππ πππππππππ @Samilben | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π
 
 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from config import SUDO_USERS

HERO_IMG = "https://te.legra.ph/file/7e7bbefe30efa696f0fbc.jpg"

@Client.on_message(filters.command("gcast"))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        sas = await message.reply("`YayΔ±m baΕlayΔ±r, gΓΆzlΙyin βπ»`")
        if not message.reply_to_message:
            await sas.edit("**__MΙnΙ hΙr hansΔ± bir mesaj ver__**")
            return
        hero = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, hero)
                sent = sent+1
                await hyper.edit(f"`YayΔ±mlanΔ±r` \n\n**UΔurlu:** `{sent}` SΓΆhbΙtlΙrπΎ \n**UΔursuz :** {failed} SΓΆhbΙtlΙrποΈ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_photo(HERO_IMG, caption=f"UΔurla edildiπ§βββ­ \n\nUΔurlu**:** `{sent}` SΓΆhbΙtlΙr \n**UΔursuzβΉοΈ :** {failed} SΓΆhbΙtlΙr")
