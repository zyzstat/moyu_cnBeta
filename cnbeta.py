import urllib.request
from bs4 import BeautifulSoup
import sys


def handle_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_text(href):
    category = input(
        """
Enter a category:
                    tech -> 科技
                    movie -> 影视
                    music -> 音乐
                    game -> 游戏
                    comic -> 动漫
                    funny -> 趣闻
                    science -> 科学
                    soft -> 软件
                    Enter -> Only recent News\n
>>"""
    )
    try:
        if category in [
            "tech",
            "movie",
            "music",
            "game",
            "comic",
            "funny",
            "science",
            "soft",
        ]:
            href = href + "/category/{}.htm".format(category)
        elif category not in [
            "tech",
            "movie",
            "music",
            "game",
            "comic",
            "funny",
            "science",
            "soft",
            "",
        ]:
            raise (Exception("Input error, try again"))
        print("Wait for it")
        request = handle_request(href)
        content = urllib.request.urlopen(request).read().decode("utf8")
        soup = BeautifulSoup(content, "lxml")
        odiv = soup.find_all("div", class_="item")
        with open("./cnbeta_txt.txt", "w") as writer:
            if category == "":
                writer.write("------------------热门-----------------\n")
                strip_mark = 0
                for cont in odiv:
                    if "详细内容" in cont.text:
                        strip_mark = 1
                    text = cont.text.replace("\n\n\n", "\n")
                    if "详细内容" in text:
                        writer.write("\n\n\n\n------------------简讯------------------\n")
                    try:
                        text = text[: text.index("详细内容")]
                    except:
                        pass
                    if strip_mark == 1:
                        if text.strip("\n").strip() != "":
                            writer.write(text.strip("\n").strip())
                            writer.write("\n----------------------------------------")
                    else:
                        writer.write(text)
            else:
                writer.write("------------------{}------------------".format(category))
                strip_mark = 0
                for cont in odiv:
                    if "详细内容" in cont.text:
                        strip_mark = 1
                    text = cont.text.replace("\n\n\n", "\n")
                    if "详细内容" in text:
                        writer.write("\n\n\n\n------------------简讯------------------\n")
                    try:
                        text = text[: text.index("详细内容")]
                    except:
                        pass
                    if strip_mark == 1:
                        if text.strip("\n").strip() != "":
                            writer.write(text.strip("\n").strip())
                            writer.write("\n----------------------------------------")
        print("\nEnjoy it\n:)")
    except Exception as e:
        print(e)


get_text("http://cnbeta.com")

print("All recent cnbeta data get, :)!!!")