import re
import base64
import requests
import json
import os

headers = {'User-Agent': 'okhttp/3.15'}

B1  = os.getenv("B1")

if B1 is None:
    raise ValueError("未设置")
    
try:
    response = requests.get(B1, headers=headers)
    response.raise_for_status()

    match = re.search(r'[A-Za-z0]{8}\*\*(.*)', response.text)

    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        result = match.group(1)
        content = base64.b64decode(result).decode('utf-8')

        print("解析后的内容：")
        print(content)

        content_lines = content.split('\n')
        cleaned_content = [line for line in content_lines if not line.strip().startswith("//")]

        cleaned_content_text = '\n'.join(cleaned_content)

        data = json.loads(cleaned_content_text)

        for site in data.get("sites", []):
            if site.get("key") == "豆豆":
                site["name"] = "📺电视吧"
            if site.get("key") == "豆":
                site["name"] = "📺电视吧"

        data["wallpaper"] ="https://yydsys.top/bg.php"
        data["warningText"] ="烟笼寒水月笼沙，夜泊秦淮近酒家。"
        data["logo"] = "./jar/logo.gif"
        data["lives"] = [
            {
                "name": "LIVE",
                "type": 0,
                "url": "./z1.txt",
                "playerType": 1,
                "epg": "http://epg.51zmt.top:8000/api/diyp/?ch={name}&date={date}",
                "logo": "https://www.xn--rgv465a.top/tvlogo/{name}.png"
            },
            {
                "name": "TV",
                "ua": "okhttp/3.15",
                "type": 0,
                "playerType": 1,
                "epg": "http://epg.51zmt.top:8000/api/diyp/?ch={name}&date={date}",
                "logo": "https://www.xn--rgv465a.top/tvlogo/{name}.png",
                "url": "https://gh.catmak.name/https://raw.githubusercontent.com/Supprise0901/TVBox_live/refs/heads/main/live.txt"
            },
            {
                "name": "TVB",
                "type": 0,
                "url": "https://epg.pw/test_channels.m3u",
                "playerType": 1
            },
            {
                "name": "虎牙一起看",
                "type": 0,
                "url": "https://sub.ottiptv.cc/huyayqk.m3u",
                "playerType": 2,
                "timeout":10,
                "ua":"okHttp/Mod-1.4.0.0"
            },
            {
                "name": "斗鱼一起看",
                "type": 0,
                "url": "https://sub.ottiptv.cc/douyuyqk.m3u",
                "playerType": 2,
                "timeout":10,
                "ua":"okHttp/Mod-1.4.0.0"
            },
            {
                "name": "B站直播",
                "type": 0,
                "url": "https://sub.ottiptv.cc/bililive.m3u",
                "playerType": 2,
                "timeout":10,
                "ua":"okHttp/Mod-1.4.0.0"
            },
            {
                "name": "YY轮播",
                "type": 0,
                "url": "https://sub.ottiptv.cc/yylunbo.m3u",
                "playerType": 2,
                "timeout":10,
                "ua":"okHttp/Mod-1.4.0.0"
            },
            {
                "name": "BTV",
                "type": 0,
                "url": "http://rihou.cc:555/gggg.nzk",
                "playerType": 1
            }
        ]

        for site in data.get("sites", []):
           if site.get("key") == "糯米":
                site["name"] = "📺看电视吧"
                data["sites"].insert(0, data["sites"].pop(data["sites"].index(site)))
                break
            
        if "sites" in data:
            if isinstance(data["sites"], list) and isinstance(data["sites"][0], list):
                data["sites"] = [item for sublist in data["sites"] for item in sublist]
            

            new_site = {
      "key": "ikun",
      "name": "🦢爱坤┃1080P",
      "type": 1,
      "api": "https://ikzy7.com/api.php/provide/vod?",
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
            data["sites"].insert(2, new_site)
                        
        else:
            print('"sites" 键不在数据中')

        keys_to_remove = ["MDrive","玩偶","YGP","ZPan","抠搜","UC","贱贱","新6V","PanSso","YpanSo","xzso","米搜","夸搜","Aliso","YiSo","wx","fan","seed","荐片"]
        data["sites"] = [site for site in data["sites"] if site.get("key") not in keys_to_remove]
        
        modified_content = json.dumps(data, indent=2, ensure_ascii=False)

        with open('b1.txt', 'w', newline='', encoding='utf-8') as f:
            f.write(modified_content)

        print("已写入。")
except requests.RequestException as e:
    print("请求失败:", e)
except Exception as ex:
    print("发生错误:", ex)
