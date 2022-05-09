
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import ssl

def do_stuff():
    pass
from django.shortcuts import render

#
# def main():
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.pushsafer.com/api'  # Set destination URL here
post_fields = {  # Set POST fields here
    "t": '대진산업',  # 알림상단 텍스트
    "m": '전자문서 결재',  # 테스트 메시지
    "s": 0,  # 사운드재생
    "v": 1,  # 진통설정
    "i": 43,  # 진통설정
    "c": '#00ff00',  # 아이콘색상
    "d": all,
    "u": 'http://3.37.211.248/eas/',
    "ut": '대진산업 전자문서결재',
    "k": 'V7n0lT68dTeoYJU6YQiW'
}

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()

    # context = {'json': json}
    # # if __name__ == "__main__":
    # #     main()
    # return render(request, context)


