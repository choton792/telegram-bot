from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8741364456:AAGwkmytOY6evjSjMykH9ovNXG11qiMMgkM"

CHANNELS = ["@Choton_111", "@Onlinee_Income_Official"]

async def check_join(context, user_id):
    for channel in CHANNELS:
        try:
            member = await context.bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    joined = await check_join(context, user_id)

    if not joined:
        buttons = [
            
            [InlineKeyboardButton("📢 Join Channel 2", url="https://t.me/Onlinee_Income_Official")],
            [InlineKeyboardButton("✅ I Joined", callback_data="check")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.reply_text(
            "❌ আগে দুইটা channel join করো তারপর access পাবে",
            reply_markup=reply_markup
        )
        return

    await update.message.reply_text("✅ Welcome! এখন তুমি bot use করতে পারো 🎉")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    joined = await check_join(context, user_id)

    if joined:
        await query.message.reply_text("✅ Access Granted! Welcome 😎")
    else:
        await query.message.reply_text("❌ এখনো সব channel join করো নাই!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
