import json
import random

import requests
import wget
import logging
douyin_url_1 = 'https://aweme.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.0&pull_type=1&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&ts=1542462470&js_sdk_version=1.2.2&app_type=normal&os_api=22&device_type=MI%206%20&device_platform=android&ssmix=a&iid=51483898235&manifest_version_code=330&dpi=240&uuid=863254010024783&version_code=330&app_name=aweme&version_name=3.3.0&openudid=b88687ce061b2143&device_id=59556438311&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Xiaomi&ac=wifi&update_version_code=3302&aid=1128&channel=tianzhuo_dy_wifi1&_rticket=1542462471640&as=a1a5a15f96707b9cf04444&cp=1b04b3576001f8cbe1Ycag&mas=01017320dc681b4a0a48a4f08daad786382c2c2c2c0c66c69c46ec'

douyin_url_2 = 'https://api.amemv.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.0&pull_type=1&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&ts=1542465317&js_sdk_version=1.2.2&app_type=normal&os_api=22&device_type=MI%206%20&device_platform=android&ssmix=a&iid=51483898235&manifest_version_code=330&dpi=240&uuid=863254010024783&version_code=330&app_name=aweme&version_name=3.3.0&openudid=b88687ce061b2143&device_id=59556438311&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Xiaomi&ac=wifi&update_version_code=3302&aid=1128&channel=tianzhuo_dy_wifi1&_rticket=1542465317979&as=a105b27fb5e27bf7104800&cp=2324b1585204f870e1OcWg&mas=01496700b76be3b975796eb721b2d95a700c0c1c2c0c8cec6646ec'

douyin_url = []

douyin_url.append(douyin_url_1)
douyin_url.append(douyin_url_2)

class MyLogging:
    def __init__(self):
        filename = 'douyin.log'
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        sh = logging.StreamHandler()
        sh.setLevel(logging.ERROR)

        fh = logging.FileHandler(filename=filename)
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")  # 定义日志输出格式

        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

mylogger = MyLogging().logger

header = {
    'User-Agent': 'okhttp/3.1'
}

session = requests.session()

while 1:
    douyin_url_req = random.sample(douyin_url,1)[0]
    douyin_data = session.get(douyin_url_req, headers=header)
    data = json.loads(douyin_data.text)

    url_list = data['aweme_list']

    for url in url_list:
        video_url = url['video']['play_addr']['url_list'][0]
        music_url = url['music']['play_url']['uri']
        music_title = url['music']['title']

        try:
            wget.download(url=music_url, out='D:\\Temp\\douyin_music\\{}'.format(music_title + '.mp3'))
            mylogger.info(music_url)
        except:
            print(video_url)
        video_name = url['desc']
        try:
            wget.download(url=video_url, out='D:\\Temp\\douyin2\\{}'.format(video_name + ".mp4"))
            mylogger.info(video_url)
        except:
            print(video_url)