# 네이버 파파고 api 키
# https://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json

from o_api.external.ocr import response

client_id = '2i_hR7gPkLy0qibmLYsG'
client_secret = 'eo2Nu8w0EA'

encoding_text = urllib.parse.quote("살려줘")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])