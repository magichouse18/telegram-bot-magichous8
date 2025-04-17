from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"

MENU, SHOP, WEED = range(3)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data="pagamenti")],
        [InlineKeyboardButton("🧍 Contattami 🧍", callback_data="contattami")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale.\n"
        "Il Bot viene costantemente aggiornato con i prodotti disponibili.\n\n"
        "Per qualsiasi informazione o ordini contattare:\n"
        "@magichous8",
        reply_markup=reply_markup
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data

    if data == str(SHOP):
        keyboard = [
            [InlineKeyboardButton("🍁 WEED 🍁", callback_data=str(WEED)),
             InlineKeyboardButton("🍫 HASH 🍫", callback_data="hash")],
            [InlineKeyboardButton("🍬 EDIBILI", callback_data="edibili"),
             InlineKeyboardButton("📖 REGOLAMENTO 📖", callback_data="regolamento")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]
        ]
        query.edit_message_text("Seleziona il servizio per ricevere maggiori informazioni:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(WEED):
        keyboard = [
            [InlineKeyboardButton("🇪🇸 SPAGNOLE 🇪🇸", callback_data="spagnole")],
            [InlineKeyboardButton("🇪🇸 CALI SPAIN 🇺🇸", callback_data="cali_spain")],
            [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data="cali_usa")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione delle migliori erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "pagamenti":
        query.edit_message_text("Accettiamo pagamenti in BTC, Postepay, PayPal e altri metodi su richiesta.")

    elif data == "contattami":
        query.edit_message_text("Per info o ordini: @magichous8")

    elif data == "spagnole":
        query.edit_message_text(
            "LEMON HAZE 🍋\n"
            "50g - 280€\n100g - 550€\n200g - 1000€\n"
            "500g - 2300€\n1kg - 3900€\n5kg - 17500€\n\n"
            "Pacchi super puliti.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]])
        )

    elif data == "cali_spain":
        query.edit_message_text("Prodotti Cali Spain disponibili. Contattaci per info!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]))

    elif data == "cali_usa":
        query.edit_message_text("Prodotti Cali USA originali. Contattaci per disponibilità.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]))

    elif data == "hash":
        query.edit_message_text("HASH disponibili: Afghan, Marocchino, Nepalese... Scrivici per i dettagli.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]))

    elif data == "edibili":
        query.edit_message_text("EDIBILI: Caramelle, Cioccolatini, Olio CBD, Gomme da masticare... Scrivici!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]))

    elif data == "regolamento":
        query.edit_message_text("REGOLAMENTO:\n- Rispetta la privacy\n- Ordini solo maggiorenni\n- Contatti solo se realmente interessati", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]))

    elif data == str(MENU):
        start(query, context)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
