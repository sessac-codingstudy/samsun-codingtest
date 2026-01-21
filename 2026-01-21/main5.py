 두 개의 정수를 입력받아 첫번째 수가 더 작으면 1을, 아니면  0을 출력하고 , 두 개의 수가 같으면 1을, 아니면 0을 출력  A,B 공백을 두고 주어집니다
 첫번째 줄에 정수A,B공백을 사이에 두고 주어집니다

제한 조건 1<=A,B<=100

A,B = map(int, input().split())
first = 1 if A < B else 0
second = 1 if A == B else 0
print(first,second)
    
결과값 숫자 두개를 공백을 사이에 두고 출력 