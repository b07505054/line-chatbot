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
        temp=random.randint(0, 9)
        message = TextSendMessage(text=event.message.text)   
        if (event.message.text == '嗨' ) and temp==0 :
            temp=1
            message1 = TextSendMessage('您好，祝您有個美好的一天喔') 
            line_bot_api.reply_message(event.reply_token,message1)
            
        elif (event.message.text == '嗨' ) and temp==1 :
            temp=0
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581296'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==2:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='789',
                sticker_id='10862'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==3:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581300'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==4:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581308'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==5 :
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581301'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==6:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581292'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==7:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='8525',
                sticker_id='16581311'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==8:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='6362',
                sticker_id='11087930'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
        elif (event.message.text == '嗨' ) and temp==9:
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            sticker_message = StickerSendMessage(
                package_id='6362',
                sticker_id='11087933'
            )
            line_bot_api.reply_message(event.reply_token, sticker_message)
#         elif event.message.text == '嗨，我想提出能進步的方式':
#             # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
#             sticker_message = StickerSendMessage(
#                 package_id='6362',
#                 sticker_id='11087933'
#             )
#             line_bot_api.reply_message(event.reply_token, sticker_message)
        elif event.message.text == '這裡有問題':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            message1 = TextSendMessage('等選上里長表單才能開放，將隨時提供問題回報') 
            line_bot_api.reply_message(event.reply_token,message1)
        elif event.message.text == '政見是什麼!!':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            message1 = TextSendMessage('五分里來蛻變，我將做到:\n'+
                                       '    1. 建立line群，讓大家可以即時反映遇到的各種問題，或許您的左鄰右舍也有遇到相同的問題或他能幫助到你呢?\n'+
                                       '    2. 承上，在line群中一起投票做下照顧到最多人的決定，任何重大決定(ex.拆陸橋於否)，我都將不會簡單寫下無意見，或獨裁決斷。\n'+
                                       '    3. 於南湖國小前的小石鍋到711前方爭取增設人行道維護學生上學安全。\n'+
                                       '    4. 組織活動，公園好空曠。假日下午或晚餐時間我們一起跳健身操一起順便撿垃圾，一起認識朋友一起聊天。\n'+
                                       '    5. 建立市場攤販與里民的聯繫管道，一起討論是否能有共善共榮的解方。( 若有必須會使用優良店家地圖，由居民自行選擇是否更傾向購買配合意願高的店家 )\n'+
                                       '    6. 協助五分里最熱心的里民組織各種志工活動，讓五分里更舒適。\n'+
                                       '    7. 配合市政府及各上層機關市政推動，積極爭取更多更多福利。\n') 
            line_bot_api.reply_message(event.reply_token,message1)
       
       
        elif event.message.text == '我想來泡茶吃點心找阿姨聊天':
            location_message = LocationSendMessage(
                title='競選總部',
                address='東湖路160巷10弄33號1樓',
                latitude=25.067462903395572, 
                longitude=121.61635255525054
            )
            line_bot_api.reply_message(event.reply_token, location_message)
        
        elif event.message.text == '我有事想跟阿姨說':
            message1 = TextSendMessage('lineid是:greattoseeyou000，歡迎你加入喔') 
            line_bot_api.reply_message(event.reply_token,message1)
        elif event.message.text == '月琴阿姨加油':
            buttons_template_message = TemplateSendMessage(
            alt_text='月琴阿姨會加油',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                title='月琴阿姨會加油',
                text='選單功能－祝大家平安喜樂',
                actions=[
                    
                    MessageAction(
                        label='競選總部',
                        text='我想來泡茶吃點心找阿姨聊天'
                    ),
                    MessageAction(
                        label='月琴阿姨的line',
                        text='我有事想跟阿姨說'
                    ),
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, buttons_template_message)
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
