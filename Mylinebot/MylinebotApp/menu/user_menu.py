import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

headers = {"Authorization":"Bearer 'token'","Content-Type":"application/json"}
line_bot_api = LineBotApi('token')

# #新增LIFF頁面到LINEBOT中
# liff_id = liff_api.add(view_type="tall",view_url="https://www.youtube.com/")

body = {
    "size": {"width": 1200, "height": 810},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 600, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "user_menu",
                      "data": "richmenu=user_menu"
                    }
        },
        {
          "bounds": {"x": 600, "y": 0, "width": 600, "height": 93},
          "action": {
                      "type": "richmenuswitch",
                      "richMenuAliasId": "user_donate",
                      "data": "richmenu=user_donate"
                    }
        },
        {
          "bounds": {"x": 0, "y": 93, "width": 800, "height": 335},
          "action": {"type": "message", "text": "查詢即期品"}
        },
        {
          "bounds": {"x": 800, "y": 93, "width": 400, "height": 335},
          "action": {"type": "uri",
                      "label": "line spot",
                      "uri": 'https://liff.line.me/1657635549-y0KwqmZb'} #優惠地圖
        },
        {
          "bounds": {"x": 0, "y": 428, "width": 400, "height": 335},
          "action": {"type": "uri",
                      "label": "share to friend",
                      "uri": 'https://liff.line.me/1657635549-35pzekgQ'} #推薦給好友
        },
        {
          "bounds": {"x": 400, "y": 428, "width": 400, "height": 335},
          "action": {"type": "uri",
                      "label": "user data update",
                      "uri": 'https://liff.line.me/1657635549-yM4MZE73'} #資料修改
        },
        {
          "bounds": {"x": 800, "y": 428, "width": 400, "height": 335},
          "action": {"type": "message", "text": "聯絡我們"}
        }
        
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text) # richmenu-ba6c5bc5928ea7bd5f7d2223576b1b1f

x = req.text.split("\"")


with open("image/user_menu.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(x[3], "image/png", f)

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+x[3], 
                       headers=headers)


