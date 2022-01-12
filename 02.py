# https://open.kattis.com/problems/busnumbers
data = []
merge = []
ans = []

def bus(data):
    data = list(map(int, data))
    data.sort()

    loop = 0
    for index in range (len(data)):
        for i in range (loop, len(data)):

            # first number / one number
            if len(merge) == 0:
                merge.append(data[i])
                if len(data) == 1:
                    ans.append(data[i])
                    break

            # other number
            elif len(merge) > 0:
                if data[i-1]+1 == data[i]:
                    merge.append(data[i])
                else:
                    if len(merge) > 2:
                        msg = str((merge[0]))+'-'+str(merge[len(merge)-1])
                        ans.append(msg)
                    else:
                        for k in range (len(merge)):
                            ans.append(merge[k])
                    loop += len(merge)
                    merge.clear()
                    break
                    
    stra = ' '.join(map(str, ans))
    print(stra)

# input data
count = input()
lines = input()
strinput = lines.split(' ')
seen = set()
for x in strinput:
    if x not in seen:
        data.append(x)
        seen.add(x)
bus(data)
