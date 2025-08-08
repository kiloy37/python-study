print("자료형 확인 프로그램 입니다")
int_a = 13;
print(type(int_a))
float_b = 10.123
print(type(float_b))
str_c = "스트링"
print(type(str_c))

x = 1e3
print('1e3 = ',x)

print(abs(-10))
print(abs(5.5))

str_x = "안녕하세요"
print(str_x)
print(type(str_x))

str_y = '안녕하세요'
print(str_y)
print(type(str_y))

ttt = True
print(type(ttt))
fff = False
print(type(fff))

arr_x = [10,20,30,40,50]
print(type(arr_x))
print("배열 0번째 = ",arr_x[0])
print("배열 1번째 = ",arr_x[1])
print("배열 2번째 = ",arr_x[2])
print("배열 3번째 = ",arr_x[3])
print("배열 4번째 = ",arr_x[4])
print("배열 -1번째 = ",arr_x[-1])
print("배열 -2번째 = ",arr_x[-2])
print("배열 -3번째 = ",arr_x[-3])
print("배열 -4번째 = ",arr_x[-4])
print("배열 -5번째 = ",arr_x[-5])

print("arr_x 의 원소갯수는 = ",len(arr_x))


arr_y = [ 'a','b','c','d','e','f'] 

print("슬라이싱 예제")
print("arr_x 의 2번째 이후",arr_y[2:])
print("arr_x 의 4번째 미만",arr_y[:4])
print("arr_x 의 2~4번째",arr_y[2:4])

dic_a = {'a':10,'b':20,'c':30,'d':40,'e':50}
print("a 의 점수는 : ", dic_a['a'])
print("b 의 점수는 : ", dic_a['b'])
print("c 의 점수는 : ", dic_a['c'])
print("d 의 점수는 : ", dic_a['d'])
print("e 의 점수는 : ", dic_a['e'])

x = 123.2323
print(int(x) , type(x) , type(int(x)))

x = True
print(type(x) , float(x) ,str(x))

x = ['a','b','c']
y = ['d','e','f']
print(x.append('d'))

x = ['a', 'b', 'c', 'd']

removed_value = x.pop(1)
print(removed_value)
print(x)

a = [1, 2, 3]
b = [4,5, 6]
print(a+b)

a = [1, 2, 3]
b = a * 3
print(b)

a = 3
a = a+a
print(a)

a = 1000
a = a**0.5
print(a)


x = 30
if x<20 :
    print("참")
else :
    print("아닌데윰")
