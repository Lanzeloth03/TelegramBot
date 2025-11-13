import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ------------ RESPUESTAS HUMANIZADAS ----------------

def respuesta_humana(texto):
    respuestas = [
        "Entiendo lo que dices, déjame pensarlo un segundo… 🤔",
        "Buen punto, mira esto 👉",
        "Interesante lo que comentas. Te explico:",
        "Ya, ya, te sigo. Mira:",
        "Déjame ayudarte con eso 😊",
        "Perfecto, aquí va la info que necesitas:",
    ]
    base = random.choice(respuestas)
    return f"{base}\n\n{texto}"

# ------------ COMANDO /start ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📚 Preguntas", "🖼 Enviar Imagen"],
        ["🤖 IA simple", "ℹ️ Info del bot"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "¡Hola! Soy *Lanz22_bot*, tu asistente 🤝\n¿En qué te ayudo hoy?",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# ------------ MANEJADOR DE MENÚ ----------------

async def manejar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if "preguntas" in texto:
        await update.message.reply_text(
            respuesta_humana("Puedes preguntarme lo que quieras 👌"))
    
    elif "info del bot" in texto:
        await update.message.reply_text(
            respuesta_humana("Fui creado para ayudarte, conversar y automatizar tareas ✨"))
    
    elif "ia simple" in texto:
        await update.message.reply_text(
            respuesta_humana("Dime algo y te doy una respuesta inteligente y natural 😄"))
    
    elif "imagen" in texto:
        await update.message.reply_text(
            respuesta_humana("Claro, envíame una imagen y la analizaré 🖼"))
    
    else:
        await update.message.reply_text(
            respuesta_humana("Te escucho 👂 ¿Qué deseas hacer?"))

# ------------ RECIBIR IMÁGENES ----------------

async def recibir_imagen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        respuesta_humana("Recibí tu imagen 🤳. Analizaré lo que pueda reconocer."))

# ------------ MENSAJES DE TEXTO (IA SIMPLE) ----------------

async def responder_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    # Simulación “IA”: respuestas adaptadas al tono humano
    if "hola" in user_msg.lower():
        reply = "¡Hola! Qué bueno verte por aquí 😄"
    elif "como estas" in user_msg.lower():
        reply = "Estoy bastante bien, gracias por preguntar 😌 ¿Y tú qué tal?"
    elif "ayuda" in user_msg.lower():
        reply = "Claro, dime qué necesitas y lo vemos juntos 👍"
    else:
        reply = f"Mmm… interesante lo que dices. Mira, pienso que:\n\n➤ {user_msg}"

    await update.message.reply_text(respuesta_humana(reply))

# ------------ MAIN ----------------

def main():
    app = Application.builder().token("TU_TOKEN_AQUI").build()

    # Comandos
    app.add_handler(CommandHandler("start", start))

    # Menú
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_menu))

    # Imagenes
    app.add_handler(MessageHandler(filters.PHOTO, recibir_imagen))

    # IA simple
    app.add_handler(MessageHandler(filters.TEXT, responder_texto))

    print("Bot ejecutándose...")
    app.run_polling()

if __name__ == "__main__":
    main()
