#퀴즈 당신의 학교에서는 파이썬 코딩 대회를 주회합니다.
#참석률을 높이기 윟 ㅐ댓글 이벤트를 진행하기로 하였습니다.
#댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle 과 sample 을 활용

from random import *
# lst=[1,2,3,4,5]
# print(lst)
# shuffle(lst) 
# print(lst)
# print(sample(lst,1))

man=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #range(1,21)
shuffle(man)
winning=sample(man,4)

print(winning[0])
print(winning[1:])


