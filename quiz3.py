# 퀴즈 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# https:// 부분은 제외 =>naver.com
# 처음만나는 점 이후 부분은 제외
# 남은 글자중 처음 세자리 + 글자갯수 글자 내 'e'갯수 +"!"로 구성


from ast import Index
from typing import Counter


print("입력받은 주소는 %s입니다." %"http://naver.com")
www="http://google.com"
www=www[www.index("http://")+7:]
www=www[:www.index(".")]
pas=www[:3]+str(len(www))+str(www.count("e"))+"!"
print(www)
print(pas)

