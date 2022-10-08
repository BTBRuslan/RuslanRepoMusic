# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**Salam👋 {}\n\nMən {} \n\nSəsli söhbətlərdə musiqi oxuya bilən bir botam\n\nMəni qrupunuza əlavə edin sonra admin edərək musiqi dinləyə bilərsiniz🥰**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="➕Məni qrupuna əlavə et➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim 🙇🏻", url=f"https://t.me/Rahid_2003"),
                    InlineKeyboardButton(text="Digər Botlar", url="https://t.me/Rahid_44"),
                ],                
                [                    
                    InlineKeyboardButton(text="Kanalım 😍❤️", url="https://t.me/qruzdaa")
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """Salam👋 {}\nKömək  \nqrupuna əlavə edərək musiqi dinləyə bilərsiniz @{} Sualınız nədir? """
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="🕹️ Təməl əmrləri", callback_data="basic_"),
            InlineKeyboardButton(text="🕹️ Admin əmrləri", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
            InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Salam burada yardım menyusu istədiyiniz seçimi seçin və araşdırın \nİstənilən kömək və ya problem üçün qoşulun @{SUPPORT_GROUP} Sualınız nədir?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="🕹️ Təməl əmrləri", callback_data="bcd"),
                InlineKeyboardButton(text="🕹️ Admin əmrləri", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Salam, Mən {BOT_NAME} \nBu sadə və gecikməsiz bir botdur\nProblem olanda qoşulun 👉 @{SUPPORT_GROUP}\nvə ya /help basın"""
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="🆘 Support", url=f"https://t.me/Rahid_Support"),
                    InlineKeyboardButton(text="Məni qrupa əlavə et ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim 🙇🏻", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sahibim 🙇🏻", url="https://t.me/Rahid_2003"),
                ],                
                [                    
                    InlineKeyboardButton(text="Əmrlər 🕹️", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`Əsas əmrlər:- `

/play (Sorğu, YouTube linki, audio fayl) - bu əmrdən istifadə edin və musiqidən həzz alın
/ytp (Sorgu) - Daha təkmil musiqi axtarmaq üçün istifadə edin
/song (Sorgu) - Bu əmrlə sevimli mahnılarınızı yükləyə bilərsiniz
/ara (Sorgu) - YouTube-da axtarmaq
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin əmrlər:-`

/durdur - Musiqinin ifasını dayandırır
/devam - Dayandırılmış musiqini davam etdirir
/skip - Növbəti mahnıya keçir
/end - Mahnını bitir
/katil - Qrupa köməkçi əlavə edin


`Sudo əmrlər:-`

/rmf - Faylı verilənlər bazasından təmizləyir
/rmw - Data faylları verilənlər bazasından təmizləyir
/clean - Faylları serverdən təmizləyir
/gcast - Qlobal mesaj yayımlamaq
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 Bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
