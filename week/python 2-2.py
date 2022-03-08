#함수정의 한 후 반드시 함수 호출

# 더하기 함수
def add(a,b):
    c = a + b
    return c
# 빼기함수
def minus(a,b):
    c = a - b
    return c
# 곱하기 함수
def multi(a,b):
    c = a * b
    return c
# 나누기 함수
def divide(a,b):
    c = a / b
    return c


while True:
    c = input("1st input")
    a = int(c)
    if a == "0000":
        break
    
    b = int(input("2nd input?"))
    a = int(a);

    result = a + b
    print(a, '+', b, '=', result)
    result = a - b
    print(a, '-', b, '=', result)
    result = a * b
    print(a, '*', b, '=', result)
    result = a / b
    print(a, '/', b, '=', result)

print("end of program")

