## 인원수랑 공포도 입력받기!
n = int(input("모험가 수 입력:"))  ##  모험가의 수 받고
num_list = list(map(int, input("공포도 입력:").split()))  # 공포도 1차원 배열 입력받기!


if  n != len(num_list):
    print("모험가 수에 맞게 입력해라 시이발")

    


group = 0 # 총그룹 수
cnt= 0   # 현그룹 사람수


for i in num_list:
    cnt += 1 # 현그룹 인원 수 추가!
    #print("전그룹 인원수",cnt)
    print("전그룹 인원수",cnt)
    if i <= cnt: # 공포도 보다 사람이 많으면! 다음 그룹으로 넘어가야지
        group+= 1
        cnt = 0

        
print(group)
