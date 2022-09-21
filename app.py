from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from flask_ngrok import run_with_ngrok
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('oeV7aX9aZ0IpUw5q4xJnhgL+SRu/uvPIEg4fsaapkP3AYY3Ox+bCaCtVPUvwJQKmhfyIY8BoZJj2KY+M8c1ElncSTTbZyjdhAuKncpXCggC7JcoNkjonzucEBe8YN435l6Lh01K1PG6Ham7XDLn4DAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('20370e7061e924b99b0ebd8078f89251')

line_bot_api.push_message('Ua3077104df675bcad56981c346693b69', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    message1 = TextSendMessage('hi')
    
    line_bot_api.reply_message(event.reply_token,message1)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
