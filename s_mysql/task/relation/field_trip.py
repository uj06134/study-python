# DBMS에서 조회한 결과를 화면에서 사용하기 위한 목적으로 만든 클래스이다.
class FieldTrip:
    def __init__(self, id, title, content, count, *files):
        self.id = id
        self.title = title
        self.content = content
        self.count = count
        self.files = files

    def get_full_path(self):
        paths = []
        for file in self.files:
            paths.append(f"/upload/{file.get('file_path')}/{file.get('file_name')}")
        return tuple(paths)
