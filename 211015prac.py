cabinet = {3:"유재석", 100:"김태호"}
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))


print(3 in cabinet) #true
print(5 in cabinet) #false

print(cabinet["A-3"])
print(cabinet["b-100"])

print(cabinet)
cabinet["A-3"]="김종국"
cabinet["c-20"]= "조세호"
print(cabinet)
