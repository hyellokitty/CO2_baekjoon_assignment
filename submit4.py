# 정렬의 경우 지난 동아리 과제로 이미 완료했던 부분이라 submit1.py에 작성되어 있습니다. (2주차에 한꺼번에 올리는 걸로 이해하고 있던 바람에 늦게 업로드하게 되었네요 죄송합니다...!)

import sys
input = sys.stdin.readline


#================================================================================================================================================================


"""  10815번 - 숫자 카드
; 카드에는 숫자가 하나씩 적혀있음 (중복 가능) -> 그런 카드를 현재 N개 가지고 있음
이제 M개의 숫자가 주어질 것 -> 해당 숫자가 적힌 카드를 갖고 있으면 1 없으면 0을 출력 -> 모든 카드에 대해 연속적으로 출력해주면 끝  """

def _10815():
    N = int(input()) # 첫째줄: 가지고 있는 카드의 개수
    card_set = set(map(int, input().split())) # 둘째줄: 각 카드에 적혀있는 숫자
    
    M = int(input()) # 셋째줄: 카드의 존재여부를 확인할 숫자의 개수
    num_list = list(map(int, input().split())) # 넷째줄: 임의로 주어지는 각 숫자

    for i in num_list:
        if i in card_set:
            print(1, end=' ')
        else:
            print(0, end=' ')


#================================================================================================================================================================


"""  14425번 - 문자열 집합
; 집합에는 총 N개의 문자열이 들어있음 -> 이제 M개의 문자열이 주어질 것 -> 각 문자열에 대해 집합에 들어있는지를 확인 -> 그래서 M개 중 총 몇개가 들어있는지 출력  """

def _14425():
    N, M = map(int, input().split()) # 첫째줄: 집합에 들어있는 문자열의 개수, 검사할 문자열의 개수
    str_set = set(input() for _ in range(N)) # 둘째줄부터: 집합에 들어있는 각 문자열

    str_list = [input() for _ in range(M)] # 바로 이어서: 존재여부를 확인할 각 문자열 
    
    count = 0
    for i in str_list:
        if i in str_set:
            count += 1
    print(count)


#================================================================================================================================================================


"""  1620번 - 나는야 포켓몬 마스터 이다솜
; 도감에는 1번부터 N번까지 모두 다른 포켓몬이 들어있음 -> 번호는 빼고 포켓몬 이름만 총 N번을 연속적으로 입력받음 -> 이제 M개의 문제가 주어질 것
무슨 문제냐면... 3, 17 이렇게 숫자가 주어지면 그 숫자에 해당하는 포켓몬 이름을 출력
Ivysaur, Metapod 이렇게 이름이 주어지면 그 이름에 해당하는 포켓몬 번호를 출력  """

def _1620():
    N, M = map(int, input().split()) # 첫째줄: 도감에 들어있는 포켓몬의 개수, 풀어야 하는 문제의 개수
    order_dict = {} # 포켓몬 번호를 키로 하는 딕셔너리 {1: Ivysaur, 2: Metapod, ...}
    name_dict = {} # 포켓몬 이름을 키로 하는 딕셔너리 {Ivysaur: 1, Metopod: 2, ...}
    
    for i in range(1, N+1): # 둘째줄부터: 도감에 들어있는 총 N종류의 포켓몬의 이름 (중복 없음)
        name = input().strip()
        order_dict[i] = name
        name_dict[name] = i
        
    for _ in range(M): # 계속해서 이어서: 풀어야 하는 총 M개의 문제
        question = input().strip()
        if question.isnumeric():
            print(order_dict[int(question)])
        else:
            print(name_dict[question])


#================================================================================================================================================================


"""  10816번 - 숫자 카드 2
; 카드에는 숫자가 하나씩 적혀있음 (중복 가능) -> 그런 카드를 현재 N개 가지고 있음
이제 M개의 숫자가 주어질 것 -> 해당 숫자가 적힌 카드를 몇개 갖고 있는지 출력 (하나도 없으면 0을 출력) -> 모든 카드에 대해 연속적으로 출력해주면 끝  """

