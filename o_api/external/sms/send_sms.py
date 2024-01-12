import json
import message

if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01053210064',
                'from': '01053210064',
                'text': '연습'
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
