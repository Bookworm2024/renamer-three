# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "21145186")
    API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7681830527:AAHIy7NeWz06sK6EeBLPxogBCLR1AGFvX0c") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","maamthree")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://infohubstore06:RUQbKf1YWc42rOIf@maamthree.csbu5.mongodb.net/?retryWrites=true&w=majority&appName=maamthree")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/8dY.png")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6011680723 5178714818').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002495227151"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results
    
    #vforce subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002123546604")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Bookslibraryofficial")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>ʜᴇʟʟᴏ {}👋

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ʙᴏᴛ
ᴜꜱɪɴɢ ᴍᴇ, ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴀ ꜰɪʟᴇ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ᴀ ᴠɪᴅᴇᴏ ᴛᴏ ᴀ ꜰɪʟᴇ 

ɢᴇᴛ, ꜱᴇᴛ, ɢᴏ! 🚀

<blockquote>ɪ ᴀᴍ ᴄʜᴀʀɢᴇᴅ ʙʏ : @infohub_updates 💞</blockquote></b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/infohub_updates>InfoHub Updates</a>
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/infohubsupport_robot>InfoHub Support</a>
├📕 Lɪʙʀᴀʀy : <a href=https://t.me/Bookslibraryofficial>Pages & Voices</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org/>Python 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://www.mongodb.com/>Mongo DB</a>
├📊 ᴠᴇʀsɪᴏɴ: <a href=https://t.me/infohub_updates>{}</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> ᴛᴏ ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ, ꜱᴇɴᴅ /start

✏️ <b><u>ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀɴʏ ꜰɪʟᴇ?</u></b>

<b>•></b> ꜱᴇɴᴅ ᴀɴʏ ꜰɪʟᴇ ᴀɴᴅ ᴛʏᴘᴇ ᴛʜᴇ ɴᴇᴡ ꜰɪʟᴇ ɴᴀᴍᴇ\n<b>•></b>ꜱᴇʟᴇᴄᴛ ᴛʜᴇ ꜰᴏʀᴍᴀᴛ [ document, video, audio ]\n\n⚠️ᴘ.ꜱ. ᴛʜᴇ ꜰɪʟᴇ ᴄᴏɴᴠᴇʀꜱɪᴏɴ ꜱʏꜱᴛᴇᴍ (ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ) ᴍᴀʏ ɴᴏᴛ ᴡᴏʀᴋ 24x7 ᴀꜱ ɪᴛ ʜᴀꜱ ᴄᴇʀᴛᴀɪɴ ʀᴇꜱᴛʀɪᴄᴛɪᴏɴꜱ ꜱᴇᴛ ᴜᴘ ʙʏ ᴛᴇʟᴇɢʀᴀᴍ ɪᴛꜱᴇʟꜰ!.           

ℹ️ ꜰᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ Qᴜᴇʀʏ, ᴀꜱꜱɪꜱᴛᴀɴᴄᴇ, ᴄᴏɴᴛᴀᴄᴛ - <a href=https://t.me/infohubsupport_robot>ɪɴꜰᴏʜᴜʙ ꜱᴜᴘᴘᴏʀᴛ</a>
"""

    UPGRADE= """
★ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ ᴀʀᴇ - 

•⪼ 🏆 ᴘʀᴏ :
ᴅᴜʀᴀᴛɪᴏɴ - 1 month
ᴘʀɪᴄᴇ - 90 INR
Qᴜᴏᴛᴀ - 100 GB

•⪼ 💎 ᴜʟᴛʀᴀ-ᴘʀᴏ:
ᴅᴜʀᴀᴛɪᴏɴ - 1 month
ᴘʀɪᴄᴇ - 165 INR
Qᴜᴏᴛᴀ - 1000 GB

💸 9% ᴅɪꜱᴄᴏᴜɴᴛ ᴏɴ ᴀʟʟ ᴘʟᴀɴꜱ ꜰᴏʀ ꜰɪʀꜱᴛ ᴛɪᴍᴇʀꜱ.
    """
    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>

<b>•></b> ꜱᴇɴᴅ ᴀɴʏ ᴘɪᴄᴛᴜʀᴇ ᴛᴏ ꜱᴇᴛ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.

<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ- 
`/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""
    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @infohub_updates" -metadata author="@infohubsupport_robot" -metadata:s:s title="Subtitled By :- @infohub_updates" -metadata:s:a title="By :- @infohub_updates" -metadata:s:v title="By:- @infohubsupport_robot" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @infohubsupport_robot
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @infohub_updates`
Exᴀᴍᴩʟᴇ:- `/set_prefix @infohub_updates`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>ꜱᴘᴇᴄɪᴀʟ ᴛʜᴀɴᴋꜱ ᴛᴏ ᴀʟʟ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://t.me/infohubsupport_robot>ɪɴꜰᴏʜᴜʙ ꜱᴜᴘᴘᴏʀᴛ</a>

• ❣️ <a href=https://t.me/the_universal_being>ᏰᎧᎧᏦᏇᎧᏒᎷ</a>
• ❣️ <a href=https://t.me/ridhiigandhii>Ridhi 🦋</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @infohub_updates" -metadata author="@infohubsupport_robot" -metadata:s:s title="Subtitled By :- @infohub_updates" -metadata:s:a title="By :- @infohub_updates" -metadata:s:v title="By:- @infohubsupport_robot" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Digital_Botz
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰RKN PROCESSING...❱━➣
┣⪼ 🗃️ ꜱɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ ᴅᴏɴᴇ : {0}%
┣⪼ 🚀 ꜱᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
