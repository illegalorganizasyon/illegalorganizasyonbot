import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


welcome_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("💊 Drugs", callback_data="drugs")],
    [InlineKeyboardButton("🔫 Silahlar", callback_data="guns")],
    [InlineKeyboardButton("💊 Reçeteli İlaçlar", callback_data="drugs2")],
    [InlineKeyboardButton("📄 Sahte Belgeler", callback_data="documents")],
    [InlineKeyboardButton("💸 Sahte Para", callback_data="money")],
    [InlineKeyboardButton("📃 Fatura Hizmeti", callback_data="invoice")],
    [InlineKeyboardButton("🏧 POS Hizmeti", callback_data="pos")],
    [InlineKeyboardButton("🌐 İllegal Script", callback_data="illegalscript")],
    [InlineKeyboardButton("₿ Ödeme", callback_data="payment")]
])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text='İllegal Market', reply_markup=welcome_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    back_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("◀️ Geri", callback_data="back")]
    ])

    query = update.callback_query

    await query.answer()

    if query.data == 'drugs':
        text = '''Marihuana - 300 TL
Meth - 300 TL
Xtc - 120 TL
LSD - 450 TL
Kokain - 2000 TL'''
        await query.edit_message_text(text=text)
        await query.edit_message_reply_markup(reply_markup=back_markup)
    elif query.data == 'guns':
	text = '''CNC Yapım 7.65mm Tabanca 4500 TL
7.65 Mermi MKE Kutu 650 TL'''
	
	await query.edit_message_text(text=text)
        await query.edit_message_reply_markup(reply_markup=back_markup)
    elif query.data == 'drugs2':
        pass
    elif query.data == 'documents':
        pass
    elif query.data == 'money':
        pass
    elif query.data == 'invoice':
        pass
    elif query.data == 'pos':
        pass
    elif query.data == 'illegalscript':
        pass
    elif query.data == 'payment':
        pass
    elif query.data == 'back':
        await query.edit_message_text(text='İllegal Market')
        await query.edit_message_reply_markup(reply_markup=welcome_markup)

    await query.answer()


def main() -> None:
    application = Application.builder().token("5649456887:AAFmc6DMtiEkyl3Oe91NJ0o_CA0px7X0faM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()


if __name__ == "__main__":
    main()
