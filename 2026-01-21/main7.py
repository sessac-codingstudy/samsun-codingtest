물의 온도를 정수로 입력받아 0℃ 미만일경우엔 ice, 100℃ 이상일때는vapor, 그 외의 경우는 water 라고 출력하는 프로그램을 작성해주세요.
첫번쩨 줄에는 물의 온도인 정수 n이 주어집니다
제한 조건  -200<= n <= 200
물의 온도에 따른 현재 상태를 문자여로 출력해주세요

물의 온도 입력 
n = int(input())
if n < 0:
    print("ice")
elif n >= 100:
    print("vapor")
else:
    print("water")