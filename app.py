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
line_bot_api = LineBotApi('oeV7aX9aZ0IpUw5q4xJnhgL+SRu/uvPIEg4fsaapkP3AYY3Ox+bCaCtVPUvwJQKmhfyIY8BoZJj2KY+M8c1ElncSTTbZyjdhAuKncpXCggC7JcoNkjonzucEBe8YN435l6Lh01K1PG6Ham7XDLn4DAdB04t89/1O/***********')
# 必須放上自己的Channel Secret
handler = WebhookHandler('20370e7061e924b99b0ebd807*******')

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
        elif event.message.text == '最近有什麼事嗎':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            message1 = TextSendMessage('里民旅遊、政見宣導都將在此一點就能看，小到打疫苗、大到所有重大事情宣導我都會以圖片形式讓大家清楚明瞭') 
            line_bot_api.reply_message(event.reply_token,message1)
        elif event.message.text == '政見是什麼!!':
            # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
            message1 = TextSendMessage('  1. 建立里民意見有效、即時溝通的管道#組建里民line社團群組，讓里民可以即時反應鄰里問題、討論鄰里重要事務。\n'+
                                       '  2. 設置事務處理、意見反饋平台 (每篇公告下方將附上google 表單)。\n'+
                                       '  3. 消弭資訊不對稱，落實鄰里重要資訊公告\n'+
                                       '  4. 爭取南湖國小前（小石鍋到7-11前方）增設人行道維護學生上學安全\n'+
                                       '  5. 爭取增設機車停車位\n'+
                                       '  6. 邀請里民運動，增加凝聚力\n'+
                                       '  7. 協助五分里最熱心的里民朋友組織各種志工活動，讓五分里更舒適\n'+
                                       '  8. 配合上層機關市政推動，保障里民應有權利，並積極爭取相關福利\n') 
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
            message1 = TextSendMessage('lineid是:greattoseeyou000，直接複製貼上就行了喔，歡迎你加入喔') 
            line_bot_api.reply_message(event.reply_token,message1)
        elif event.message.text == '月琴阿姨加油':
            buttons_template_message = TemplateSendMessage(
            alt_text='月琴阿姨會加油',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img.onl/eszFk0',
                title='月琴阿姨會加油',
                text='選單功能－祝大家平安喜樂',
                actions=[
                    
                    MessageAction(
                        label='競選總部',
                        text='我想來泡茶吃點心找阿姨聊天'
                    ),
                    URIAction(
                        label='月琴阿姨的LINE',
                        uri='https://line.me/ti/p/uNZuJUcrMo'
                 )
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
