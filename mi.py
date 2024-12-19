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
    # 发送 GET 请求
    response = requests.get(B2, headers=headers)
    response.raise_for_status()
    response_text = response.text  # 获取文本内容

    print("Response text:", response_text)
    
    match = re.search(r'[A-Za-z0-9]{8}\*\*(.*)', response_text)
    
    if not match:
        print("在响应文本中未找到匹配项。")
    else:
        result = match.group(1)
        print("正则匹配到的内容:", content)

    data = json.loads(response_text)

    # 找到并替换特定字段值
    for site in data.get("sites", []):
        if site.get("key") == "push_agent":
            site["name"] = "请勿相信视频中广告"

    # 修改内容
    data["wallpaper"] = "http://www.kf666888.cn/api/tvbox/img"
    data["logo"] = "./jar/logo.gif"
    data["warningText"] ="否极泰来,好运连连。"
    data["lives"] = [
        {
            "name": "LIVE",
            "ua": "okhttp/3.15",
            "type": 0,
            "playerType": 1,
            "epg": "http://epg.51zmt.top:8000/api/diyp/?ch={name}&date={date}",
            "logo": "https://live.fanmingming.com/tv/{name}.png",
            "url": "./zo.txt"
        },
        {
            "name": "TV",
            "ua": "okhttp/3.15",
            "type": 0,
            "playerType": 1,
            "url": "./zb.txt"
        },
        {
            "name": "TVB",
            "type": 0,
            "url": "./zba.txt",
            "playerType": 1
        },
        {
            "name": "NOW",
            "type": 0,
            "url": "./zb3.txt",
            "playerType": 1
        },
        {
      "name": "BTV",
      "type": 0,
      "url": "http://rihou.cc:567/gggg.nzk",
      "playerType": 1
        }
    ]
    data["rules"] = [
        {
            "name": "暴风",
            "hosts": [
                "bfzy",
                "bfbfvip",
                "bfengbf"
            ],
            "regex": [
                "#EXTINF.*?\\s+.*?adjump.*?\\.ts"
            ]
        },
        {
            "name": "量子",
            "hosts": [
                "vip.lz",
                "hd.lz",
                ".cdnlz"
            ],
            "regex": [
                "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:7\\.166667,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:4\\.066667,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "17.19"
            ]
        },
        {
            "name": "非凡",
            "hosts": [
                "vip.ffzy",
                "hd.ffzy",
                "super.ffzy"
            ],
            "regex": [
                "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:6\\.400000,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:6\\.666667,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXTINF.*?\\s+.*?1171(057).*?\\.ts",
                "#EXTINF.*?\\s+.*?6d7b(077).*?\\.ts",
                "#EXTINF.*?\\s+.*?6718a(403).*?\\.ts",
                "17.99",
                "14.45"
            ]
        },
        {
            "name": "索尼",
            "hosts": [
                "suonizy"
            ],
            "regex": [
                "#EXT-X-DISCONTINUITY\\r*\\n*#EXTINF:1\\.000000,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXTINF.*?\\s+.*?p1ayer.*?\\.ts",
                "#EXTINF.*?\\s+.*?\\/video\\/original.*?\\.ts"
            ]
        },
        {
            "name": "快看",
            "hosts": [
                "kuaikan"
            ],
            "regex": [
                "#EXT-X-KEY:METHOD=NONE\\r*\\n*#EXTINF:5,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXT-X-KEY:METHOD=NONE\\r*\\n*#EXTINF:2\\.4,[\\s\\S]*?#EXT-X-DISCONTINUITY",
                "#EXT-X-KEY:METHOD=NONE\\r*\\n*#EXTINF:1\\.467,[\\s\\S]*?#EXT-X-DISCONTINUITY"
            ]
        },
        {
            "name": "一起看广告",
            "hosts": [
                "yqk88"
            ],
            "regex": [
                "18.4",
                "15.1666",
                "16.5333",
                "#EXT-X-DISCONTINUITY\\r*\\n*[\\s\\S]*?#EXT-X-CUE-IN"
            ]
        },
        {
            "name": "爱坤",
            "hosts": [
                "ik"
            ],
            "regex": [
                "#EXT-X-KEY:METHOD=NONE\\r*\\n*#EXTINF:[\\s\\S]*?#EXT-X-DISCONTINUITY"
            ]
        },
        {
            "name": "磁力广告",
            "hosts": [
                "magnet"
            ],
            "regex": [
                "更多",
                "请访问",
                "example",
                "社 區",
                "x u u",
                "直 播",
                "更 新",
                "社 区",
                "有趣",
                "有 趣",
                "英皇体育",
                "全中文AV在线",
                "新葡京",
                "娱乐城",
                "澳门皇冠赌场",
                "赞助播出",
                "哥哥快来",
                "美女荷官",
                "棋牌",
                "裸聊",
                "新片首发",
                "UUE29"
            ]
        },
        {
            "name": "火山嗅探",
            "hosts": [
                "huoshan.com"
            ],
            "regex": [
                "item_id="
            ]
        },
        {
            "name": "抖音嗅探",
            "hosts": [
                "douyin.com"
            ],
            "regex": [
                "is_play_url="
            ]
        },
        {
            "name": "农民嗅探",
            "hosts": [
                "toutiaovod.com"
            ],
            "regex": [
                "video/tos/cn"
            ]
        }
    ]

    data["ads"] = [
        "wan.51img1.com",
        "iqiyi.hbuioo.com",
        "vip.ffzyad.com",
        "https://lf1-cdn-tos.bytegoofy.com/obj/tos-cn-i-dy/455ccf9e8ae744378118e4bd289288dd"
    ]

    # 添加新数据到 "sites" 的第二段
    if "sites" in data:
        # 如果 "sites" 是一个包含列表的列表，则将其转换为单一的列表
        if isinstance(data["sites"], list) and isinstance(data["sites"][0], list):
            data["sites"] = [item for sublist in data["sites"] for item in sublist]

        new_site = {
            "key": "农民",
            "name": "📺看电视吧",
            "type": 3,
            "api": "csp_XYQHiker",
            "searchable": 1,
            "quickSearch": 1,
            "filterable": 1,
            "jar": "./jar/custom_spider.jar;md5;4557db37965e20fb46cb59c3f603383c",
            "ext":"./json/nm.json"
        }
        new_site1 = {
            "key": "人人影视",
            "name": "🧙人人┃1080P",
            "type": 3,
            "api": "csp_XBPQ",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 1,
            "jar": "./jar/yu.jar;md5;7e2f6ef2a5dce8b152dadefa6c7d4ba7",
            "ext": {
        "影片类型": "看电视吧",
        "简介": "请勿相信视频中广告。+<div class=\"stui-pannel_bd\"&&</div>",
        "分类url": "https://www.567dyy.com/list/{cateId}/area/{area}/by/{by}/class/{class}/page/{catePg}/year/{year}.html",
        "分类": "电影$1#电视剧$2#综艺$3#动漫$4#短剧$5"
      }
        }
        new_site2 = {
            "key": "qwqfun",
            "name": "👌QWQ┃1080P",
            "type": 1,
            "api": "https://www.qwqfun.one/api.php/tvbox",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 1,
            "ext": "qwqfun"
        }
        new_site3 = {
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
        new_site4 = {
            "key": "天天弹幕",
            "name": "👻天天┃1080P",
            "type": 3,
            "api": "csp_TianTian",
            "searchable": 1,
            "quickSearch": 1,
            "filterable": 1,
            "jar": "./jar/xs.txt;md5;62604d62b4f3bd41b195b5670bed80a9",
            "ext": {"danmu": True}
        }
        new_site5 = {
            "key": "Wexwwe",
            "name": "🏝WWE┃1080P",
            "type": 3,
            "api": "csp_Wexwwe",
            "searchable": 0,
            "changeable": 0,
            "jar": "./jar/wex.txt;md5;21a5ba32da12067f02d223bbe1b27651"
        }
        new_site6 = {
            "key": "七新影视",
            "name": "🐇七新┃1080P",
            "type": 3,
            "api": "csp_XYQHiker",
            "searchable": 1,
            "quickSearch": 1,
            "filterable": 1,
            "jar": "./jar/custom_spider.jar;md5;705ba6e23c4384c37a11dd904727520b",
            "ext":"./json/qx.json"
        }
        
        # 将 new_site 和 new_site2 插入到特定位置
        data["sites"].insert(0, new_site)
        data["sites"].insert(1, new_site1)
        data["sites"].insert(3, new_site2)
        data["sites"].insert(4, new_site3)
        data["sites"].insert(5, new_site4)
        data["sites"].insert(6, new_site5)
        data["sites"].insert(7, new_site6)

    else:
        print('"sites" 键不在数据中')

    # 删除指定的键
    keys_to_remove = ["豆瓣","配置","csp_Wogg","csp_Netfixtv","csp_UC","米搜","荐片"]
    data["sites"] = [site for site in data["sites"] if site.get("key") not in keys_to_remove]
    
    # 将修改后的内容转换为 JSON 字符串，并指定 ensure_ascii=False 以确保汉字和表情符号正常显示
    modified_content = json.dumps(data, indent=2, ensure_ascii=False)

    # 将修改后的 JSON 字符串写入 b2.txt 文件中
    with open('b2.txt', 'w', newline='', encoding='utf-8') as f:
        f.write(modified_content)

    print("修改后的内容已写入到 b2.txt 文件中。")

except requests.RequestException as e:
    print(f"请求失败: {e}")

except json.JSONDecodeError as e:
    print(f"JSON 解析失败: {e}")

except Exception as e:
    print(f"发生错误: {e}")
