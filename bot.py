import telebot

id_admin = ""
token_bot = ""
files_src = ""
photos_src = ""
sec_admin = ""
with open('config.txt') as f:
    for i in f:
        if i[0] == "#":
            break
        elif i[0] == "i":
            id_admin = i[9:].rstrip()
        elif i[0] == "s":
            id_admin = i[9:].rstrip()
        elif i[0] == "t":
            token_bot = i[10:].rstrip()
        elif i[0] == "f":
            files_src = i[10:].rstrip()
        elif i[0] == "p":
            photos_src = i[11:].rstrip()
bot = telebot.TeleBot(token_bot)


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    if str(user_id) == id_admin:
        bot.send_message(message.chat.id, 'Привет')

        @bot.message_handler(content_types=['document'])
        def handle_docs_photo(message):
            try:

                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = files_src + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "Пожалуй, я сохраню это")
            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(content_types=['photo'])
        def handle_docs_photo(message):
            try:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = photos_src + file_info.file_path
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "Пожалуй, я сохраню это")

            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(content_types=['audio'])
        def handle_docs_photo(message):
            try:
                file_info = bot.get_file(message.audio[len(message.audio) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = photos_src + file_info.file_path
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "Пожалуй, я сохраню это")

            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(content_types=['video'])
        def handle_docs_photo(message):
            try:
                file_name = message.json['video']['file_name']
                file_info = bot.get_file(message.video.file_id)
                with open(file_name, "wb") as f:
                    file_content = bot.download_file(file_info.file_path)
                    f.write(file_content)
                bot.reply_to(message, f"OK. Сохранил {file_name}")

            except Exception as e:
                bot.reply_to(message, e)

        @bot.message_handler(content_types=['voice'])
        def handle_docs_photo(message):
            try:
                file_info = bot.get_file(message.voice[len(message.voice) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                src = photos_src + file_info.file_path
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.reply_to(message, "Пожалуй, я сохраню это")

            except Exception as e:
                bot.reply_to(message, e)
    else:
        bot.send_message(message.chat.id, 'Уходи незнакомец ' + str(user_id))


bot.infinity_polling()
