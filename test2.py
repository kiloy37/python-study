x = 27

z = False
count = 0

while count < 20:
    count += 1
    if count < 5 :
        continue
    elif count > 10 :
        break
    else :
        print(count)
        
for i in range(100):
    y = int(input("숫자를 예상해보세요"))
    if x == y :
        print("정답!")
        break
    elif x > y :
        print("작습니다")
    else :
        print("큽니다")