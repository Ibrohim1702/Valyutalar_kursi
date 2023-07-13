from telegram import ReplyKeyboardMarkup, KeyboardButton
import requests


def valyuta(get):
    log['state'] = 3
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    for i in response.json():
        if i['CcyNm_UZ'] == get:
            st = f"Nomi: {i['CcyNm_UZ']}\nQiymati: {i['Rate']}\nDifferansiyalligi: {i['Diff']}"
            return st


log = {'state': 0, 'dona': 1}


def button(step=None):
    btn = []
    if step == "button":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("Next ⏭")])

    elif step == "Next ⏭":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("🔙 Back"), KeyboardButton("Next ⏭")])

    elif step == "🔙 Back":
        url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
        response = requests.get(url).json()
        for i in range((log['dona'] - 1) * 9, log['dona'] * 9, 3):
            btn.append([
                KeyboardButton(response[i]['CcyNm_UZ']), KeyboardButton(response[i - 2]['CcyNm_UZ']),
                KeyboardButton(response[i - 1]['CcyNm_UZ'])
            ])
        btn.append([KeyboardButton("🔙 Back"), KeyboardButton("Next ⏭")])

    elif step == "lang":
        btn = [
            [KeyboardButton("🇺🇿UZ"), KeyboardButton("🇷🇺RU")]
        ]
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def start(update, context):
    log['state'] = 1
    update.message.reply_text("Assalomu aleykum", reply_markup=button("button"))


def message_handler(update, context):
    msg = update.message.text
    if msg == "Next ⏭":
        log['dona'] = 2
        log['dona'] = log.get("dona", 1) + 1
        update.message.reply_text(f"Valyutalardan birini tanlang", reply_markup=button("Next ⏭"))
    elif msg == "🔙 Back":
        log["dona"] = log.get("dona", 1) - 1
        update.message.reply_text(f"Valyutalardan birini tanlang", reply_markup=button("🔙 Back"))
    else:
        update.message.reply_text(f"Markaziy bankning bugungi valyuta kursi:\n{valyuta(msg)}")
