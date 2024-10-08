from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# استخدام الـ API الخاص بك
TOKEN = '7662044209:AAGkhGIVOPEBy4foGXdC2CoyNffxR77hqBM'

# استخدام الـ ID الخاص بالقناة
CHANNEL_ID = '-1002300230236'
# قم بوضع ID القناة هنا

# دالة توليد الكوبون الثابت
def generate_coupon():
    return "GGcash_joined"  # الكوبون الثابت

# دالة البداية التي تعرض زرين: زر الانضمام وزر التحقق
def start(update, context):
    user_id = update.message.chat_id
    # إنشاء زرين: زر للانضمام إلى القناة وزر للتحقق من العضوية
    keyboard = [
        [InlineKeyboardButton("Join Channel", url="https://t.me/anabaa2323")],
        [InlineKeyboardButton("تحقق من العضوية", callback_data="check_membership")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # نص الرسالة المعدل
    context.bot.send_message(chat_id=user_id, text='اضغط على الزر أدناه للانضمام إلى القناة، ثم تحقق من عضويتك للحصول على رمز الكوبون "GGcash*****".\nيمكنك استخدامه في تطبيق GGcash Rewards.', reply_markup=reply_markup)

# دالة التحقق مما إذا كان المستخدم عضوًا في القناة
def check_membership(update, context):
    query = update.callback_query
    user_id = query.message.chat_id

    try:
        # التحقق مما إذا كان المستخدم عضوًا في القناة
        chat_member = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        
        if chat_member.status in ['member', 'administrator', 'creator']:
            # إذا كان المستخدم عضوًا في القناة
            coupon_code = generate_coupon()

            # إنشاء أزرار لنسخ الكوبون والانتقال لتطبيق GGcash
            keyboard = [
                [InlineKeyboardButton("📋 نسخ الكوبون", callback_data="copy_coupon")],
                [InlineKeyboardButton("افتح GGcash Rewards", url="https://play.google.com/store/apps/details?id=com.ggcash.rewards.live")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # رسالة عند إرسال الكوبون
            context.bot.send_message(chat_id=user_id, text=f"شكراً على الاشتراك! ها هو الكوبون الخاص بك: {coupon_code}\nيمكنك استخدامه في تطبيق GGcash Rewards عبر الرابط التالي:", reply_markup=reply_markup)
        
        else:
            context.bot.send_message(chat_id=user_id, text="يبدو أنك لم تنضم إلى القناة بعد. يرجى الانضمام للحصول على الكوبون.")
    
    except Exception as e:
        context.bot.send_message(chat_id=user_id, text=f"حدث خطأ أثناء التحقق من العضوية: {str(e)}")

# دالة للتعامل مع نسخ الكوبون
def handle_copy_coupon(update, context):
    query = update.callback_query
    user_id = query.message.chat_id

    # استجابة عند الضغط على زر "نسخ الكوبون"
    context.bot.send_message(chat_id=user_id, text="تم نسخ الكوبون: GGcash_joined\nيمكنك لصقه في التطبيق.")

# الوظيفة الرئيسية لتشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # ربط وظيفة start بالأمر /start
    dp.add_handler(CommandHandler('start', start))

    # ربط وظيفة check_membership عندما يتم الضغط على زر "تحقق من العضوية"
    dp.add_handler(CallbackQueryHandler(check_membership, pattern="check_membership"))

    # ربط وظيفة نسخ الكوبون عندما يتم الضغط على زر "نسخ الكوبون"
    dp.add_handler(CallbackQueryHandler(handle_copy_coupon, pattern="copy_coupon"))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



