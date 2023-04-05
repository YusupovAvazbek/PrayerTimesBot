from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
import pray as pray
import tumanlar as t
btn_today,btn_week,btn_region='Bugungi taqvim','Bir Haftalik',"Mintaqani o'zgartirish"
main_buttons=ReplyKeyboardMarkup([
    [btn_today,btn_week],[btn_region]
],resize_keyboard=True)
STATE_REGION=1
STATE_VAQT=2

user_region=dict()
def start(update,context):
    user=update.message.from_user
    user_region[user.id]=None
    butons=[
        [
            InlineKeyboardButton('Toshkent shaxri',callback_data='Toshkent'),
            InlineKeyboardButton('Namangan',callback_data='Namangan_vil')
        ],
        [
            InlineKeyboardButton('Andijon',callback_data='Andijon_vil'),
            InlineKeyboardButton("Farg'оna",callback_data="Farg'оna_vil")
        ],
        [
            InlineKeyboardButton('Jizzax',callback_data='Jizzax_vil'),
            InlineKeyboardButton("Buxoro",callback_data="Buxoro_vil")
        ],
        [
            InlineKeyboardButton('Surxondaryo',callback_data='Surxondaryo_vil'),
            InlineKeyboardButton("Navoiy",callback_data="Navoiy_vil")
        ],
        [
            InlineKeyboardButton('Samarqand',callback_data='Samarqand_vil'),
            InlineKeyboardButton("Qoraqalpog'iston",callback_data='Qora_qal')
        ],
        [
            InlineKeyboardButton('Qashqadaryo',callback_data='Qashqadaryo_vil'),
            InlineKeyboardButton("Toshkent viloyati",callback_data='Toshkent_vil')
        ],
        [
            InlineKeyboardButton('Xorazm',callback_data='Xorazm_vil'),
            InlineKeyboardButton("Sirdaryo",callback_data='Sirdaryo_vil')
        ]
    ]
    update.message.reply_html("Assalomu Aleykum <b>{}!</b>\n\n<b> 🇺🇿 Iltimos mintaqani tanlang</b>".
    format(user.first_name),reply_markup=InlineKeyboardMarkup(butons))
    return STATE_REGION

def inline_callback(update,context):
    nam_tuman=t.tuman.namangan_tumanlar
    far_tuman=t.tuman.fargona_tumanlar
    andijon_tuman=t.tuman.andijon_tumanlar
    tosh_vil_tuman=t.tuman.toshkent_vil_tumanlari
    jizzah_tuman=t.tuman.jizzah_tumanlar
    sirdaryo_tuman=t.tuman.sirdaryo_tumanlar
    surxondaryo_tuman=t.tuman.surxondaryo_tumanlar
    qashqadaryo_tuman=t.tuman.qashqadaryo_tumanlar
    samarqand_tuman=t.tuman.samarqand_tumanlar
    buxoro_tuman=t.tuman.buxoro_tumanlar
    navoiy_tuman=t.tuman.navoiy_tumanlar
    xorazm_tuman=t.tuman.xorazm_tumanlar
    qoraqalpoq=t.tuman.qoraqalpoq_tumanlar
    try:
        query=update.callback_query
        if (query.data!="Namangan_vil" and query.data!="Farg'оna_vil" and 
            query.data!='Andijon_vil' and query.data!="Toshkent_vil"  and 
            query.data!='Jizzax_vil' and query.data!='Sirdaryo_vil'and 
            query.data!='Surxondaryo_vil' and query.data!="Qashqadaryo_vil" and 
            query.data!="Samarqand_vil" and query.data!="Buxoro_vil" and
            query.data!="Navoiy_vil" and query.data!="Xorazm_vil" and query.data!="Qora_qal"):
            query.message.delete()
            user_id=query.from_user.id
            user_region[user_id]=query.data
            query.message.reply_html(text='<b>Kerakli buyruqni tanlang</b>',
                                reply_markup=main_buttons)
            return STATE_VAQT
    except:
        pass
    try:    
        if query.data=="Namangan_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(nam_tuman))
            
            
        if query.data=="Farg'оna_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(far_tuman))
            
        
        if query.data=="Andijon_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(andijon_tuman))
        
        if query.data=='Toshkent_vil':
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(tosh_vil_tuman))
        
        if query.data=="Jizzax_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(jizzah_tuman))
            
        if query.data=="Sirdaryo_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(sirdaryo_tuman))
            
        if query.data=='Surxondaryo_vil':
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(surxondaryo_tuman))
        
        if query.data=='Qashqadaryo_vil':
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(qashqadaryo_tuman))
        
        if query.data=='Samarqand_vil':
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(samarqand_tuman))
        
        if query.data=="Buxoro_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(buxoro_tuman))

        if query.data=="Navoiy_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(navoiy_tuman))
        if query.data=="Xorazm_vil":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(xorazm_tuman))
        if query.data=="Qora_qal":
            query.message.delete()
            query.message.reply_html(text='<b> Tumaniningizni tanlang</b>',
                                reply_markup=InlineKeyboardMarkup(qoraqalpoq))
    except:
        pass

