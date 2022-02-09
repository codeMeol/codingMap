# # print(5)
# # print(-10)
# # print(3.14)
# # print(1000)
# # print(5+3)
# # print(2*8)
# # print(3*(3+1))
# # print(5+3)
# # print(5+3)
# # print(5+3)

# # print('풍선')
# # print('풍선')
# # print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# # print('ㅋ'*9)

# # print(5>10)
# # print(5<10)
# # print(True)
# # print(False)
# # print(not True)
# # print(not (5>10))

# # animal = "강아지"
# # name = "연탄이"
# # age = 4
# # hobby= "산책"
# # is_adult = age>=3

# # print("우리집"+animal+"의 이름은"+name+"예요")
# # print(name+"는 "+str(age)+"이며, "+hobby+"을 아주 좋아해요")
# # print(name+"는 어른일까요? "+str(is_adult))

# # animal = "고양이"
# # name = "나비"
# # age = 2
# # hobby= "뒹굴어버리기 "
# # is_adult = age>=3

# # print("우리집"+animal+"의 이름은"+name+"예요")
# # print(name+"는 "+str(age)+"이며, "+hobby+" 을 아주 좋아해요")
# # print(name+"는 어른일까요? "+str(is_adult))

# # print(2 + 3 * 4) #14
# # print((2+3)*4) #20

# # number= 2+3 *4 #14
# # print(number)
# # print(number+"=2")

# # print(abs(-5)) #5 절대값
# # print(pow(4,2)) #4^2=4 *4 = 16 4에 2승 제곱이란 뜻
# # print(max(5,12)) #12 5부터 12중에 가장 큰값
# # print(min(5,12)) #5 5부터 12중에 가장 작은값
# # print(round(3.14)) #3  반올림 
# # print(round(4.99)) #5  반올림

# # from math import *
# # print(floor(4.99)) # 내림=>4
# # print(ceil(3.14)) # 올림 ->4
# # print(sqrt(16)) # 제곱근 4

# import math
# from random import *

# # print(random()) #0.0~ 1.0미만의 임의의 값 생성
# # print(random() * 10) #0.0~10.0 미만의 임의의 값 생성
# # print(int(random()*10)) #0~10 미만의 임의의 값 생성
# # print(int(random()*10)) #0~10 미만의 임의의 값 생성
# # print(int(random()*10)) #0~10 미만의 임의의 값 생성

# # print(int(random()*45+1))
# # print(int(random()*45+1))
# # print(int(random()*45+1))
# # print(int(random()*45+1))
# # print(int(random()*45+1))
# # print(int(random()*45+1))

# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1,46)) #1~46 미만의 임의의 값 생성

# # print(randint(1,45))#1~45 이하의 임의의 값 생성
# # print(randint(1,45))#1~45 이하의 임의의 값 생성
# # print(randint(1,45))#1~45 이하의 임의의 값 생성
# # print(randint(1,45))#1~45 이하의 임의의 값 생성
# # print(randint(1,45))#1~45 이하의 임의의 값 생성
# # print(randint(1,45))#1~45 이하의 임의의 값 생성

# # sentence = '나는 소년입니다'
# # print(sentence)
# # sentence2= "파이썬은 쉬워요"
# # print(sentence2)
# # sentence3= """
# # 나는 소년이고 ,
# # 파이썬은 쉬워요
# # """
# # print(sentence3)

# # jumin="990120-1234567"

# # print("성별 : "+ (jumin[7]))
# # print("연 : "+ jumin[0:2]) #0~2직전까지
# # print("월 : "+jumin[2:4])
# # print("일 : "+ jumin[4:6])

# # print("생년월일 :"+jumin[:6])
# # print("뒤 7자리 :"+ jumin[7:]) #7부터  끝까지
# # print("뒤 7자리(뒤에부터) : " +jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# # python = "Python is Amazing"

# # print(python.lower()) # all lower case
# # print(python.upper()) # all upper case
# # print(python[0].isupper()) #if first spelling is uppercase then return true
# # print(len(python)) #return "python"`s length
# # print(python.replace("Python", "java")) #change Python to java

# # index= python.index("n") #index, when you find "n" return "n"`s place number
# # print(index)
# # index = python.index("n",index + 1) # index + 1 mean, you would find n then refind n from "n+1" place
# # print(index)

# # print(python.find("java")) # if find java return -1 because cannot found java 
# # print(python.index("java"))  #use index => return error because cannot found java

# # print("나는 % d살입니다." %20)
# # print("나는 % s을 좋아해요"%"파이썬")
# # print("Apple은 %c로 시작해요"%"A")

# # print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

# # print("나는 {}살입니다.".format(20))
# # print("나는 {}색과,{}색을 좋아해요".format("파란","빨간"))
# # print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# # age=20
# # color = "빨간"

# # print(f"나는{age}살이며,{color}색을 좋아해요")

# # print("백문이 불여일견\n 백견이 불여일타")

# # # print('저는 "나도코딩"입니다.')
# # print("저는 \"나도코딩\"입니다.")

# # #\\는문장 내에서 \

# # print("     Red    Apple     \rPine")

# #리스트 []

# #지하철 칸별로 10명, 20명 ,30명

# # subway1=10
# # subway2=20
# # subway3=30

# # subway =[10,20,30]
# # print(subway)
# # subway=["유재석","조세호","박명수"]
# # print(subway)
# # #조세호씨가 몇번째 타고계시니
# # print(subway.index("조세호")+1)
# # #하하씨가 다음 정류장에서 다음 칸에 탐
# # subway.append("하하")
# # print(subway)

# # subway.insert(1,"정형돈")
# # print(subway)

# # subway.pop()
# # print( subway)

# # num_list=[1,2,5,4,3,6]
# # num_list.sort()
# # print(num_list)

# # num_list.reverse()
# # print(num_list)

# # num_list=[1,2,5,4,3,6]
# # #//extend 리스트 합치기
# # mix_list=["조세호",20,True]
# # num_list.extend(mix_list)
# # print(num_list)

# cabinet={3:"유재석", 100:"김태호"}
# # print(cabinet[3])
# # print(cabinet[100])

# # print(cabinet.get(3))
# # print(cabinet.get(5,"사용가능"))
# # print("hi")

# print(3 in cabinet) # true
# print(5 in cabinet) # false

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] ="조세호"
# print(cabinet)

# del cabinet["A-3"]
# print("김종국 컷"+str(cabinet))

# #key 들만 출력

# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key value 쌍으로 출력
# print(cabinet.items())

# #clear 함수
# print(cabinet.clear())
