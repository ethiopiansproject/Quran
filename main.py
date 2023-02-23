import os
from telebot import TeleBot,telebot,types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
from telebot.util import user_link,quick_markup

token = os.getenv("btk")
bot = telebot.TeleBot(token,parse_mode="HTML")

kb1 = quick_markup({
"Al-Fatihah":{"callback_data":"fa"},
"Al-Baqarah":{"callback_data":"ba"},
"Aali Imran":{"callback_data":"im"},
"An-Nisa’ ":{"callback_data":"ni"},
"Al-Ma’idah":{"callback_data":"ma"},
"Al-An’am":{"callback_data":"ana"},
"Al-A’raf":{"callback_data":"ara"},
"Al-Anfal":{"callback_data":"anf"},
"At-Taubah":{"callback_data":"ta"},
"Yunus":{"callback_data":"yun"},
"Hud":{"callback_data":"hu"},
"Yusuf":{"callback_data":"yu"},
"Ar-Ra’d":{"callback_data":"rad"},
"Ibrahim":{"callback_data":"ib"},
"Al-Hijr":{"callback_data":"hi"},
"An-Nahl":{"callback_data":"nah"},
"Al-Isra’ ":{"callback_data":"is"},
"Al-Kahf":{"callback_data":"kaf"},
"Maryam":{"callback_data":"mar"},
"Ta-Ha":{"callback_data":"taha"},
"Next":{"callback_data":"nex1"},
})


kb2 = quick_markup({
"Al-Anbiya’ ":{"callback_data":"anb"},
"Al-Haj":{"callback_data":"haj"},
"Al-Mu’minun":{"callback_data":"mum"},
"An-Nur":{"callback_data":"nur"},
"Al-Furqan":{"callback_data":"fur"},
"Ash-Shu’ara’":{"callback_data":"shu"},
"An-Naml":{"callback_data":"nam"},
"Al-Qasas":{"callback_data":"qa"},
"Al-Ankabut":{"callback_data":"ank"},
"Ar-Rum":{"callback_data":"rum"},
"Luqman":{"callback_data":"luq"},
"As-Sajdah":{"callback_data":"saj"},
"Al-Ahzab":{"callback_data":"ah"},
"Saba’ ":{"callback_data":"saba"},
"Al-Fatir":{"callback_data":"fat"},
"Ya-Sin":{"callback_data":"yas"},
"As-Saffah":{"callback_data":"saff"},
"Sad":{"callback_data":"sad"},
"Az-Zumar":{"callback_data":"zum"},
"Ghafar":{"callback_data":"gaf"},
"Back":{"callback_data":"bk1"},
"Next":{"callback_data":"nex2"},
})

kb3 = quick_markup({
"Fusilat":{"callback_data":"fus"},
"Ash-Shura":{"callback_data":"shur"},
"Az-Zukhruf":{"callback_data":"zuk"},
"Ad-Dukhan":{"callback_data":"duk"},
"Al-Jathiyah":{"callback_data":"jat"},
"Al-Ahqaf":{"callback_data":"ahq"},
"Muhammad":{"callback_data":"mum"},
"Al-Fat’h":{"callback_data":"fath"},
"Al-Hujurat":{"callback_data":"huj"},
"Qaf":{"callback_data":"qaf"},
"Adz-Dzariyah":{"callback_data":"zar"},
"At-Tur":{"callback_data":"tur"},
"An-Najm":{"callback_data":"naj"},
"Al-Qamar":{"callback_data":"qam"},
"Ar-Rahman":{"callback_data":"rah"},
"Al-Waqi’ah":{"callback_data":"waq"},
"Al-Hadid":{"callback_data":"had"},
"Al-Mujadilah":{"callback_data":"muj"},
"Al-Hashr":{"callback_data":"hash"},
"Al-Mumtahanah":{"callback_data":"mumt"},
"Back":{"callback_data":"bk2"},
"Next":{"callback_data":"nex3"},
})

