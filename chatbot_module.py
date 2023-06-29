import random

# Daftar respons chatbot
responses = {
    'sapaan': ['Halo!', 'Hai!', 'Selamat datang!', 'Halo, ada yang bisa saya bantu?'],
    'perpisahan': ['Sampai jumpa!', 'Terima kasih telah menghubungi kami.', 'Selamat tinggal!'],
    'terima_kasih': ['Sama-sama!', 'Tidak masalah.', 'Senang bisa membantu!'],
    'default': ['Maaf, saya tidak mengerti. Bisa Anda jelaskan lebih lanjut?', 'Mohon maaf, bisa diulangi?']
}

# Fungsi untuk mendapatkan respons dari chatbot berdasarkan input pengguna
def get_bot_response(user_message):
    user_message = user_message.lower()
    
    if 'halo' in user_message or 'hai' in user_message:
        return random.choice(responses['sapaan'])
    elif 'sampai jumpa' in user_message or 'terima kasih' in user_message:
        return random.choice(responses['perpisahan'])
    elif 'terima kasih' in user_message:
        return random.choice(responses['terima_kasih'])
    else:
        return random.choice(responses['default'])
