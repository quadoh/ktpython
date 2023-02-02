# N이 10보다 작으면 앞에 0을붙인다.
# 각 자리의 숫자를 더하고 ex) 26 => 2+6=8
# 제일 오른쪽 자리수와 앞의 오른쪽 자리 수를 합친다 ex) 26 => 26, 2+6 =8,  => 68
# 몇번 반복해서 원래 입력받은 N이 되는지 구한다
# 싸이클의 횟수를 count에 넣는다

def cycle(N) :
    trans=-1
    if(N<10):
        trans = N*10 + N
    else :
        trans = int((N%10)*10 + (N/10 + N%10) % 10)
    #print(trans)
    return trans

# 0 <= N <= 99
N = int(input())

count = 0

check = N
while True:
    check = cycle(check)
    if N == check:
        count+=1
        break
    else :
        cycle(check)
        count+=1

print(count)