kb4 = quick_markup({
"As-Saf":{"callback_data":"saf"},
"Al-Jum’ah":{"callback_data":"juma"},
"Al-Munafiqun":{"callback_data":"muna"},
"At-Taghabun":{"callback_data":"taga"},
"At-Talaq":{"callback_data":"tala"},
"At-Tahrim":{"callback_data":"tahr"},
"Al-Mulk":{"callback_data":"mul"},
"Al-Qalam":{"callback_data":"qal"},
"Al-Haqqah":{"callback_data":"haq"},
"Al-Ma’arij":{"callback_data":"maar"},
"Nuh":{"callback_data":"nuh"},
"Al-Jinn":{"callback_data":"jin"},
"Al-Muzammil":{"callback_data":"muzam"},
"Al-Mudaththir":{"callback_data":"muda"},
"Al-Qiyamah":{"callback_data":"qi"},
"Al-Insan":{"callback_data":"ins"},
"Al-Mursalat":{"callback_data":"murs"},
"An-Naba' ":{"callback_data":"nab"},
"An-Nazi’at":{"callback_data":"nazi"},
"Abasa":{"callback_data":"aba"},
"Back":{"callback_data":"bk3"},
"Next":{"callback_data":"nex4"},
})

kb5 = quick_markup({
"At-Takwir":{"callback_data":"tawk"},
"Al-Infitar":{"callback_data":"inf"},
"Al-Mutaffifin":{"callback_data":"muta"},
"Al-Inshiqaq":{"callback_data":"inshi"},
"Al-Buruj":{"callback_data":"bur"},
"At-Tariq":{"callback_data":"tari"},
"Al-A’la":{"callback_data":"ala"},
"Al-Ghashiyah":{"callback_data":"gash"},
"Al-Fajr":{"callback_data":"faj"},
"Al-Balad":{"callback_data":"bala"},
"Ash-Shams":{"callback_data":"sham"},
"Al-Layl":{"callback_data":"layl"},
"Adh-Dhuha":{"callback_data":"duha"},
"Al-Inshirah":{"callback_data":"inshir"},
"At-Tin":{"callback_data":"tin"},
"Al-‘Alaq":{"callback_data":"alaq"},
"Al-Qadar":{"callback_data":"qad"},
"Al-Bayinah":{"callback_data":"bayi"},
"Az-Zalzalah":{"callback_data":"zal"},
"Al-‘Adiyah":{"callback_data":"adi"},
"Back":{"callback_data":"bk4"},
"Next":{"callback_data":"nex5"},
})

kb6 = quick_markup({
"Al-Qari’ah":{"callback_data":"qari"},
"At-Takathur":{"callback_data":"taka"},
"Al-‘Asr":{"callback_data":"asr"},
"Al-Humazah":{"callback_data":"huma"},
"Al-Fil":{"callback_data":"fil"},
"Quraish":{"callback_data":"qur"},
"Al-Ma’un":{"callback_data":"mau"},
"Al-Kauthar":{"callback_data":"kau"},
"Al-Kafirun":{"callback_data":"kafi"},
"An-Nasr":{"callback_data":"nasr"},
"Al-Masad":{"callback_data":"masad"},
"Al-Ikhlas":{"callback_data":"ik"},
"Al-Falaq":{"callback_data":"fala"},
"An-Nas":{"callback_data":"nas"},
"Page1":{"callback_data":"p1"},
"Page2":{"callback_data":"p2"},
"Page3":{"callback_data":"p3"},
"Page4":{"callback_data":"p4"},
"Back":{"callback_data":"bk5"},
})

pages = quick_markup({
    "Page1":{"callback_data":"pg1"},
    "Page2":{"callback_data":"pg2"},
    "Page3":{"callback_data":"pg3"},
    "Page4":{"callback_data":"pg4"},
    "Page5":{"callback_data":"pg5"},
    "Page6":{"callback_data":"pg6"}
    })
    
markup = InlineKeyboardMarkup()
channel = InlineKeyboardButton("Join",url="t.me/ThewayofProphets")
markup.add(channel)

channel ="@ThewayofProphets"
@bot.message_handler(commands=["start"])
def welcome_msg(msg):
    user_id = msg.from_user.id
    check_user = bot.get_chat_member(chat_id =channel,user_id =user_id )
    if check_user.status=='left' or check_user.status=='kicked':
        bot.reply_to(msg,f"Aselamu Aleykum {user_link(msg.from_user)} welcome\n to get all quran audio file join my channel\n after joining send /start",reply_markup=markup)
    else:
        pass
        text ="feel free to listen and download audios\n \t\t Choose Surah"
        bot.reply_to(msg,text,reply_markup=kb1)