def _10816():
    N = int(input()) # 첫째줄: 가지고 있는 카드의 개수
    arr1 = list(map(int, input().split())) # 둘째줄: 각 카드에 적혀있는 숫자

    M = int(sys.stdin.readline()) # 셋째줄: 카드의 존재여부 및 그 개수를 확인할 숫자의 개수
    arr2 = list(map(int, input().split())) # 넷째줄: 임의로 주어지는 각 숫자

    my_dict = {} # 카드에 적혀있는 숫자를 키, 중복되는 카드의 개수를 값으로 하는 딕셔너리 
    # 총 10개의 카드에 적혀있는 숫자 6 3 2 10 10 10 -10 -10 7 3 
    # 그러면 만들어지는 딕셔너리는 {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}
    
    for i in arr1:
        if i not in my_dict: my_dict[i] = 1 # 없는 카드면 추가
        else: my_dict[i] += 1 # 있는 카드면 개수를 +1

    for i in arr2:
        if i in my_dict: print(my_dict[i], end=' ') # 있는 카드면 개수를 출력
        else: print(0, end=' ') # 없는 카드면 0을 출력


#================================================================================================================================================================


"""  1764번 - 듣보잡
; 이름도 못 들어본 사람이 N명, 얼굴도 모르는 사람이 M명 -> 그렇게 총 N+M명의 이름이 주어짐 
-> 이름도 모르고 얼굴도 모르는 사람은 몇명? 그 이름은?  """

def _1764():
    N, M = map(int, input().split()) # 듣지도 못한 사람의 수와 보지도 못한 사람의 수

    set1 = set() # 듣지도 못한 사람의 이름을 저장할 집합
    set2 = set() # 보지도 못한 사람의 이름을 저장할 집합
    res = [] # 듣도 보도 못한 사람의 이름을 저장할 리스트
    
    # 개행문자 제거해서 집합에 추가 -> 교집합을 구함 -> 리스트로 만듦 -> 오름차순으로 정렬
    for _ in range(N):
        n = input().strip()
        set1.add(n)
    for _ in range(M):
        m = input().strip()
        set2.add(m)
    res = sorted(list(set1 & set2))
    
    # 듣보잡의 수와 그 이름들을 출력
    print(len(res))
    for i in res: print(i)


#================================================================================================================================================================


"""  1269번 - 대칭 차집합  
; 어떤 두 집합 A와 B가 주어짐 -> 대칭 차집합의 원소의 개수는? -> A-B ∪ B-A 구해서 len(저거) 출력
예를 들어 A = {1 2 4}, B = {2 3 4 5 6} -> A-B = {1}, B-A = {3 5 6} -> A-B ∪ B-A = {1 3 5 6} -> 4 출력하기만 하면 끝  """

def _1269():
    N, M = map(int, input().split()) # 집합 A의 원소의 개수와 집합 B의 원소의 개수
    A = set(map(int, input().split())) # 집합 A의 총 N개의 원소
    B = set(map(int, input().split())) # 집합 B의 총 M개의 원소

    A_B = A.difference(B) # 집합 A-B를 구한 것
    B_A = B.difference(A) # 집합 B-A를 구한 것
    
    print(len(A_B) + len(B_A)) # 원소의 개수를 더해서 출력


#================================================================================================================================================================


"""  11478번 - 서로 다른 부분 문자열의 개수
; 어떤 문자열이 주어짐 -> 모든 부분 문자열을 구함 (이때는 중복 O) -> 서로 다른 부분 문자열의 '개수'만 출력 (이때는 중복 X)
예를 들어 ababc -> a b a b c ab ba ab bc aba bab abc abab babc ababc -> 개수는 15인데 중복 제외하면 12개
이거 그냥... 0:1~0:5 a ab aba abab ababc / 1:2~1:5 b ba bab babc / 2:3~2:5 a ab abc / 3:4~3:5 b bc / 4:5 c
싹 다 집합에 넣어두면 알아서 중복 제거 -> 마지막에 len(집합) 출력하면 끝  """

def _11478():
    S = input().strip() # 부분 문자열을 구할 전체 문자열
    part = '' # 구해진 각 부분 문자열 (위에서 a, aba 이런 것)
    res = set() # 중복 제거를 위해 집합에 저장
    
    for i in range(len(S)): # 슬라이싱 왼쪽 고정해두고 오른쪽 1(사실 0)부터 5(사실 4)까지 자르기
        for j in range(i, len(S)):
            part = S[i:j+1]
            res.add(part)
    
    print(len(res))

