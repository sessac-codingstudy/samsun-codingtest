inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

print(f"{a + b} {(a + b) / 2:.1f}")

inp = input() #  한 줄의 문자열 입력. 예: "10 20"
arr = inp.split() # 입력받은 문자열을 공백(띄어쓰기)을 기준으로 나누어 리스트(arr)에 저장. 예: ["2", "5"]
a = int(arr[0]) # 리스트의 첫 번째 요소(문자열)를 정수형(integer)으로 변환하여 변수 a에 저장. 예: a = 2
b = int(arr[1]) # 리스트의 두 번째 요소(문자열)를 정수형(integer)으로 변환하여 변수 b에 저장. 예: b = 5
print(f"{a+b} {(a+b) / 2:.1f}") # a와 b의 합, 그리고 a와 b의 평균을 출력합니다.
                               # f-string을 사용하여 문자열을 포맷하며, 평균은 소수점 첫째 자리까지(.1f) 표시합니다.