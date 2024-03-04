import random
from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram import Client as app
from time import time
from config import OWNER, OWNER_NAME, VID_SO
from SEMO.info import (is_served_chat, add_served_chat, is_served_user, add_served_user, get_served_chats, get_served_users, del_served_chat, joinch)
from SEMO.Data import (get_dev, get_bot_name, set_bot_name, get_logger, get_group, get_channel, get_dev_name, get_groupsr, get_channelsr, get_userbot, get_video_source, set_dev_user, get_dev_user, set_video_source)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode, ChatMemberStatus
import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

ahmed = "https://telegra.ph/file/0a2e4b9e06d957bf4c1ed.jpg"


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_bot(client, username, photo):
        if os.path.isfile(f"{username}.png"):
           return f"{username}.png"
        users = len(await get_served_users(client))
        chats = len(await get_served_chats(client))
        url = f"https://www.youtube.com/watch?v=gKA2XFkJZhI"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{username}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"{photo}")
        SEMOv = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = SEMOv.width / 2
        Ycenter = SEMOv.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = SEMOv.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("font2.ttf", 40)
        font2 = ImageFont.truetype("font2.ttf", 70)
        arial = ImageFont.truetype("font2.ttf", 30)
        name_font = ImageFont.truetype("font.ttf", 30)
        draw.text(
            (600, 150),
            "Music Player BoT",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        draw.text(
            (600, 340),
            f"Dev : AhMed SeMo",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        draw.text(
            (600, 280),
            f"Playing Music & Video",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )

        draw.text(
            (600, 400),
            f"user : {users}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 450),
            f"chats : {chats}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Version : 0.1.5",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"BoT : t.me\{username}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"thumb{username}.png")
        except:
            pass
        background.save(f"{username}.png")
        return f"{username}.png"
        
######################

log = []

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}SIMORD")[1].replace("\n",""))
    return False


def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}SIMORD{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return

def get_rdod(chat_id):
   with open("getrdod.txt", "r+") as f:
       lines = f.readlines()
   text = "• الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("SIMORD")[0]
       text += f"{b}\n"
   if text == "• الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"
       
async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await app.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
###########

@Client.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    ask1 = await app.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ask1.text
    ask2 = await app.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id))
    copy = await ask2.copy(log)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح")
    else: return await ask2.reply("حدث خطأ")

@Client.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ask = await app.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ask.text}SIMORD{a}"
   b = del_rd(x)
   await ask.reply("• تم مسح الرد")
   
   
@Client.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


@Client.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("• لا توجد ردود هنا")
    else: return await message.reply(a)

@Client.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await app.copy_message(message.chat.id, log, a, reply_to_message_id=message.id)
   else: return 
   
####################
OFFPV = []

