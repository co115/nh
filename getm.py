import os
import requests
import re
from datetime import datetime
import subprocess
import sys
import pytz

try:
    import pytz
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytz"])
    import pytz

headers = {'User-Agent': 'okhttp/3.15'}

url1 = os.getenv("URL_1")
url2 = os.getenv("URL_2")
url3 = os.getenv("URL_3")
JK = os.getenv("JK", "false").lower() == "true"

beijing_tz = pytz.timezone('Asia/Shanghai')
current_beijing_time = datetime.now(beijing_tz)

current_date_str = current_beijing_time.strftime("%Y-%m-%d")

processed_contents = [None] * 3

urls = [url1, url2, url3]

url3_playlist = ""

if JK and url3:
    try:
        response = requests.get(url3, headers=headers)
        response.raise_for_status()
        url3_playlist = response.text
        response.encoding = 'utf-8'
        print(f"从 {url3} 获取到的内容长度: {len(url3_playlist)}")

        pattern = re.compile(
            r'(🐼电视公告[\s\S]*?(?=(VIP|🔥|🐼|$)))|'
            r'(<script[\s\S]*?</script>)',
            flags=re.IGNORECASE
        )

        updated_playlist = re.sub(pattern, '', url3_playlist)

        updated_playlist = re.sub(r'\n{2,}', '\n\n', updated_playlist).strip()

        updated_playlist = re.sub(r"更新\d{4}-\d{2}-\d{2},", f"更新{current_date_str},", updated_playlist)

        if not updated_playlist.endswith('\n'):
            updated_playlist += '\n'

        url3_playlist = updated_playlist
        print(f"URL3 内容已成功处理")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {url3} - {e}")
        url3_playlist = ""

for index, url in enumerate(urls[:2]):
    try:
        if url:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            playlist = response.text

            response.encoding = 'utf-8'
            playlist = response.text

            print(f"从 {url} 获取到的内容长度: {len(playlist)}")

            if url == url1:
                playlist = re.sub(r'更新时间[\s\S]*?(?=(🐼|💓|$))', '', playlist)
                playlist = re.sub(r'<script[\s\S]*?</script>', '', playlist)
                playlist = "\n".join(line.replace(",,", ",") for line in playlist.strip().split("\n"))

                # 判断是否是m3u格式
                if playlist.startswith("#EXTM3U"):
                    print("检测到 m3u 格式，正在转换为 txt 格式...")
                    m3u_content = []
                    group_titles = {}  # 用于存储每个 group-title 对应的频道信息
                    lines = playlist.splitlines()

                    for i, line in enumerate(lines):
                        if line.startswith("#EXTINF"):
                            match = re.search(r'group-title="([^"]+)"', line)
                            if match:
                                group_title = match.group(1)
                                channel_name = line.split(",")[-1].strip()
                                url_line = lines[i + 1].strip() if i + 1 < len(lines) and not lines[i + 1].startswith("#") else None

                                # 将相同的 group-title 合并到同一个 group
                                if group_title not in group_titles:
                                    group_titles[group_title] = {
                                        "channels": [],
                                        "urls": []
                                    }

                                if channel_name not in group_titles[group_title]["channels"]:
                                    group_titles[group_title]["channels"].append(channel_name)

                                if url_line and url_line not in group_titles[group_title]["urls"]:
                                    group_titles[group_title]["urls"].append(url_line)

                    # 构建新的 m3u 内容
                    for group_title, data in group_titles.items():
                        m3u_content.append(f"{group_title}, #genre#")
                        for channel, url in zip(data["channels"], data["urls"]):
                            m3u_content.append(f"{channel}, {url}")
                        m3u_content.append("")

                    playlist = "\n".join(m3u_content)
                    print("m3u 内容已成功转换为 txt 格式")

            if url3_playlist:
                url3_playlist = re.sub(r'^AKTV','#genre#\n?', '', url3_playlist)
                pattern = r'(🔥AKTV恢复,#genre#)[\s\S]*?(?=(VIP|🔥|🐼|$))'
                playlist = re.sub(pattern, r'\1\n' + url3_playlist + '\n', playlist)

            if url == url2:
                playlist = re.sub(r"更新\d{4}-\d{2}-\d{2},", f"更新{current_date_str},", playlist)
                with open("zl.txt", "w", encoding='utf-8') as file:
                    file.write(playlist)
                
                print("已更新")

            playlist = re.sub(r'\n{2,}', '\n\n', playlist).strip()

            if not playlist.endswith('\n'):
                playlist += '\n'

            processed_contents[index] = playlist

            print(f"内容已成功从 {url} 获取并处理")

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {url} - {e}")
        processed_contents[index] = ""

pattern_aktv = r'🔥AKTV恢复,#genre#'
aktv_found_in_url1 = False

if url1 and re.search(pattern_aktv, processed_contents[0] if processed_contents[0] else ''):
    aktv_found_in_url1 = True

if not aktv_found_in_url1:
    write_order = [1, 2, 0]

    with open("z1.txt", "w", encoding='utf-8') as file:
        if processed_contents[1]:
            file.write(processed_contents[1])
            file.write("\n")
        if url3_playlist:
            file.write("网络推流,#genre#\n")
            file.write(url3_playlist)
            file.write("\n")
        if processed_contents[0]:
            file.write(processed_contents[0])
            file.write("\n")

    print("已处理1")
else:
    write_order = [1, 0]

    with open("z1.txt", "w", encoding='utf-8') as file:
        for idx in write_order:
            if idx < len(processed_contents) and processed_contents[idx]:
                file.write(processed_contents[idx])
                file.write("\n")

    print("已处理2")
