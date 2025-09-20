import re
import base64
import requests
import json
import os

B2  = os.getenv("B2")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

try:
    response = requests.get(B2, headers=headers)
    response.raise_for_status()
    response_text = response.text

    print("Response text:", response_text)
    
    match = re.search(r'[A-Za-z0-9]{8}\*\*(.*)', response_text)
    
    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        result = match.group(1)
        print("正则匹配到的内容:", content)

    data = json.loads(response_text)

    for site in data.get("sites", []):
        if site.get("key") == "push_agent":
            site["name"] = "请勿相信视频中广告"

    data["wallpaper"] = "http://王二小放牛娃牛逼.999888987.xyz"
    data["logo"] = "./jar/logo.gif"
    data["warningText"] ="否极泰来,好运连连。"
    data["lives"] = [
        {
            "name": "LIVE",
            "ua": "okhttp/3.15",
            "type": 0,
            "playerType": 1,
            "epg": "http://epg.cdn.loc.cc/epg/?ch={name}&date={date}",
            "logo": "https://epg.iill.top/logo/{name}.png",
            "url": "./zo.txt"
        },
        {
            "name": "TV",
            "ua": "okhttp/3.15",
            "type": 0,
            "playerType": 1,
            "url": "https://gh.catmak.name/https://raw.githubusercontent.com/Supprise0901/TVBox_live/refs/heads/main/live.txt"
        },
        {
            "name": "TVB",
            "type": 0,
            "url": "https://epg.pw/test_channels.m3u",
            "playerType": 1
        },
        {
            "name": "NOW",
            "type": 0,
            "url": "https://gh.catmak.name/https://raw.githubusercontent.com/JohnnyW820/IPTV/refs/heads/main/my-iptv.txt",
            "playerType": 1
        },
        {
      "name": "BTV",
      "type": 0,
      "url": "http://rihou.cc:555/gggg.nzk",
      "playerType": 1
        }
    ]

    for site in data.get("sites", []):
        if site.get("key") == "csp_nongmin":
            site["name"] = "📺看电视吧"
            data["sites"].insert(0, data["sites"].pop(data["sites"].index(site)))
            break 
        
    if "sites" in data:
        if isinstance(data["sites"], list) and isinstance(data["sites"][0], list):
            data["sites"] = [item for sublist in data["sites"] for item in sublist]

        new_site = {
            "key": "shan",
            "name": "🍊闪电┃影视",
            "type": 1,
            "api": "http://sdzyapi.com/api.php/provide/vod/",
            "ext":{"danmu":true},
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 1,
            "categories": [
            "国产剧",
            "大陆综艺",
            "海外剧",
            "港剧",
            "有声动漫",
            "写真热舞",
            "国产动漫",
            "动画片"
      ]
        }
        new_site1 = {
            "key": "ikun",
            "name": "🦢爱坤┃影视",
            "type": 1,
            "api": "https://ikzy7.com/api.php/provide/vod?",
            "ext":{"danmu":true},
            "searchable": 1,
            "changeable": 1,
            "categories": [
        "大陆综艺",
        "国产剧",
        "香港剧",
        "爽文短剧",
        "喜剧片",
        "国产动漫"
      ]
        }
        new_site2 = {
            "key": "Wexwwe",
            "name": "🏝WWE┃娱乐",
            "type": 3,
            "api": "csp_WexwweGuard",
            "searchable": 0,
            "changeable": 0,
            "jar": "./jar/wex.png;md5;4b1f5223aa26cc9489d0b481d708d278"
        }
        
        data["sites"].insert(1, new_site)
        data["sites"].insert(2, new_site1)
        data["sites"].insert(3, new_site2)

    else:
        print('"sites" 键不在数据中')

    keys_to_remove = ["豆豆","警示","config","csp_Netfixtv","csp_Netfixtv2","csp_Wogg","csp_Duopan","csp_UC","csp_XiaoYi","csp_MiSou","荐片"]
    data["sites"] = [site for site in data["sites"] if site.get("key") not in keys_to_remove]
    
    modified_content = json.dumps(data, indent=2, ensure_ascii=False)

    with open('b2.txt', 'w', newline='', encoding='utf-8') as f:
        f.write(modified_content)

    print("已写入。")

except requests.RequestException as e:
    print(f"请求失败: {e}")

except json.JSONDecodeError as e:
    print(f"JSON 解析失败: {e}")

except Exception as e:
    print(f"发生错误: {e}")
