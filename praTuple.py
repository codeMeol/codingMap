# #Tuple

# menu=("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])


# name="김종국"
# age=20
# hobby="헬스"

# (name, age, hobby)= ("김종국" , 20 , "코딩")
# print(name,age,hobby)

# #set
# #중복안됨 순서없음

# my_set={1,2,3,3,3}
# print(my_set)

# java={"유재석","김태호","양세형"}
# python= set(["유재석","박명수"])

# # #교집합 자바와 파이썬을 모두 할수있는 개발자
# # print(java & python)
# # print(java.intersection(python))

# # #합집합 자바나 파이썬 둘중 하나라도 하는 개발자

# # print(java|python)
# # print(java.union(python))

# # #차집합 자바는 할줄 알지만 파이썬은 모르는 개발자

# # print(java -python)
# # print(java.difference(python))

# # #python 할줄 아는 사람이 늘어남
# # python.add("김태호")
# # print(python)

# #java를 까먹은 사람
# java.remove("김태호")
# print(java)

#자료구조의 변경
# menu={"커피","우유","주스"}
# print(menu, type(menu))

# menu=list(menu)
# print(menu,type(menu))

# menu=tuple(menu)
# print(menu,type(menu))

# weather= input("오늘 날씨는 어때요?")
# if  weather== "비":
#     print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if temp>=30:
#     print("너무 더워요 나가지 마세요")
# elif temp >= 10 or temp <30:
#     print("나갈만 해")
# else:
#     print("너무 추워요 나가지 마요")

# for waiting_no in range(1,6):
#     print("대기번호 :{0}".format(waiting_no))

# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}님 커피가 준비 되었습니다".format(customer))

#while
# customer= "토르"
# index = 5
# while index>= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer,index))
#     index-=1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")


customer = "토르"
person="Unknown"

while person !=customer:
    print("{0},커피가 준비 되었습니다.".format(customer))
    person= input("이름이 어떻게 되세요?")
print("맛있게드세요")    