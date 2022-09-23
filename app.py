from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import random
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
#     if event.message.type == 'message':
        temp=random.randint(0, 1)
        message = TextSendMessage(text=event.message.text)   
        if (event.message.text == '你好' or event.message.text == '您好' ) and temp==0 :
            temp=1
            message1 = TextSendMessage('您好，祝您有個美好的一天喔') 
            line_bot_api.reply_message(event.reply_token,message1)
            
        elif (event.message.text == '你好' or event.message.text == '您好') and temp==1 :
            temp=0
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581296'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '晚安':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='789',
                sticker_id='10862'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '午安':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581300'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '早安':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581308'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '掰掰' or event.message.text == '拜拜' :
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581301'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '加油':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581292'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '生氣':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581311'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '難過':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='6362',
                sticker_id='11087930'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '好累':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='6362',
                sticker_id='11087933'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        
        else:
           
            line_bot_api.reply_message(event.reply_token,message)
#     else:
#         try:
#             stid=event.message.stickerId '
#             paid=events.message.packageId
#             sticker_message = StickerSendMessage(
#                 package_id=paid,
#                 sticker_id=stid
#             )
#             line_bot_api.reply_message(event.reply_token, sticker_message)
#         except:
            
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