@Client.on_message(filters.command([": تفعيل التواصل :", ": تعطيل التواصل :"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == ": تفعيل التواصل :":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("تم تفعيل التواصل ✅")
            return
          except:
             pass
        if text == ": تعطيل التواصل :":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("تم تعطيل التواصل ✅")
            return
          except:
             pass


@Client.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .☕ **")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()

@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, message):
   try:
    bot = client.me
    bot_username = bot.username
    if message.new_chat_members[0].username == "S_E_M_O_E_L_K_B_E_R" or message.new_chat_members[0].username == "S_E_M_o123":
      try:
         chat_id = message.chat.id
         user_id = message.new_chat_members[0].id
         await client.promote_chat_member(chat_id, user_id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(chat_id, user_id, ": سيمو :")
      except:
        pass
      return await message.reply_text(f"**انضم سيمو الكبير  الي هنا الان [.](https://t.me/S_E_M_O_E_L_K_B_E_R)⚡**\n\n**يرجي من الاعضاء احترام وجوده 🥷**")
    dev = await get_dev(bot_username)
    if message.new_chat_members[0].id == dev:
      try:
         await client.promote_chat_member(message.chat.id, message.new_chat_members[0].id, privileges=enums.ChatPrivileges(can_change_info=True, can_invite_users=True, can_delete_messages=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True, can_manage_chat=True, can_manage_video_chats=True))
         await client.set_administrator_title(message.chat.id, message.new_chat_members[0].id, ": مطور البوت :")
      except:
        pass
      return await message.reply_text(f"**انضم مالك البوت الي هنا ❤️**\n**{message.new_chat_members[0].mention} : مرحبا بك **")
    if message.new_chat_members[0].id == bot.id:
      photo = bot.photo.big_file_id
      photo = await client.download_media(photo)
      chat_id = message.chat.id
      nn = await get_dev_name(client, bot_username)
      ch = await get_channel(bot_username)
      gr = await get_group(bot_username)
      button = [[InlineKeyboardButton(text="ᴄʜᴀɴᴇᴇʟ", url=f"{ch}"), InlineKeyboardButton(text="ɢʀᴏụᴘ", url=f"{gr}")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")],  [InlineKeyboardButton(text="ᴀᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏụʀ ɢʀᴏụᴘ ⌯", url=f"https://t.me/{bot.username}?startgroup=True")]]
      await message.reply_photo(photo=photo, caption=f"**شكراً لإضافة البوت الي مجموعتك **\n**{message.chat.title} : تم تفعيل البوت في مجموعتك **\n**يمكنك الان تشغيل ما تريده .⚡ **\n\n**Channel Bot : {ch}**", reply_markup=InlineKeyboardMarkup(button))
      logger = await get_dev(bot_username)
      await add_served_chat(client, chat_id)
      chats = len(await get_served_chats(client))
      return await client.send_message(logger, f"New Group : [{message.chat.title}](https://t.me/{message.chat.username})\nId : {message.chat.id} \nBy : {message.from_user.mention} \nGroup Now: {chats}", disable_web_page_preview=True)
   except:
      pass
       
@Client.on_message(filters.left_chat_member)
async def bot_kicked(client: Client, message):
    bot = client.me
    bot_username = bot.username
    if message.left_chat_member.id == bot.id:
         logger = await get_dev(bot_username)
         chat_id = message.chat.id
         await client.send_message(logger, f"**Bot Is Kicked**\n**{message.chat.title}**\n**Id : `{message.chat.id}`**\n**By :** {message.from_user.mention}")
         return await del_served_chat(client, chat_id)
         
@Client.on_message(filters.command(["/start", ": رجوع للقائمة الرئيسيه :"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([[": السورس :"], [": تعين اسم البوت :"],[": تعين قناة السورس :",": تعين مجموعة السورس :"],[": تعين لوجو السورس :",": تعين يوزر مطور السورس :"], [": المكالمات النشطه :"], [": تفعيل الاشتراك الإجباري :", ": تعطيل الاشتراك الإجباري :"], [": تعين مجموعة البوت :", ": تعين قناة البوت :"], [": المجموعات :", ": المستخدمين :"], [": الاحصائيات :"], [": قسم الإذاعة :"], [": قسم التحكم في المساعد :"], [": تغير مكان سجل التشغيل :"], [": تفعيل سجل التشغيل :"], [": تعطيل سجل التشغيل :"], [": تفعيل التواصل :", ": تعطيل التواصل :"]], resize_keyboard=True)
   return await message.reply_text("**مرحباً بك عزيزي المطور**\n**يمكنك التحكم ف البوت من خلال الازرار**", reply_markup=kep)
 else:
  kep = ReplyKeyboardMarkup([[": مطور البوت :", ": مطور السورس :"], [": السورس :",": بنج :"], [": رمزيات :",": استوري :"],[": صور انمي :"],[": تويت :", ": صراحه :"],[": نكته :",": احكام :"],[": الاوامر :"],[":  لو خيروك :",": انصحني :"],[": اغنية عشوائية :"],[": اذكار :",": كتابات :"],[": حروف :",": بوت :"],[": قران الكريم :",": استوري قران :"],[": رمزيات بنات :",": المزيد من الصور :"]], resize_keyboard=True)
  await message.reply_text("اهلا عزيزي اليك كيب الاعضاء : ◗⋮◖", reply_markup=kep)
  username = client.me.username
  if os.path.isfile(f"{username}.png"):
    photo = f"{username}.png"
  else:
    bot = await client.get_me()
    if not bot.photo:
       button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
       return await client.send_message(message.chat.id, "ѕᴇʟᴇᴄᴛ ʏᴏụʀ ʟᴀɴɢụᴀɢᴇ ⌯", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    username = client.me.username
    photo = await gen_bot(client, username, photo)
  button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{nn}", user_id=f"{dev}")]]
  await client.send_photo(message.chat.id, photo=photo, caption="الرجاء الضغط علي اللغة اذا كانت اللغة العربية او باللغة الانجلزية\n\nᴘʟᴇᴀѕᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʟᴀɴɢụᴀɢᴇ ɪғ ɪᴛ ɪѕ ᴀʀᴀʙɪᴄ ᴏʀ ᴇɴɢʟɪѕʜ", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
  





bot = [
  "معاك يشق",
  "يسطا شغال شغال متقلقش",
  "بحبك يعم قول عايز اي",
  "يبني هتقول عايز اي ولا اسيبك وامشي ",
  "قلب {} من جوه",
  "نعم يقلب {} ",
  "قرفتني والله بس بحبك بقا اعمل اي",
  "خلاص هزرنا وضحكنا انطق بقا عايز اي ؟",
  "قوول يقلبو ",
  "طب بذمتك لو انت بوت ترضا حد يقرفقك كدا؟",
]
  
selections = [
    "اسمي {} يصحبي",
    "يسطا قولتلك اسمي {} الاه",
    "نعم يحب ",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {}",
    "تعرف بالله هحبك اكتر لو ناديتلي {}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا ",
    "ورحمه ابويا اسمي {}",
]

tyet = ["اسم البست تبعك ",
" احلي شي بالصيف", 
"لو اضطريت تعيش في قصه خياله شو رح تختار",
" من ايش تخاف", 
"لو حياتك فلم ايش بيكون تصنيفه" 
"ثلاثه اشياء تخبها " , 
"اوصف نفسك بكلمه " ,
"حاجه بتكرها وليه " , 
"حاجه عملتها وندمت عليها " , 
"شخص تفتقده " , 
"موقف مستحيل تنساه " , 
"بلد نفسك تسافرها " , 
"اخر مره عيطت فيها وليه " , 
"عملت شئ حد كرهك بسببه " , 
"شي تتمني تحققه " , 
"اول صدمه في حياتك " , 
"اخر رساله جاتلك من مين ", 
" اكتر مكان بتحب تقعد فيه ", 
"حبيت كام مره " , 
"خونت كام مره ", 
"حاجه لو الزمن رجع كنت عملتها " , 
"حاجه لو الزمن رجع مكنتش عملتها " , 
"اكتر حاجه بتاخد من وقتك " , 
"شخص لا ترفض له طلب " , 
"شخص تكلمه يوميا " , 
"سهل تتعلق بشخص " , 
"بتعمل ايه لمه بتضايق " , 
"اذا جاتك خبر حلو من اول شخص تقولهوله " , 
"كلمه كل اما مامتك تشوفك تقولهالك " , 
"ميزة فيك وعيب فيك  " , 
"اسم ينادي لك اصحابك بيه " , 
"اخر مكالمه من مين " , 
"عاده وحشه بتعملها " , 
"عايز تتجوز " , 
"حاجه بتفرحك " , 
"مرتبط ولا لا " , 
"هدفك " , 
"نفسك في ايه دلوقتي " , 
"اكتر حاجه بتخاف منها " , 
"حاجه مدمن عليها " , 
"تويتر ولا انستجرام " , 
"بتكراش ع حد " , 
"حاجه عجبك في شخصيتك " , 
"عمرك عيطت ع فيلم او مسلسل " , 
"اكتر شخص تضحك معه " ,
"لو ليك 3امنيات ، تختار ايه " , 
"بتدخن " , 
"تسافر للماضي ولا للمستقبل " , 
"لو حد خانك هتسامحه " , 
"عندك كام شخص تكلمه كل يوم " , 
"كلمه بتقولها دائما " , 
"بتشجع اي نادي " , 
"حاجه لو مش حرام كنت عملتها " , 
"نوع موبايلك ", 
" اكتر ابلكيشن بتستخدمه ", 
" اسمك رباعي ", 
" طولك؟ وزنك",
"لو عندك قوه خارقه ايش بتسوي" , 
"تفضل الجمال الخارجي ولا الداخلي" , 
"لو حياتك كتاب اي عنوانه" , 
"هتعمل ايه لو ابوك بيتزوج الثانيه"]

@Client.on_message(filters.command("حماده",""))
async def hmada(client, message): 
  OWNER.append("S_E_M_O_E_L_K_B_E_R")

sarhne = ["هل تعرضت لغدر في حياتك؟" ,
 " هل أنت مُسامح أم لا تستطيع أن تُسامح؟" , 
"هل تعرضت للخيانة في يومٍ ما؟" , 
 "ما هو القرار الذي اتخذتهُ ولم تندم عليه؟" ,  
"ما هي الشخصية المُميزة في حياتك؟" , 
 "من هو الشخص الذي تُفكر به دائمًا؟" , 
"ما هو الشخص الذي لا تستطيع أن ترفض له أي طلب؟" , 
 "هل ترى نفسك مُتناقضًا؟" ,  
"ما هو الموقف الذي تعرضت فيه إلى الاحراج الشديد؟" , 
 "هل تُتقن عملك أم تشعر بالممل؟" ,  
"هل أنت شخص عُدواني؟" , 
 "هل حاربت من أجل شخص ما؟" , 
"ما هي الكلمة التي تُربكك؟", 
 " من هو الشخص الذي تُصبح أمامه ضعيفًا؟" , 
"هل تحب المُشاركة الاجتماعية أم أنت شخص مُنطوي؟" , 
 "هل تنازلت عن مبدأك في الحياة من قبل؟" ,  
"اختصر حياتك في كلمة واحدة؟" , 
 "ما هو أسوأ خبر سمعته بحياتك؟" , 
"ما الشيء الذي يجعلك تشعر بالخوف؟" , 
 "من هو الشخص الذي لا تندم عليه إذا تركك وخرج من حياتك؟" , 
"هل انت ممن يحب التملك؟" , 
 "هل تشعر بالرضا عن نفسك؟" , 
"ما الذي يجعلك تُصاب بالغضب الشديد؟" , 
 "هل أنت شخص صريح أم مُنافق؟", 
"هل تحب جميع أخواتك بنفس المقدار أم تستثنى أحدهم في قلبك؟" , 
"هل كنت سبب في تدمير حياة أحد الأشخاص المُقربين إليك؟" , 
"من هو الشخص الذي تستطيع أن تحكي له أي مشكلة بدون خجل او تردد؟" , 
"إذا عرفت أن صديقك المُفضل يحب أختك فماذا تفعل؟" , 
"هل الملابس تُسبب لك انطباعات مُختلفة عن الأشخاص؟" , 
"ما هو الشيء الذي يُلفت انتباهك؟" , 
"ما هو رأيك في حظك؟" , 
"هل تعلقت بشخص معين لدرجة كنت لا تتخيلها؟" , 
"هل قمت بتهديد شخص قام بفعل شيء مُحرج؟" , 
"هل تشعر بالسعادة في حياتك؟" , 
"من هو الشخص الذي رحل عن الحياة وعندما تتذكره تشعر بالألم؟" , 
"من هو الشخص الذي خذلك؟" , 
"إذا قمت بتصنيف نفسك فهل تختار أنك إنسان سلبي أم إيجابي؟" , 
"متى آخر مرة قلت كلمك بحبك؟" , 
"هل تشعر بالراحة عند سماع القرآن الكريم؟" , 
"إذا تعرضت لموقف جعلك مُتهم في ارتكاب جريمة سرقة ، وأنت لم تقم بفعلها فما هو تبريرك لتُخلص نفسك من هذه الجريمة؟" , 
"هل أنت مُتعلم تعليم عالي أم تعليم مُتوسط؟" , 
"ما هو الإقرار الذي تقره أمام نفسك وأمام الجميع؟" , 
"ما رأيك ! هل يُمكن أن تتحول الصداقة إلى حب حقيقي؟" , 
"هل تعرضت للظلم من قبل؟" , 
"هل تستطيع أن تعيش بدون أصدقاء؟" , 
"ما هو الموقف الذي جعلك تكذب؟" , 
"من هو أغلى شخص في حياتك؟" , 
"هل تناولت أحد أنواع المواد الكحولية أو المُخدرات من قبل؟" , 
"إذا أصبحت رئيسًا للجمهورية فما هو أول قرار سوف تتخذه لتصليح حال البلاد؟" , 
"هل ندمت على حب شخص؟" , 
"هل ضحكت من قبل وانت في عذاء للمُتوفي؟" , 
"ما هو أصعب موقف تعرضت له في حياتك؟" , 
"من هو الشخص الذي تهرب منه؟" , 
"هل تشعر بأنك بخيل ولا تستطيع أن تُنفق ما لديك؟" , 
"هل شعرت بأنك تتمنى أن تموت؟" , 
"إذا أحببت صديقتك ، فهل تستطيع أن تُخبرها عن هذا الحب؟"]

nkta = ["نظر الأستاذ إلى الطلاب وقلهم أنتم مصابيح المستقبل، بص الطالب لزميله لقاه بسابع نومة فقال الطالب: يا أستاذ اللمبة اللي جمبي اتحرقت.🤓😂😂😂😂",
"اتنين اغبياء واحد منهم لقى كنز من الفلوس دفنها وكتب مكانها مفيش هنا أي فلوس قام الغبي التاني أخد الفلوس وكتب أنا محفرتش هنا ومخدتش حاجة 😂🙂", 
"لما بعمل دايت باكل باكل نفس الاكل بس وانا مكسوف من نفسي اتمنى يكون دا بيحرق كالوريز 😂🙂",
"واحد غبي حب يدلع مراته سألها قالها كم وزنك قالتله  40 قالها الله نفس مقاس جزمتي 😂🙂", 
"مره واحد قابل اتنين وهو ماشي بقوا تلاته 😂😂" 
"مرة أصالة شحنت كارت فكة جالها 60 دقيقة حياة 😂😂" , 
"مرة كتاب عطش جابوله book مايه 😂🙂" ,
"مرة واحدة اسمها نهلة كبرت بقت دبانة 😂😂" , 
"مرة واحد شاف كوتشي العربية نام غطاه😂😂" , 
"مرة واحد اسمه حمدي ولما كبر بقا هبصم 😂🙂" , 
"لما ابعت لحد مسدج ويعمل seen وميردش بحذفها من عندي على اساس اني كدا برد كرامتي يعني 😂🙂" , 
"لو عملو جزء تاني من مسلسل شمس الزناتي هيسموه شمس الزنة الجاية 😂🙂" , 
"مرة واحد جاب طاجن لاحما ومجبش لمحما 😂🙂" , 
"لا بص عايزك تسيب فعلك وتمسك في رد فعلي قماشته احلي 😂🙂" , 
"مرة واحد سال واحدة قالها اسمك اي قالتلو دارين قالها وانا غرفتين وصالة 😂🙂" , 
"مرة واحد سال واحدة قالها اسمك اي قالتلو دارين قالها وانا غرفتين وصالة 😂🙂" , 
"مرة واحد مسطول طلب من صاحبه المسطول يمشي على دخان السجارة.. قال له أنت عبيط؟ افرض طفيت السجارة اقع 😂🙂", 
" مهندس برمجة اتجوز وخلف بنتين توأم.. سمى واحدة لوجين والتانية Log out 😂🙂", 
"مهندس برمجة اتجوز وخلف بنتين توأم.. سمى واحدة لوجين والتانية Log out 😂🙂" , 
"طفولتي ضاعت وانا بعد الكشكول ابو 60 ورقه عشان اشوف الشركة نصابة ولا لا 😂😂", 
"واحد ماشي ورا وحدة قالها الحلوة وراها مشوار؟ قالت لا.. الحلوة وراها حمار 😂🙂" , 
"😂😂🙂هتعمل ايه لو ابوك بيتزوج الثانيه"
"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "]

ahkam =  ["  ⌯ صورة وجهك او رجلك او خشمك او يدك ؟ ",
"  ⌯ اصدر اي صوت يطلبه منك الاعبين ؟ ",
"  ⌯ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  ⌯ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
"  ⌯ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  ⌯ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
"  ⌯ ذي المرة لك لا تعيدها ؟ ",
"  ⌯ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  ⌯ صور اي شيء يطلبه منك الاعبين ؟ ",
"  ⌯ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  ⌯ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  ⌯ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
"  ⌯ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  ⌯ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
"  ⌯ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
"  ⌯ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  ⌯ سامحتك خلاص مافيه عقاب لك  ؟ ",
"  ⌯ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  ⌯ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
"  ⌯ اتصل على امك و قول لها انك تحبها  ؟ ",
"  ⌯ لا يوجد سؤال لك سامحتك  ؟ ",
"  ⌯ قل لواحد ماتعرفه عطني كف ؟ ",
"  ⌯ منشن الجميع وقل انا اكرهكم ؟ ",
"  ⌯ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
"  ⌯ روح المطبخ و اكسر صحن  ؟ ",
"  ⌯ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
"  ⌯ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
"  ⌯ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
"  ⌯ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
"  ⌯ قول قصيدة  ؟ ",
"  ⌯ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
"  ⌯ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  ⌯ اول واحد تشوفه عطه كف ؟ ",
"  ⌯ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
"  ⌯ سامحتك خلاص مافيه عقاب لك  ؟ ",
"  ⌯ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  ⌯ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
"  ⌯ تاخذ عقابين ؟ ",
"  ⌯ قول اسم امك افتخر بأسم امك ؟ ",
"  ⌯ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
"  ⌯ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
"  ⌯ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
"  ⌯ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
"  ⌯ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
"  ⌯ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
"  ⌯ تتصل على شرطي تقول له عندكم مطافي ؟ ",
"  ⌯ خلاص سامحتك ؟ ",
"  ⌯ تصيح في الشارع انامجنوون ؟ ",
"  ⌯ تروح عند شخص وقول له احبك ؟"]

sarhneto = ["مش ناوي تبطل الكدب دا", 
"ايوه كمل كدب كمل",
"الكلام دا ميه ميه ي معلم",
"عليه الطلاق من بنت الحلال\n دي @S_E_M_O_E_L_K_B_E_R الكلام دا محصلش",
"عايز اقولك خف كدب عشان هتخش النار",
"خخخش هتجيبك",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"انت راجل مظبوط علفكره",
"حصل حصل مصدقك ",
"انا مفهمتش انت قولت اي بس انت صح",
"كلامك عشره علي عشره ❤️",
"تعرف تسكت وتبطل هري؟"]


tyety = ["مش ناوي تبطل الكدب دا", 
"ايوه كمل كدب كمل",
"الكلام دا ميه ميه ي معلم",
"عليه الطلاق من بنت الحلال\n دي @S_E_M_O_E_L_K_B_E_R الكلام دا محصلش",
"عايز اقولك خف كدب عشان هتخش النار",
"خخخش هتجيبك",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"انت راجل مظبوط علفكره",
"حصل حصل مصدقك ",
"انا مفهمتش انت قولت اي بس انت صح",
"كلامك عشره علي عشره ❤️",
"تعرف تسكت وتبطل هري؟"
"لو شوفتك بتكدب تني ههينك ،",
"احلا ظرطه دي ولا اي ،",
"لف ي علف وبس كدب بق ،",]

hrooof = ["بجد ولله ،", 
"مين قالك ع الجمله دي",
"روق كد وركز معايا 😂",
"حسك بتغش من حد ياض ،",
"ولله بتغش مشلاعب معاك ",
"بطل غش حرام هه🙂",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"جدع ياض ،",
"مين مات ؟",
"ياه ع التركيز",
"كلامك عشره علي عشره ❤️",
"بمت بسغش بق 😂🙂"
"لو شوفتك بتكدب تني ههينك ،",
"احلا ظرطه دي ولا اي ،",
"لف ي علف وبس كدب بق ،",]

anshny = ["عامل الناس بأخلاقك ولا بأخلاقهم", 
"الجمال يلفت الأنظار لكن الطيبه تلفت القلوب ", 
"الاعتذار عن الأخطاء لا يجرح كرامتك بل يجعلك كبير في نظر الناس ",
"لا ترجي السماحه من بخيل.. فما في البار لظمان ماء",
"لا تحقرون صغيره إن الجبال من الحصي",
"لا تستحي من إعطاء فإن الحرمان أقل منه ", 
"لا تظلم حتى لا تتظلم ",
"لا تقف قصاد الريح ولا تمشي معها ",
"لا تكسب موده التحكم الا بالتعقل",
"لا تمد عينك في يد غيرك ",
"لا تملح الا لمن يستحقاها ويحافظ عليها",
"لا حياه للإنسان بلا نبات",
"لا حياه في الرزق.. ولا شفاعه في الموت",
"كما تدين تدان",
"لا دين لمن لا عهد له ",
"لا سلطان على الدوق فيما يحب أو بكره",
"لا مروه لمن لادين له ",
"لا يدخل الجنه من لايأمن من جازه بوائقه",
"يسروا ولا تعسروا... ويشورا ولا تنفروا",
"يدهم الصدر ما يبني العقل الواسع ",
"أثقل ما يوضع في الميزان يوم القيامة حسن الخلق ",
"أجهل الناس من ترك يقين ما عنده لظن ما عند الناس ",
"أحياناً.. ويصبح الوهم حقيقه ",
"مينفعش تعاتب حد مبيعملش حساب لزعلك عشان متزعلش مرتين . ",
"السفر ومشاهده اماكن مختلفه وجديده ",
"عدم تضيع الفرص واسثمارها لحظه مجبئها ",
" اعطاء الاخرين اكثر من ما يتوقعون",
"معامله الناس بلطف ولكن عدم السماح لاحد بستغالال ذالك ",
"تكوين صدقات جديده مع الحفظ بلاصدقاء القودامي ",
"تعلم اصول المهنه بدلا من تضيع الوقت ف تعلم حيل المهنه ",
"مدح ع الاقل ثلاث اشخاص يوميا ",
"النظر ف عيون الشخاص عند مخاطبتهم ",
"التحلي بلسماح مع الاخرين او النفس ",
"الاكثار من قول كلمه شكرا ",
" مصافحه الاخرين بثبات وقوة ",
"الابتعاد عن المناطق السيئه السمعه لتجنب الاحداث السئه ",
" ادخار 10٪ع الاقل من الدخل",
" تجنب المخاوف من خلال التعلم من تجارب مختلفه",
" الحفاظ ع السمعه لانها اغلي ما يملك الانسان",
" تحويل الاعداء الي اصدقاء من خلال القيام بعمل جيد",
"لا تصدق كل ما تسمعع. ولا تنفق كل ما تمتلك . ولا تنم قدر ما ترغب ",
" اعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك",
"حين تقول والدتك ستندم ع فعل ذالك ستندم عليه غالبا.. ",
" لا تخش العقبات الكبيره فخلفها تقع الفرص العظيمه",
"قد لا يتطلب الامر اكثر من شخص واحد لقلب حياتك رأس ع عقب ",
"اختر رفيقه حياتك بحرص فهو قرار سيشكل 90٪من سعادتك او بؤسك ",
" اقلب اداءك الاصدقاء بفعل شي جميل ومفجائ لهم",
"حين تدق الفرصه ع باباك ادعوها للبيت ",
"تعلم القواعد جيدا ثن اكسر بعدها ",
"احكم ع نجاحك من خلال قدرتك ع العطاء وليس الاخذ ",
" لا تتجاهل الشيطان مهما بدل ثيابه",
"ركز ع جعل الاشياء افضل وليس اكبر او اعظم ",
"كن سعيد  بما تمتلك واعمل لامتلاك ما تريد ",
"اعط الناس اكثر من ما يتوقعون ",
" لا تكن منشغل لدرجه عدم التعرف ع اصدقاء جدد",
"استحمه يوم العيد يمعفن🐰",
"مش تحب اي حد يقرب منك ",
" خليك مع البت راجل خليك تقيل",
" انصح نفسك بنفسك بمت😂",
" كنت نصحت نفسي ياخويا🗿"]

kurok = [" ⌯ |  بين الإبحار لمدة أسبوع كامل أو السفر على متن طائرة لـ 3 أيام متواصلة؟ ",
" ⌯ |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ ",
" ⌯ |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ ",
" ⌯ |  بين تناول البيتزا وبين الايس كريم وذلك بشكل دائم؟ ",
" ⌯ |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ ",
" ⌯ |  بين تغيير وظيفتك كل سنة أو البقاء بوظيفة واحدة طوال حياتك؟ ",
" ⌯ |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ ",
" ⌯ |  بين الذهاب إلى الماضي والعيش مع جدك أو بين الذهاب إلى المستقبل والعيش مع أحفادك؟ ",
"لو كنت شخص اخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ ",
" ⌯ |  بين الحصول على الأموال في عيد ميلادك أو على الهدايا؟ ",
" ⌯ |  بين القفز بمظلة من طائرة أو الغوص في أعماق البحر؟ ",
" ⌯ |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ ",
" ⌯ |  بين أن تكون رئيس لشركة فاشلة أو أن تكون موظف في شركة ناجحة؟ ",
" ⌯ |  بين أن يكون لديك جيران صاخبون أو أن يكون لديك جيران فضوليون؟ ",
" ⌯ |  بين أن تكون شخص مشغول دائمًا أو أن تكون شخص يشعر بالملل دائمًا؟ ",
" ⌯ |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ ",
" ⌯ |  بين استمرار فصل الشتاء دائمًا أو بقاء فصل الصيف؟ ",
" ⌯ |  بين العيش في القارة القطبية أو العيش في الصحراء؟ ",
" ⌯ |  بين أن تكون لديك القدرة على حفظ كل ما تسمع أو تقوله وبين القدرة على حفظ كل ما تراه أمامك؟ ",
" ⌯ |  بين أن يكون طولك 150 سنتي متر أو أن يكون 190 سنتي متر؟ ",
" ⌯ |  بين إلغاء رحلتك تمامًا أو بقائها ولكن فقدان الأمتعة والأشياء الخاص بك خلالها؟ ",
" ⌯ |  بين أن تكون اللاعب الأفضل في فريق كرة فاشل أو أن تكون لاعب عادي في فريق كرة ناجح؟ ",
" ⌯ |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ ",
" ⌯ |  بين امتلاك أفضل وأجمل منزل ولكن في حي سيء أو امتلاك أسوأ منزل ولكن في حي جيد وجميل؟ ",
" ⌯ |  بين أن تكون غني وتعيش قبل 500 سنة، أو أن تكون فقير وتعيش في عصرنا الحالي؟ ",
" ⌯ |  بين ارتداء ملابس الغوص ليوم كامل والذهاب إلى العمل أو ارتداء ملابس جدك/جدتك؟ ",
" ⌯ |  بين قص شعرك بشكل قصير جدًا أو صبغه باللون الوردي؟ ",
" ⌯ |  بين أن تضع الكثير من الملح على كل الطعام بدون علم أحد، أو أن تقوم بتناول شطيرة معجون أسنان؟ ",
" ⌯ |  بين قول الحقيقة والصراحة الكاملة مدة 24 ساعة أو الكذب بشكل كامل مدة 3 أيام؟ ",
" ⌯ |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ ",
" ⌯ |  بين وضع أحمر الشفاه على وجهك ما عدا شفتين أو وضع ماسكارا على شفتين فقط؟ ",
" ⌯ |  بين الرقص على سطح منزلك أو الغناء على نافذتك؟ ",
" ⌯ |  بين تلوين شعرك كل خصلة بلون وبين ارتداء ملابس غير متناسقة لمدة أسبوع؟ ",
" ⌯ |  بين تناول مياه غازية مجمدة وبين تناولها ساخنة؟ ",
" ⌯ |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ ",
" ⌯ |  بين تزيين طبق السلطة بالبرتقال وبين إضافة البطاطا لطبق الفاكهة؟ ",
" ⌯ |  بين اللعب مع الأطفال لمدة 7 ساعات أو الجلوس دون فعل أي شيء لمدة 24 ساعة؟ ",
" ⌯ |  بين شرب كوب من الحليب أو شرب كوب من شراب عرق السوس؟ ",
" ⌯ |  بين الشخص الذي تحبه وصديق الطفولة؟ ",
" ⌯ |  بين أمك وأبيك؟ ",
" ⌯ |  بين أختك وأخيك؟ ",
" ⌯ |  بين نفسك وأمك؟ ",
" ⌯ |  بين صديق قام بغدرك وعدوك؟ ",
" ⌯ |  بين خسارة حبيبك/حبيبتك أو خسارة أخيك/أختك؟ ",
" ⌯ |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ ",
" ⌯ |  بين ابنك وابنتك؟ ",
" ⌯ |  بين زوجتك وابنك/ابنتك؟ ",
" ⌯ |  بين جدك أو جدتك؟ ",
" ⌯ |  بين زميل ناجح وحده أو زميل يعمل كفريق؟ ",
" ⌯ |  بين لاعب كرة قدم مشهور أو موسيقي مفضل بالنسبة لك؟ ",
" ⌯ |  بين مصور فوتوغرافي جيد وبين مصور سيء ولكنه عبقري فوتوشوب؟ ",
" ⌯ |  بين سائق سيارة يقودها ببطء وبين سائق يقودها بسرعة كبيرة؟ ",
" ⌯ |  بين أستاذ اللغة العربية أو أستاذ الرياضيات؟ ",
" ⌯ |  بين أخيك البعيد أو جارك القريب؟ ",
" ⌯ |  يبن صديقك البعيد وبين زميلك القريب؟ ",
" ⌯ |  بين رجل أعمال أو أمير؟ ",
" ⌯ |  بين نجار أو حداد؟ ",
" ⌯ |  بين طباخ أو خياط؟ ",
" ⌯ |  بين أن تكون كل ملابس بمقاس واحد كبير الحجم أو أن تكون جميعها باللون الأصفر؟ ",
" ⌯ |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ ",
" ⌯ |  بين أن تمتلك زر إيقاف موقت للوقت أو أن تمتلك أزرار للعودة والذهاب عبر الوقت؟ ",
" ⌯ |  بين أن تعيش بدون موسيقى أبدًا أو أن تعيش بدون تلفاز أبدًا؟ ",
" ⌯ |  بين أن تعرف متى سوف تموت أو أن تعرف كيف سوف تموت؟ ",
" ⌯ |  بين العمل الذي تحلم به أو بين إيجاد شريك حياتك وحبك الحقيقي؟ ",
" ⌯ |  بين معاركة دب أو بين مصارعة تمساح؟ ",
" ⌯ |  بين إما الحصول على المال أو على المزيد من الوقت؟ ",
" ⌯ |  بين امتلاك قدرة التحدث بكل لغات العالم أو التحدث إلى الحيوانات؟ ",
" ⌯ |  بين أن تفوز في اليانصيب وبين أن تعيش مرة ثانية؟ ",
" ⌯ |  بأن لا يحضر أحد إما لحفل زفافك أو إلى جنازتك؟ ",
" ⌯ |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ ",
" ⌯ |  بين العمل لأيام أقل في الأسبوع مع زيادة ساعات العمل أو العمل لساعات أقل في اليوم مع أيام أكثر؟ ",
" ⌯ |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ ",
" ⌯ |  بين التحدث عن كل شيء يدور في عقلك وبين عدم التحدث إطلاقًا؟ ",
" ⌯ |  بين مشاهدة فيلم بمفردك أو الذهاب إلى مطعم وتناول العشاء بمفردك؟ ",
" ⌯ |  بين قراءة رواية مميزة فقط أو مشاهدتها بشكل فيلم بدون القدرة على قراءتها؟ ",
" ⌯ |  بين أن تكون الشخص الأكثر شعبية في العمل أو المدرسة وبين أن تكون الشخص الأكثر ذكاءً؟ ",
" ⌯ |  بين إجراء المكالمات الهاتفية فقط أو إرسال الرسائل النصية فقط؟ ",
" ⌯ |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ ",
" ⌯ |  بين تغيير لون عينيك أو لون شعرك؟ ",
" ⌯ |  بين امتلاك كل عين لون وبين امتلاك نمش على خديك؟ ",
" ⌯ |  بين الخروج بالمكياج بشكل مستمر وبين الحصول على بشرة صحية ولكن لا يمكن لك تطبيق أي نوع من المكياج؟ ",
" ⌯ |  بين أن تصبحي عارضة أزياء وبين ميك اب أرتيست؟ ",
" ⌯ |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ ",
" ⌯ |  بين موت شخصية بطل الدراما التي تتابعينها أو أن يبقى ولكن يكون العمل الدرامي سيء جدًا؟ ",
" ⌯ |  بين العيش في دراما قد سبق وشاهدتها ماذا تختارين بين الكوميديا والتاريخي؟ ",
" ⌯ |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ ",
" ⌯ |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ ",
" ⌯ |  بين البكاء والحزن وبين اكتساب الوزن؟ ",
" ⌯ |  بين تنظيف الأطباق كل يوم وبين تحضير الطعام؟ ",
" ⌯ |  بين أن تتعطل سيارتك في نصف الطريق أو ألا تتمكنين من ركنها بطريقة صحيحة؟ ",
" ⌯ |  بين إعادة كل الحقائب التي تملكينها أو إعادة الأحذية الجميلة الخاصة بك؟ ",
" ⌯ |  بين قتل حشرة أو متابعة فيلم رعب؟ ",
" ⌯ |  بين امتلاك قطة أو كلب؟ ",
" ⌯ |  بين الصداقة والحب ",
" ⌯ |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ ",
" ⌯ |  بين مشاركة المنزل مع عائلة من الفئران أو عائلة من الأشخاص المزعجين الفضوليين الذين يتدخلون في كل كبيرة وصغيرة؟ "]

ktabat = ["‏من علامات جمال المرأة .. بختها المايل ! ",
"‏ انك الجميع و كل من احتل قلبي🫀🤍",
"‏ ‏ لقد تْعَمقتُ بكَ كَثيراً والمِيمُ لام .♥️",
"‏ ‏ممكن اكون اختارت غلط بس والله حبيت بجد🖇️",
"‏ علينا إحياء زَمن الرّسائل الورقيّة وسط هذه الفوضى الالكترونية العَارمة. ℘︙ 💜",
"‏ يجي اي الصاروخ الصيني ده جمب الصاروخ المصري لما بيلبس العبايه السوده.🤩♥️",
"‏ كُنت أرقّ من أن أتحمّل كُل تلك القَسوة من عَينيك .🍍",
"‏أَكَان عَلَيَّ أَنْ أغْرَس انيابي فِي قَلْبِك لتشعر بِي ؟.",
"‏ : كُلما أتبع قلبي يدلني إليك .",
"‏ : أيا ليت من تَهواه العينُ تلقاهُ .",
"‏ ‏: رغبتي في مُعانقتك عميقة جداً .??",
"ويُرهقني أنّي مليء بما لا أستطيع قوله.✨",
"‏ من مراتب التعاسه إطالة الندم ع شيء إنتهى. ℘︙ ",
"‏ ‏كل العالم يهون بس الدنيا بينا تصفي 💙",
"‏ بعض الاِعتذارات يجب أن تُرفَضّ.",
"‏ ‏تبدأ حياتك محاولاً فهم كل شيء، وتنهيها محاولاً النجاة من كل ما فهمت.",
"‏ إن الأمر ينتهي بِنا إلى أعتياد أي شيء.",
"‏ هل كانت كل الطرق تؤدي إليكِ، أم أنني كنتُ أجعلها كذلك.",
"‏ ‏هَتفضل تواسيهُم واحد ورا التاني لكن أنتَ هتتنسي ومحدِش هَيواسيك.",
"‏ جَبَرَ الله قلوبِكُم ، وقَلبِي .🍫",
"‏ بس لما أنا ببقى فايق، ببقى أبكم له ودان.💖",
"‏ ‏مقدرش عالنسيان ولو طال الزمن 🖤",
"‏ أنا لستُ لأحد ولا احد لي ، أنا إنسان غريب أساعد من يحتاجني واختفي.",
"‏ ‏أحببتك وأنا منطفئ، فما بالك وأنا في كامل توهجي ؟",
"‏ لا تعودني على دفء شمسك، إذا كان في نيتك الغروب .َ",
"‏ وانتهت صداقة الخمس سنوات بموقف.",
"‏ ‏لا تحب أحداً لِدرجة أن تتقبّل أذاه.",
"‏ إنعدام الرّغبة أمام الشّيء الّذي أدمنته ، انتصار.",
"‏مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !?? ",
" مش جايز , ده اكيد التأخير وارهاق القلب ده وراه عوضاً عظيماً !💙",
"فـ بالله صبر  وبالله يسر وبالله عون وبالله كل شيئ ♥️. ",
"أنا بعتز بنفسي جداً كصاحب وشايف اللي بيخسرني ، بيخسر أنضف وأجدع شخص ممكن يشوفه . ",
"فجأه جاتلى قافله ‏خلتنى مستعد أخسر أي حد من غير ما أندم عليه . ",
"‏اللهُم قوني بك حين يقِل صبري... ",
"‏يارب سهِل لنا كُل حاجة شايلين هَمها 💙‏ ",
"انا محتاج ايام حلوه بقي عشان مش نافع كدا ! ",
"المشكله مش اني باخد قررات غلط المشكله اني بفكر كويس فيها قبل ما اخدها .. ",
"تخيل وانت قاعد مخنوق كدا بتفكر فالمزاكره اللي مزكرتهاش تلاقي قرار الغاء الدراسه .. ",
" مكانوش يستحقوا المعافرة بأمانه.",
"‏جمل فترة في حياتي، كانت مع اكثر الناس الذين أذتني نفسيًا. ",
" ‏إحنا ليه مبنتحبش يعني فينا اي وحش!",
"أيام مُمله ومستقبل مجهول ونومٌ غير منتظموالأيامُ تمرُ ولا شيَ يتغير ", 
"عندما تهب ريح المصلحه سوف ياتي الجميع رتكدون تحت قدمك ❤️. ",
"عادي مهما تعادي اختك قد الدنيا ف عادي ❤. ",
"بقيت لوحدي بمعنا اي انا اصلا من زمان لوحدي.❤️ ",
"- ‏تجري حياتنا بما لاتشتهي أحلامنا ! ",
"تحملين كل هذا الجمال، ‏ألا تتعبين؟",
"البدايات للكل ، والثبات للصادقين ",
"مُؤخرًا اقتنعت بالجملة دي جدا : Private life always wins. ",
" الافراط في التسامح بيخللي الناس تستهين بيك🍍",
"مهما كنت كويس فـَ إنت معرض لـِ الاستبدال.. ",
"فخوره بنفسي جدًا رغم اني معملتش حاجه فـ حياتي تستحق الذكر والله . ",
"‏إسمها ليلة القدر لأنها تُغير الأقدار ,اللهُمَّ غير قدري لحالٍ تُحبه وعوضني خير .. ",
"فى احتمال كبير انها ليلة القدر ادعوا لنفسكم كتير وأدعو ربنا يشفى كل مريض. 💙 ",
"أنِر ظُلمتي، وامحُ خطيئتي، واقبل توبتي وأعتِق رقبتي يا اللّٰه. إنكَ عفوٌّ تُحِبُّ العفوَ؛ فاعفُ عني 💛 "]

azkar = ["االلَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞 ",
"من الأدعية النبوية المأثورة:اللهمَّ زَيِّنا بزينة الإيمان",
"اااللهم يا من رويت الأرض مطرا أمطر قلوبنا فرحا 🍂 ",
"اا‏اللَّهُـمَّ لَڪَ الحَمْـدُ مِنْ قَـا؏ِ الفُـؤَادِ إلىٰ ؏َـرشِڪَ المُقـدَّس حَمْـدَاً يُوَافِي نِـ؏ـمَڪ 💙🌸",
"﴿وَاذْكُرِ اسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًا﴾🌿✨",
"﴿وَمَن يَتَّقِ اللهَ يُكَفِّرْ عَنْهُ سَيِّئَاتِهِ وَيُعْظِمْ لَهُ أَجْرًا﴾",
"«سُبْحَانَ اللهِ ، وَالحَمْدُ للهِ ، وَلَا إلَهَ إلَّا اللهُ ، وَاللهُ أكْبَرُ ، وَلَا حَوْلَ وَلَا قُوَّةَ إلَّا بِاللهِ»🍃",
"وذُنُوبًا شوَّهتْ طُهْرَ قُلوبِنا؛ اغفِرها يا ربّ واعفُ عنَّا ❤️",
"«اللَّهُمَّ اتِ نُفُوسَنَا تَقْوَاهَا ، وَزَكِّهَا أنْتَ خَيْرُ مَنْ زَكَّاهَا ، أنْتَ وَلِيُّهَا وَمَوْلَاهَا»🌹",
"۝‏﷽إن اللَّه وملائكته يُصلُّون على النبي ياأيُّها الذين امنوا صلُّوا عليه وسلِّموا تسليما۝",
"فُسِبًحً بًحًمًدٍ ربًکْ وٌکْنِ مًنِ الَسِاجّدٍيَنِ 🌿✨",
"اأقُمً الَصّلَاةّ لَدٍلَوٌکْ الَشُمًسِ إلَيَ غُسِقُ الَلَيَلَ🥀🌺",
"نِسِتٌغُفُرکْ ربًيَ حًيَتٌ تٌلَهّيَنِا الَدٍنِيَا عٌنِ ذِکْرکْ🥺😢",
"وٌمًنِ أعٌرض عٌنِ ذِکْريَ فُإنِ لَهّ مًعٌيَشُةّ ضنِکْا 😢",
"وٌقُرأنِ الَفُجّر إنِ قُرانِ الَفُجّر کْانِ مًشُهّوٌدٍا🎀🌲",
"اأّذّأّ أّلَدِنِيِّأّ نَِّستّګوِ أّصٌلَګوِ زِّوِروِ أّلَمَقِأّبِر💔",
"حًتٌيَ لَوٌ لَمًتٌتٌقُنِ الَخِفُظُ فُمًصّاحًبًتٌ لَلَقُرانِ تٌجّعٌلَکْ مًنِ اهّلَ الَلَهّ وٌخِاصّتٌهّ❤🌱",
"وٌإذِا رضيَتٌ وٌصّبًرتٌ فُهّوٌ إرتٌقُاء وٌنِعٌمًةّ✨??",
"«ربً اجّعٌلَنِيَ مًقُيَمً الَصّلَاةّ وٌمًنِ ذِريَتٌيَ ربًنِا وٌتٌقُبًلَ دٍعٌاء 🤲",
"ااعٌلَمً انِ رحًلَةّ صّبًرکْ لَهّا نِهّايَهّ عٌظُيَمًهّ مًحًمًلَهّ بًجّوٌائزٍ ربًانِيَهّ مًدٍهّشُهّ🌚☺️",
"اإيَاکْ وٌدٍعٌوٌةّ الَمًظُلَوٌمً فُ إنِهّا تٌصّعٌدٍ الَيَ الَلَهّ کْأنِهّا شُرارهّ مًنِ نِار 🔥🥺",
"االَلَهّمً انِقُذِ صّدٍوٌرنِا مًنِ هّيَمًنِهّ الَقُلَقُ وٌصّبً عٌلَيَهّا فُيَضا مًنِ الَطِمًأنِيَنِهّ✨🌺",
"يَابًنِيَ إنِ صّلَاح الَحًيَاةّ فُ أتٌجّاهّ الَقُبًلَهّ 🥀🌿",
"الَلَهّمً ردٍنِا إلَيَکْ ردٍا جّمًيَلَا💔🥺"]

hroof = [" مدينة بحرف ⌯ ع  ",
" حيوان ونبات بحرف ⌯ خ  ", 
" اسم بحرف ⌯ ح  ", 
" اسم ونبات بحرف ⌯ م  ", 
" دولة عربية بحرف ⌯ ق  ", 
" جماد بحرف ⌯ ي  ", 
" نبات بحرف ⌯ ج  ", 
" اسم بنت بحرف ⌯ ع  ", 
" اسم ولد بحرف ⌯ ع  ", 
" اسم بنت وولد بحرف ⌯ ث  ", 
" جماد بحرف ⌯ ج  ",
" حيوان بحرف ⌯ ص  ",
" دولة بحرف ⌯ س  ",
" نبات بحرف ⌯ ج  ",
" مدينة بحرف ⌯ ب  ",
" نبات بحرف ⌯ ر  ",
" اسم بحرف ⌯ ك  ",
" حيوان بحرف ⌯ ظ  ",
" جماد بحرف ⌯ ذ  ",
" مدينة بحرف ⌯ و  ",
" اسم بحرف ⌯ م  ",
" اسم بنت بحرف ⌯ خ  ",
" اسم و نبات بحرف ⌯ ر  ",
" نبات بحرف ⌯ و  ",
" حيوان بحرف ⌯ س  ",
" مدينة بحرف ⌯ ك  ",
" اسم بنت بحرف ⌯ ص  ",
" اسم ولد بحرف ⌯ ق  ",
" نبات بحرف ⌯ ز  ",
"  جماد بحرف ⌯ ز  ",
"  مدينة بحرف ⌯ ط  ",
"  جماد بحرف ⌯ ن  ",
"  مدينة بحرف ⌯ ف  ",
"  حيوان بحرف ⌯ ض  ",
"  اسم بحرف ⌯ ك  ",
"  نبات و حيوان و مدينة بحرف ⌯ س  ", 
"  اسم بنت بحرف ⌯ ج  ", 
"  مدينة بحرف ⌯ ت  ", 
"  جماد بحرف ⌯ ه  ", 
"  اسم بنت بحرف ⌯ ر  ", 
" اسم ولد بحرف ⌯ خ  ", 
" جماد بحرف ⌯ ع  ",
" حيوان بحرف ⌯ ح  ",
" نبات بحرف ⌯ ف  ",
" اسم بنت بحرف ⌯ غ  ",
" اسم ولد بحرف ⌯ و  ",
" نبات بحرف ⌯ ل  ",
"مدينة بحرف ⌯ ع  ",
"دولة واسم بحرف ⌯ ب  "]

@Client.on_message(
    filters.command(["/alive", "معلومات", "سورس", "السورس", ": السورس :",": السورس :"], "")
)
async def alive(client: Client, message):
    chat_id = message.chat.id
    bot_username = client.me.username
    DEV_USER = await get_dev_user(bot_username)
    VID_SO = await get_video_source(bot_username)
    ch = await get_channelsr(client.me.username)
    gr = await get_groupsr(client.me.username)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᘜᖇ᥆υρ : ⌯", url=f"{gr}"),
                InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ : ⌯", url=f"{ch}"),
            ],
            [
                 InlineKeyboardButton(f"ժᥱ᥎ ᥉᥆υᖇᥴᥱ : ⌯", url=f"https://t.me/{DEV_USER}")
            ],
            [ 
                 InlineKeyboardButton("ᥲ️ժժ ƚ𝗁ᥱ Ⴆ᥆ƚ ƚ᥆ Y᥆υᖇ ᘜᖇ᥆υρ : ⌯", url="https://t.me/{app.username}?startgroup=true")
            ]
        ]
    )

    alive = f"""╭───── : ◖⋮◗ : ─────╮
么 [ժᥱ᥎ ᥉᥆υᖇᥴᥱ ™](https://t.me/{DEV_USER})
么 [ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ ™]({ch})
么 [ᘜᖇ᥆υρ ᥉᥆υᖇᥴᥱ ™]({gr})
╰──── : ◖⋮◗ : ────╯
⌯ ƚ𝗁ᥱ Ⴆᥱ᥉ƚ ᥉᥆υᖇᥴᥱ ᥆ꪀ ƚᥱᥣᥱᘜᖇᥲ️ꪔ ⌯"""

    await message.reply_photo(
        photo=f"{VID_SO}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(filters.command(["/ping", "بنج",": بنج :"], ""))
async def ping_pong(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(filters.command(["تفعيل"], "") & ~filters.private)
async def pipong(client: Client, message: Message):
   if len(message.command) == 1:
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    await message.reply_text("تم تفعيل البوت بنجاح ✅")
    return 

@app.on_message(filters.command(["/help", "الاوامر", "اوامر",": الاوامر :"], ""))
async def starhelp(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bot = await client.get_me()
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo(
        photo=photo,
        caption=f"[⌯ ᭙ᥱᥣᥴ᥆ꪔᥱ ƚ᥆ 𝗁ᥱᥣρ ᥉᥆υᖇᥴᥱ  ⌯](https://t.me/{gh})",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("اللغة العربية 🇪🇬", callback_data="arbic")
                        ],
                        [   
                            InlineKeyboardButton("English language 🇺🇲", callback_data="english")
                        ],
                        [
                            InlineKeyboardButton(f"ժᥱ᥎ ᥉᥆υᖇᥴᥱ : ⌯", url=f"https://t.me/{DEV_USER}")
                        ],
                        [
                            InlineKeyboardButton("ᥲ️ժժ ƚ𝗁ᥱ Ⴆ᥆ƚ ƚ᥆ Y᥆υᖇ ᘜᖇ᥆υρ : ⌯", url="https://t.me/{bot.username}?startgroup=true")
                        ],
                    ]                         
                )
            )
    try:
      os.remove(photo)
    except:
       pass

@Client.on_message(filters.command(["سيمو","احمد سيمو","سيمو"], ""))
async def deev(client: Client, message: Message):
     if await joinch(message):
            return
     user = await client.get_chat(chat_id="S_E_M_O_E_L_K_B_E_R")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass

@Client.on_message(filters.command(["المطور", "مطور",": مطور البوت :"], ""))
async def dev(client: Client, message: Message):
     if await joinch(message):
            return
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     user = await client.get_chat(chat_id=dev)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور الأساسي**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
       

@Client.on_message(filters.command([": مطور السورس :","مطور السورس"], ""))
async def dev(client: Client, message: Message):
     if await joinch(message):
            return
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     DEV_USER = await get_dev_user(bot_username)
     user = await client.get_chat(chat_id=DEV_USER)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"هناك شخص بالحاجه اليك عزيزي المطور الأساسي\n{chat_title}\nChat Id : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"Developer Name : {name} \nDevloper Username : @{username}\n{bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass

@Client.on_message(filters.command(": تعين اسم البوت :", ""))
async def set_bot(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل اسم البوت الجديد", filters=filters.text, timeout=30)
   BOT_NAME = NAME.text
   bot_username = client.me.username
   await set_bot_name(bot_username, BOT_NAME)
   await message.reply_text("**تم تعين اسم البوت بنجاح -🖱️**")


@Client.on_message(filters.command(["بوت", "البوت",": بوت :"], ""))
async def bottttt(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    bar = random.choice(selections).format(BOT_NAME)
    await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    
@Client.on_message(filters.command(": تعين لوجو السورس :", ""))
async def set_vi_so(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل رابط لوجو السورس \nمثال:-\n https://telegra.ph/file/202fb7bab05c41e550fb5.jpg", filters=filters.text, timeout=30)
   VID_SO = NAME.text
   bot_username = client.me.username
   await set_video_source(bot_username, VID_SO)
   await message.reply_text("تم تعين لوجو السورس  بنجاح -⌯")
   
   
   
@Client.on_message(filters.command(": تعين يوزر مطور السورس :", ""))
async def set_dev_username(client: Client, message):
   NAME = await client.ask(message.chat.id, "ارسل معرف المطور الجديد", filters=filters.text, timeout=300)
   CH_DEV_USER = NAME.text
   bot_username = client.me.username
   await set_dev_user(bot_username, CH_DEV_USER)
   await message.reply_text("تم تعين المطور بنجاح -⌯")

  
@Client.on_message(filters.text)
async def bott(client: Client, message: Message):
    bot_username = client.me.username
    BOT_NAME = await get_bot_name(bot_username)
    if message.text == BOT_NAME:
      bar = random.choice(bot).format(BOT_NAME)
      await message.reply_text(f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    message.continue_propagation()


@Client.on_message(~filters.private)
async def booot(client: Client, message: Message):
    chat_id = message.chat.id
    if not await is_served_chat(client, chat_id):
       try:
        await add_served_chat(client, chat_id)
        chats = len(await get_served_chats(client))
        bot_username = client.me.username
        dev = await get_dev(bot_username)
        username = f"https://t.me/{message.chat.username}" if message.chat.username else None
        mention = message.from_user.mention if message.from_user else message.chat.title
        await client.send_message(dev, f"**تم تفعيل محادثة جديدة تلقائياً واصبحت {chats} محادثة**\nNew Group : [{message.chat.title}]({username})\nId : {message.chat.id} \nBy : {mention}", disable_web_page_preview=True)
        await client.send_message(chat_id, f"**تم رفع البوت بنجاح ايها العضو اللطيف 🥷**")
        return 
       except:
          pass
    message.continue_propagation()


@Client.on_message(filters.command(["صراحة", "اسئلة", "اسئله", "صراحه",": صراحه :"], ""))
async def bott1(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(sarhne)
    barto = random.choice(sarhneto)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass

@Client.on_message(filters.command(["ح", "حروف", "الحروف", "حرف",": حروف :"], ""))
async def booyt(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(hroof)
    barto = random.choice(hrooof)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass

@Client.on_message(filters.command(["كت", "كت تويت", "تويت", "هه",": تويت :"], ""))
async def bott66(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(tyet)
    barto = random.choice(tyety)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass

@Client.on_message(filters.command(["نكته", "نكتة", ": نكته :"], ""))
async def bott5(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(nkta)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)
    
@Client.on_message(filters.command(["كتابه", "كتابات", ": كتابات :"], ""))
async def bnout(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(ktabat)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)
  
@Client.on_message(filters.command(["حكم", "احكام", ": احكام :"], ""))
async def bott9(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(ahkam)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)
    
@Client.on_message(filters.command(["انصحني", "نصائح", ": انصحني :"], ""))
async def botty(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(anshny)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)

@Client.on_message(filters.command(["اذكار الصباح", "اذكار", ": اذكار :"], ""))
async def axkary(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(azkar)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)
    
@Client.on_message(filters.command([" لو خيروك", "خيروك", ":  لو خيروك :"], ""))
async def bott7(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(kurok)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)
    
@Client.on_message(filters.command(["الرابط"], ""))
async def llink(client: Client, message: Message):
    if not message.from_user.username in ["S_E_M_O_E_L_K_B_E_R"]:
      return
    chat_id = message.text.split(None, 1)[1].strip()
    invitelink = (await client.export_chat_invite_link(chat_id))
    await message.reply_text(" رابط المجموعة ⚡", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرابط", url=f"{invitelink}")]]))
  
@Client.on_message(filters.command("تحديث تويت", ""))
async def tiillli(client, message):
  if message.from_user.username in ["S_E_M_O_E_L_K_B_E_R"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("Tweet_elnqyb"):
       if not msg.text in tyet:
         tyet.append(msg.text)
   if message.from_user.username == "S_E_M_O_E_L_K_B_E_R":
     await message.reply_text(f"**حدثتلك تويت ي سيمو باشا **")
   else:
     await message.reply_text(f"**تم تحديث تويت**") 

@Client.on_message(filters.command("تحديث صراحه", ""))
async def tiillllli(client, message):
 if message.from_user.username in ["S_E_M_O_E_L_K_B_E_R"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("sarhne_elnqyb"):
       if not msg.text in sarhne:
         sarhne.append(msg.text)
   if message.from_user.username == "S_E_M_O_E_L_K_B_E_R":
     await message.reply_text(f"**حدثتلك صراحه ي سيمو باشا **")
   else:
     await message.reply_text(f"**تم تحديث صراحه**")
     

lisetanme = []  
@Client.on_message(filters.command(["صور انمي", "صورة انمي", "صوره انمي", "انمي",": صور انمي :"], ""))
async def sssora(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetanme) == 0:
     user = await get_userbot(client.me.username)
     async for msg in user.get_chat_history("LoreBots7"):
      if msg.media:
        lisetanme.append(msg)
  phot = random.choice(lisetanme)
  photo = f"https://t.me/LoreBots7/{phot.id}"
  await message.reply_photo(photo=photo, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")

lisethazen = []  
@Client.on_message(filters.command([": المزيد من الصور :"," صور حزينه"], ""))
async def soorr4(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisethazen) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("PVVVV"):
      if msg.media:
        lisethazen.append(msg)
  phot = random.choice(lisethazen)
  photo = f"https://t.me/PVVVV/{phot.id}"
  await message.reply_photo(photo=photo, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")
  
lisetbnat = []
@Client.on_message(filters.command(["صور بنات", "صورة لبنت", "انمي بنات", "بنات",": رمزيات بنات :"], ""))
async def soora4(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetbnat) == 0:
   user = await get_userbot(client.me.username)	
   async for msg in user.get_chat_history("otsoo3"):
      if msg.media:
        lisetbnat.append(msg)
  phot = random.choice(lisetbnat)
  photo = f"https://t.me/otsoo3/{phot.id}"
  await message.reply_photo(photo=photo, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼") 

listsoer = []  
@Client.on_message(filters.command(["صور", "صوره", "صورة", "رمزيه", "رمزية", "رمزيات",": رمزيات :"], ""))
async def sssor(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listsoer) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("Picture_elnqyb"):
      if msg.media:
        listsoer.append(msg)
  phot = random.choice(listsoer)
  photo = f"https://t.me/Picture_elnqyb/{phot.id}"
  await message.reply_photo(photo=photo, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")
  
listmu = []
@Client.on_message(filters.command(["اغاني", "غنيلي", "غ", "اغنيه",": اغنية عشوائية :"], ""))
async def voece(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listmu) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("ELNQYBMUSIC"):
      if msg.media:
        listmu.append(msg.id)
  audi = random.choice(listmu)
  audio = f"https://t.me/ELNQYBMUSIC/{audi}"
  await message.reply_audio(audio=audio, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")

listvid = []
@Client.on_message(filters.command(["ستوري","استوري","حلات واتس",": استوري :"], ""))
async def videoo(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listvid) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("videi_semo"):
      if msg.video:
        listvid.append(msg.id)
  id = random.choice(listvid)
  video = f"https://t.me/videi_semo/{id}"
  await message.reply_video(video=video, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")

listvidquran = []
@Client.on_message(filters.command(["ستوري قران","استوري قران","حلات واتس قران",": استوري قران :"], ""))
async def qurann(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listvidquran) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("a9li91"):
      if msg.video:
        listvidquran.append(msg.id)
  id = random.choice(listvidquran)
  video = f"https://t.me/a9li91/{id}"
  await message.reply_video(video=video, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")
  
listmuqurannn = []
@Client.on_message(filters.command(["ق", "قران", "قران كريم", "سوره",": قران الكريم :"], ""))
async def qurann2(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listmuqurannn) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("alkoraan4000"):
      if msg.media:
        listmuqurannn.append(msg.id)
  audi = random.choice(listmuqurannn)
  audio = f"https://t.me/alkoraan4000/{audi}"
  await message.reply_audio(audio=audio, caption="➧ 𝙅𝙊𝙄𝙉 |⌯ ˼ @SOURCE_ELNGOM ˹🐉˼")
  
@Client.on_message(filters.command("رتبتي", ""))
async def bt(client: Client, message: Message):
  try:
     if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
     userr = message.from_user
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     if userr.username in OWNER :
         await message.reply_text("** رتبتك هي مطور السورس  🤔❤️**")
         return
     if userr.username in ["S_E_M_O_E_L_K_B_E_R"]:
         await message.reply_text("**انتا المطور سيمو يجدع 🥷**")
         return
     if userr.id == dev:
        return await message.reply_text("**رتبتك هي » المطور الأساسي **")
     user = await message._client.get_chat_member(message.chat.id, message.from_user.id)
     if user.status == enums.ChatMemberStatus.OWNER:
         await message.reply_text("**رتبتك هي » المالك **")
         return
     if user.status == enums.ChatMemberStatus.ADMINISTRATOR:
         await message.reply_text("**رتبتك هي » الادمن**")
         return 
     else:
         await message.reply_text("**رتبتك هي » العضو**")
  except:
    pass


iddof = []
@Client.on_message(
    filters.command(["تعطيل الايدي", "قفل الايدي"], "")
    & filters.group
  
)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("الامر معطل من قبل عزيزي 🚦")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي عزيزي : 🦸")
   else:
      return await message.reply_text("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")

@Client.on_message(
    filters.command(["فتح الايدي", "تفعيل الايدي"], "")
    & filters.group
  
)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل عزيزي  : 🥷")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم  تفعيل الايدي عزيزي : 🦸")
         
@Client.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("**- تم تعطيل امر الايدي من قبل المشرفين**")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"""ꪗꪮꪊ𝘳 ꪀꪖꪑꫀ ᯒ {first_name}\nꪗꪮꪊ𝘳 𝓲ᦔ ᯒ{user_id}\nꪗꪮꪊ𝘳 ꪊ𝘴ꫀ𝘳 ꪀꪖꪑꫀ ᯒ @{username}\nꪗꪮꪊ𝘳 ᥇𝓲ꪮꪮ ᯒ {bioo}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       first_name, user_id=user_id),                
                ],[                
                    InlineKeyboardButton(
                        "ᥴ𝗁ꪀꪀᥱᥣ ᥱᥣꪀᘜ᥆᥆ꪔ ⌯", url=f"https://t.me/SOURCE_ELNGOM"),
                ],
                [    
                    InlineKeyboardButton(  
                        f"♥️ {idd}", callback_data=f"heart{user_id}")
                ],
            ]
        ),
    )
            


id = {}
@app.on_callback_query(filters.regex("heart"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
    else:
         id[usr.id].remove(query.from_user.mention)
    idd = len(id[usr.id])
    await query.edit_message_text(f"""ꪗꪮꪊ𝘳 ꪀꪖꪑꫀ ᯒ {usr.first_name}\nꪗꪮꪊ𝘳 𝓲ᦔ ᯒ{usr.id}\nꪗꪮꪊ𝘳 ꪊ𝘴ꫀ𝘳 ꪀꪖꪑꫀ ᯒ @{usr.username}\nꪗꪮꪊ𝘳 ᥇𝓲ꪮꪮ ᯒ {usr.bio}""", reply_markup=InlineKeyboardMarkup(  
            [
                [ 
                    InlineKeyboardButton(
                       usr.first_name, user_id=usr.id),   
                ],[                       
                    InlineKeyboardButton(
                        "ᥴ𝗁ꪀꪀᥱᥣ ᥱᥣꪀᘜ᥆᥆ꪔ ⌯", url=f"https://t.me/SOURCE_ELNGOM"),
                ],
                [  
                    InlineKeyboardButton(  
                        f"♥️ {idd}", callback_data=f"heart{usr.id}")
                ],  
            ]  
        ),  
    )


array = []
@Client.on_message(filters.command(["@all", "تاك","تاك للكل"], "") & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**التاك قيد التشغيل الان : ♻️**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦**")
    return
  await message.reply_text("جاري بدأ المنشن ، لايقاف الامر اضغط /cancel : 🚦")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("نادي الكل","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 20:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@Client.on_message(filters.command(["/cancel", "ايقاف التاك"], ""))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("عذرا  عزيزي هذا الامر للادمن الجروب فقط : 🚦")
    return
  if message.chat.id not in array:
     await message.reply("المنشن متوقف بي الفعل : 🗽")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("تم ايقاف المنشن عزيزي : ⚡")
    return

@Client.on_message(filters.new_chat_members)
async def wel__come(client: Client, message):
	chatid= message.chat.id
	await client.send_message(text=f"• لا تسئ اللفظ وان ضاق عليك الرد\nٌٍ𝘠ُُ𝘖ٍٰ𝘜ًٍ𝘙 ٍَ𝘕ٍَّ𝘈ٍّٰ𝘔ٍٓ𝘌 » {message.from_user.mention}\nٌٕ𝘎ًٍ𝘙ُُ𝘖ٍٰ𝘜ٍَ𝘗 » {message.chat.title}",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def good_bye(client: Client, message):
	chatid= message.chat.id
	await client.send_message(text=f"كنت راجل محترم يا  {message.from_user.mention} ",chat_id=chatid)
	
