# https://open.kattis.com/problems/jumbojavelin
data = []

def mult (list):
    N = int(list[0])
    length = 0
    count = 0
    if len(list) - N == 1 and 1 < N <= 100:
        for i in range(1, len(list)):
            if 1 <= int(list[i]) <= 50:
                length += int(list[i])
                count += 1
                if count>1:
                    length -= 1
        print(length)


line = input()
data.append(line)
for round in range(int(line)):
    lines = input()
    data.append(lines)
mult(data)









