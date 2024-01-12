import hello

# 실행 대상인 파일의 모듈명(__name__)이 '__main__'이라면 실행할 코드 작성
# 여러 개의 모듈을 import하여 사용할 때 가장 처음으로 실행될 메인 파일을 구분하는 코드이다.
# 즉, 모듈인지 시작점인지 구분하기 위해 사용한다.
if __name__ == '__main__':
    print('Hello Python')