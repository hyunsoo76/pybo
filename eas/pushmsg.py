
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
# import ssl
# from asgiref.sync import sync_to_async

# # def push():
# #
# #     if __name__ == "__main__":
# #         return
# #     else:
# #         pass
# from django.shortcuts import render

# def main():
#     ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://www.pushsafer.com/api'  # Set destination URL here
# post_fields = {  # Set POST fields here
#     "t": '대진산업',  # 알림상단 텍스트
#     "m": '전자문서 결재',  # 테스트 메시지
#     "s": 0,  # 사운드재생
#     "v": 1,  # 진동설정
#     "i": 78,  # 아이콘
#     "c": '#00CC00',  # 아이콘색상
#     "d": all,
#     "u": 'http://3.37.211.248/eas/',
#     "ut": '대진산업 전자문서결재',
#     "k": 'V7n0lT68dTeoYJU6YQiW'
# }

# request = Request(url, urlencode(post_fields).encode())
# json = urlopen(request).read().decode()

#     # context = {'json': json}
# if __name__ == "__main__":
#       main()
#     # return render(request, context)

# 위의 코드가 approvals 만들기전 파일

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError
import ssl

# Pushsafer API URL
PUSHSAFER_API_URL = "https://www.pushsafer.com/api"

# SSL 인증서 문제로 죽지 않게 기본 컨텍스트 조정 (필요할 때만 사용)
ssl._create_default_https_context = ssl._create_unverified_context


def send_push(
    title="대진산업",
    message="전자문서 결재",
    url="http://3.37.211.248/eas/",
    url_title="대진산업 전자문서결재",
):
    """
    Pushsafer로 푸시 알림을 전송하는 함수.
    장고가 import 할 때는 아무 작업도 하지 않고,
    필요할 때 view 등에서 이 함수를 직접 호출해서 사용.
    """
    post_fields = {
        "t": title,          # 알림 상단 텍스트
        "m": message,        # 메시지
        "s": 0,              # 사운드 재생
        "v": 1,              # 진동 설정
        "i": 78,             # 아이콘
        "c": "#00CC00",      # 아이콘 색상
        "u": url,            # 클릭 시 열리는 URL
        "ut": url_title,     # URL 제목
        "k": "V7n0lT68dTeoYJU6YQiW",  # Pushsafer 키 (기존 값 사용)
    }

    request = Request(PUSHSAFER_API_URL, urlencode(post_fields).encode())

    try:
        response = urlopen(request, timeout=5)
        text = response.read().decode()
        print("Pushsafer 응답:", text)
        return text
    except URLError as e:
        # 로컬 개발 환경에서는 여기서 에러 나도 서버가 죽지 않도록 방어
        print("Pushsafer 전송 오류:", e)
        return None
    except Exception as e:
        print("Pushsafer 기타 오류:", e)
        return None


if __name__ == "__main__":
    # 단독 실행 테스트용 (python pushmsg.py 로 실행할 때만 동작)
    send_push()

