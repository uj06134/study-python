# https://ocr.space/OCRAPI
# K84512198388957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true
import requests


def parse_text(path):
    url = f'https://api.ocr.space/parse/imageurl?apikey=K86528119188957&url={path}&language=kor&isOverlayRequired=true'
    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    return result['ParsedResults'][0]['ParsedText']