@bot.message_handler(func=lambda m:True,content_types=["photo", "video", "text", "document", "sticker", "audio", "video_note"])
def send_quran(msg):
    user_id = msg.from_user.id
    check_user = bot.get_chat_member(chat_id =channel,user_id =user_id )
    if check_user.status=='left' or check_user.status=='kicked':
        bot.reply_to(msg,f"Aselamu Aleykum {user_link(msg.from_user)} welcome\n to get all quran audio file join my channel",reply_markup=markup)
    else:
        bot.reply_to(msg,"choose surah")

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    data=call.data
    if data =="pg1":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb1)
    elif data =="pg2":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb2)
    elif data =="pg3":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb3)
    elif data =="pg4":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb4)
    elif data =="pg5":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb5)
    elif data =="pg6":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb6)
    elif data =="fa":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/4",reply_markup=pages)
    elif data =="ba":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/5",reply_markup=pages)
    elif data =="im":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/6",reply_markup=pages)
    elif data =="ni":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/7",reply_markup=pages)
    elif data =="ma":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/8",reply_markup=pages)
    elif data =="ana":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/9",reply_markup=pages)
    elif data =="ara":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/10",reply_markup=pages)
    elif data =="anf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/11",reply_markup=pages)
    elif data =="ta":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/12",reply_markup=pages)
    elif data =="yun":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/13",reply_markup=pages)
    elif data =="hu":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/14",reply_markup=pages)
    elif data =="yu":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/15",reply_markup=pages)
    elif data =="rad":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/16",reply_markup=pages)
    elif data =="ib":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/17",reply_markup=pages)
    elif data =="hi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/18",reply_markup=pages)
    elif data =="nah":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/19",reply_markup=pages)
    elif data =="is":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/20",reply_markup=pages)
    elif data =="kaf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/21",reply_markup=pages)
    elif data =="mar":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/22",reply_markup=pages)
    elif data =="taha":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/23",reply_markup=pages)   
    elif data =="nex1":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb2)
        
    elif data =="anb":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/24",reply_markup=pages)
    elif data =="haj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/25",reply_markup=pages)
    elif data =="mum":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/26",reply_markup=pages)
    elif data =="nur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/27",reply_markup=pages)
    elif data =="fur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/28",reply_markup=pages)
    elif data =="shu":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/29",reply_markup=pages)
    elif data =="nam":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/30",reply_markup=pages)
    elif data =="qa":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/31",reply_markup=pages)
    elif data =="ank":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/32",reply_markup=pages)
    elif data =="rum":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/33",reply_markup=pages)
    elif data =="luq":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/34",reply_markup=pages)
    elif data =="saj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/35",reply_markup=pages)
    elif data =="ah":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/36",reply_markup=pages)
    elif data =="saba":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/37",reply_markup=pages)
    elif data =="fat":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/38",reply_markup=pages)
    elif data =="yas":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/39",reply_markup=pages)
    elif data =="saff":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/40",reply_markup=pages)
    elif data =="sad":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/41",reply_markup=pages)
    elif data =="zum":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/42",reply_markup=pages)
    elif data =="gaf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/43",reply_markup=pages)
    elif data =="bk1":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb1)
    elif data =="nex2":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb3)
        
    elif data =="fus":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/44",reply_markup=pages)
    elif data =="shur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/45",reply_markup=pages)
    elif data =="zuk":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/46",reply_markup=pages)
    elif data =="duk":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/47",reply_markup=pages)
    elif data =="jat":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/48",reply_markup=pages)
    elif data =="ahq":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/49",reply_markup=pages)
    elif data =="muh":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/50",reply_markup=pages)
    elif data =="fath":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/51",reply_markup=pages)
    elif data =="huj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/52",reply_markup=pages)
    elif data =="qaf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/53",reply_markup=pages)
    elif data =="zar":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/54",reply_markup=pages)
    elif data =="tur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/55",reply_markup=pages)
    elif data =="naj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/56",reply_markup=pages)
    elif data =="qam":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/57",reply_markup=pages)
    elif data =="rah":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/58",reply_markup=pages)
    elif data =="waq":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/59",reply_markup=pages)
    elif data =="had":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/60",reply_markup=pages)
    elif data =="muj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/61",reply_markup=pages)
    elif data =="hash":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/62",reply_markup=pages)
    elif data =="mumt":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/63",reply_markup=pages)
    elif data =="bk2":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb2)
    elif data =="nex3":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb4)
        
    elif data =="saf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/64",reply_markup=pages)
    elif data =="juma":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/65",reply_markup=pages)
    elif data =="muna":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/66",reply_markup=pages)
    elif data =="taga":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/67",reply_markup=pages)
    elif data =="taha":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/68",reply_markup=pages)
    elif data =="tahr":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/69",reply_markup=pages)
    elif data =="mul":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/70",reply_markup=pages)
    elif data =="qal":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/71",reply_markup=pages)
    elif data =="haq":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/72",reply_markup=pages)
    elif data =="maar":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/73",reply_markup=pages)
    elif data =="nuh":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/74",reply_markup=pages)
    elif data =="jin":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/75",reply_markup=pages)
    elif data =="muzam":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/76",reply_markup=pages)
    elif data =="muda":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/77",reply_markup=pages)
    elif data =="qi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/78",reply_markup=pages)
    elif data =="ins":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/79",reply_markup=pages)
    elif data =="murs":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/80",reply_markup=pages)
    elif data =="nab":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/81",reply_markup=pages)
    elif data =="nazi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/82",reply_markup=pages)
    elif data =="aba":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/83",reply_markup=pages)
    elif data =="bk3":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb3)
    elif data =="nex4":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb5)
 
    elif data =="tawk":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/84",reply_markup=pages)
    elif data =="inf":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/85",reply_markup=pages)
    elif data =="muta":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/86",reply_markup=pages)
    elif data =="inshi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/87",reply_markup=pages)
    elif data =="bur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/88",reply_markup=pages)
    elif data =="tari":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/89",reply_markup=pages)
    if data =="ala":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/90",reply_markup=pages)
    elif data =="gash":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/91",reply_markup=pages)
    elif data =="faj":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/92",reply_markup=pages)
    elif data =="bala":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/93",reply_markup=pages)
    elif data =="sham":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/94",reply_markup=pages)
    elif data =="layl":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/95",reply_markup=pages)
    elif data =="duha":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/96",reply_markup=pages)
    elif data =="inshir":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/97",reply_markup=kb5)
    elif data =="tin":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/98",reply_markup=pages)
    elif data =="alaq":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/99",reply_markup=pages)
    elif data =="qad":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/100",reply_markup=pages)
    elif data =="bayi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/101",reply_markup=pages)
    elif data =="zal":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/102",reply_markup=pages)
    elif data =="adi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/103",reply_markup=pages)
    elif data =="bk4":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb4)
    elif data =="nex5":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb6)
        
    elif data =="qari":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/104",reply_markup=pages)
    elif data =="taka":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/105",reply_markup=pages)
    elif data =="asr":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/106",reply_markup=pages)
    elif data =="huma":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/107",reply_markup=pages)
    elif data =="fil":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/108",reply_markup=pages)
    elif data =="qur":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/109",reply_markup=pages)
    elif data =="mau":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/110",reply_markup=pages)
    elif data =="kau":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/111",reply_markup=pages)
    elif data =="kafi":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/112",reply_markup=pages)
    elif data =="nasr":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/113",reply_markup=pages)
    elif data =="masad":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/114",reply_markup=pages)
    elif data =="ik":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/115",reply_markup=pages)
    elif data =="fala":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/116",reply_markup=pages)
    elif data =="nas":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_audio(call.message.chat.id,"https://t.me/QarimSiddiq/117",reply_markup=pages)
    elif data =="p1":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb1)
    elif data =="p2":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb2)
    elif data =="p3":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb3)
    elif data =="p4":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb4)
    elif data =="bk5":
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id,reply_markup=kb5)
    
    
    
bot.infinity_polling()
    
