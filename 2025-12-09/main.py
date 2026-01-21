# 변수를 선언해서 정수 a,b를 입력받고, 다음 조건에 따라 만족하면 1을, 만족하지 않는다면 0을 각 줄에 출력합니다
# input() 한줄로 입력
# split() 입력한 문자열 공백 기준으로 나눔
# map(int,..)"",""를 정수로 (int)로 바뀜

a,b = map(int,input().split())

print(int(a >= b))
print(int(a > b ))
print(int(a <= b ))
print(int(a < b ))
print(int(a == b ))
print(int(a != b ))
