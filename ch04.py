# 변수와 자료형
# 변수
abc = 12340
print(abc)
abc

print(abc*1/2)
print(abc*1/4)
print(abc*1/5)

# 문자열
# 문자열 만들기
print("String Test")
print('String Test')
# 문자열을 변수에 저장하고 출력
string1 = "String Test 1"
string2 = 'String Test 2'
print(string1)
print(string2)

type(string1)
type(string2)

# 큰 따옴표나 작은따옴표 문자열 안에 포함하기
string3 = 'This is a "double" quotation test'
string4 = "This is a 'single' quotation test"
print(string3)
print(string4)

# 큰 따옴표 + 작은 따옴표 둘다 문자열안에 포함하기: 삼중따옴표
long_string1= '''[삼중 작은 따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표(")와 작은 따옴표(')도 입력할 수 있습니다.'''

long_string2= """[삼중 큰따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표(")와 작은 따옴표(')도 입력할 수 있습니다."""
print(long_string1)
print(long_string2)

# 문자열 다루기
a = 'Enjoy'
b = 'Python!'
c = a + b
print(c)
print(a*3)

#리스트_리스트만들기
# 어떤 학생의 국영수과 점수 리스트
student1 = [90, 95, 85, 80]
student1

type(student1)

# 인덱스 이용하여 리스트의 해당 값 불러오기
student1[0]
student1[1]
student1[-1]#마지막 리스트 값

# 인덱스 이용_새 데이터 할당
student1[1] = 100
student1

myFriends=['James', 'Robert', 'Lisa', 'Mary']
myFriends
myFriends[1]
myFriends[2]
myFriends[3]

# 혼합 형태 리스트
mixedList = [0, 1, 2, 3.14, 'python', 'program', True, myFriends]
mixedList

#리스트 다루기
list_con1 = [1, 2, 3, 4]
list_con2 = [5, 6, 7, 8]
list_con = list_con1 + list_con2
print(list_con)

list_con1 = [1, 2, 3, 4]
list_con = list_con1 * 3
print(list_con)

# 리스트 중 일부 항목 가져오기
list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_data)
print(list_data[0:3])
print(list_data[4:8])
print(list_data[:3])
print(list_data[7:])
print(list_data[::2])

# 리스트 항목 삭제
print(list_data)
del list_data[6]
print(list_data)

# 리스트에서 존재 여부 확인하기
list_data1 = [1, 2, 3, 4, 5]
print(5 in list_data1)
print(6 in list_data1)

# 메서드 실습: append(), insert(), extend()
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.append('Thomas')
print(myFriends)

myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.insert(1, 'Paul')
print(myFriends)

myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.extend(['Laura', 'Betty'])
print(myFriends)

# 튜플_튜플 만들기
tuple1 = (1, 2, 3, 4)
tuple1
type(tuple1)
tuple1[1]

tuple2 = 1, 2, 3, 4
print(tuple2)
type(tuple2)

# 원소가 1개인 튜플을 생성할 경우: ',' 필요
tuple3 = (9, )
tuple4 = 10, 
print(tuple3)
print(tuple4)

# 튜플 다루기
# 에러 나는 경우
tuple5 = (1, 2, 3, 4)
tuple5[1] = 5

del tuple5[1]

# 사용 가능한 것: index(), count()
tuple6 = ('a', 'b', 'c', 'd', 'e', 'f')
tuple6.index('c')

tuple7 = ('a', 'a', 'a', 'b', 'b', 'c', 'd')
tuple7.count('a')

# 세트_세트 만들기
set1 = {1, 2, 3}
set1a = {1, 2, 3, 3}
print(set1)
print(set1a)

type(set1)

# 세트_ 교집합, 합집합, 차집합
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
A.intersection(B)
A.union(B)
A.difference(B)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
A & B
A | B
A - B

# 리스트, 튜플, 세트 간 타입 변환
a = [1, 2, 3, 4, 5]
type(a)

b = tuple(a)
b
type(b)

c = set(a)
c
type(c)

list(b)
list(c)

# 딕셔너리_딕셔너리 만들기
country_capital = {"영국": "런던", "프랑스":"파리", "스위스":"베른", "호주":"멜버른", "덴마크":"코펜하겐"}
country_capital
type(country_capital)
country_capital["영국"]

dict_data1 = {1:"버스", 3:"비행기", 4:"택시", 5:"자전거"}
dict_data1
dict_data1[3]

dict_data2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(dict_data2)
print(dict_data2[4])

dict_data3 = {"list_data1":[11, 12, 13], "list_data2": [21, 22, 23]}
print(dict_data3)
print(dict_data3["list_data2"])

mixed_dict = {1:10, 'dict_num': {1:10, 2:20}, "dict_list_tuple":{"A":[11, 12, 13], "B":(21,22,23)}, "dict_string": "이것은 책입니다."}
mixed_dict

# 딕셔너리 다루기
# 추가
country_capital["독일"]= "베를린"
country_capital

# 수정
country_capital["호주"] = "캔버라"
country_capital

# 삭제
del country_capital["덴마크"]
country_capital

# 딕셔너리 메서드
fruit_code = {"사과":101, "배":102, "딸기": 103, "포도":104, "바나나":105}
print(fruit_code.keys())
print(fruit_code.values())
print(fruit_code.items())

#dict_keys, values, items 을 출력하지 않으면서 값을 받는 방법: list()로 소환
list(fruit_code.keys())
list(fruit_code.values())
list(fruit_code.items())

# 키 update()
fruit_code2 = {"오렌지":106, "수박":107}
fruit_code.update(fruit_code2)
fruit_code

# clear()
fruit_code2.clear()
print(fruit_code2)
type(fruit_code2)