def today(update,context):
    try:    
        user=update.message.from_user
        city=user_region[user.id]
        if not user_region[user.id]:
            return STATE_REGION
        javob=pray.praytime.timepray(city)
        update.message.reply_html(text=f"<b>{javob}</b>")
    except:
        pass

def week(update,context): 
    update.message.reply_html(text=f"Noqulaylik uchun uzur botning bu funksiyasi hali ishga tushirilmagan")
#    url=f"https://islomapi.uz/api/present/week?region={city}"
#    r=requests.get(url)
#
#    res=r.json()
#    return res
def select_region(update,context):
    butons=[
        [
            InlineKeyboardButton('Toshkent shaxri',callback_data='Toshkent'),
            InlineKeyboardButton('Namangan',callback_data='Namangan_vil')
        ],
        [
            InlineKeyboardButton('Andijon',callback_data='Andijon_vil'),
            InlineKeyboardButton("Farg'оna",callback_data="Farg'оna_vil")
        ],
        [
            InlineKeyboardButton('Jizzax',callback_data='Jizzax_vil'),
            InlineKeyboardButton("Buxoro",callback_data="Buxoro_vil")
        ],
        [
            InlineKeyboardButton('Surxondaryo',callback_data='Surxondaryo_vil'),
            InlineKeyboardButton("Navoiy",callback_data="Navoiy_vil")
        ],
        [
            InlineKeyboardButton('Samarqand',callback_data='Samarqand_vil'),
            InlineKeyboardButton("Qoraqalpog'iston",callback_data='Qora_qal')
        ],
        [
            InlineKeyboardButton('Qashqadaryo',callback_data='Qashqadaryo_vil'),
            InlineKeyboardButton("Toshkent viloyati",callback_data='Toshkent_vil')
        ],
        [
            InlineKeyboardButton('Xorazm',callback_data='Xorazm_vil'),
            InlineKeyboardButton("Sirdaryo",callback_data='Sirdaryo_vil')
        ]
    ]
    update.message.reply_text(' 🇺🇿 Yangi mintaqani tanlang 👇',reply_markup=InlineKeyboardMarkup(butons))
    return STATE_REGION

def main():
    updater=Updater('5480247472:AAHZQHqtQtgxHeAC8KCnLbEdP6kgaBaWRLY',use_context=True)
    
    dispatcher=updater.dispatcher
    
    #dispatcher.add_handler(CommandHandler('Start',start))
    
    #dispatcher.add_handler(CallbackQueryHandler(inline_callback))
    
    conv_handlar=ConversationHandler(
        entry_points=[CommandHandler('Start',start)],
        states={
            STATE_REGION:
                [
                CallbackQueryHandler(inline_callback),
                MessageHandler(Filters.regex('^('+btn_today+')$'),today),
                MessageHandler(Filters.regex('^('+btn_week+')$'),week),
                MessageHandler(Filters.regex('^('+btn_region+')$'),select_region)
                
                ],
            STATE_VAQT:
            [
                MessageHandler(Filters.regex('^('+btn_today+')$'),today),
                MessageHandler(Filters.regex('^('+btn_week+')$'),week),
                MessageHandler(Filters.regex('^('+btn_region+')$'),select_region)

            ],
            
        },
        fallbacks=[CommandHandler('Start',start)]
    )
    dispatcher.add_handler(conv_handlar)
    updater.start_polling()
    updater.idle()
main()