# https://open.kattis.com/problems/busnumbers
data = []


def checkdata (lists):
    Number = []
    N = int(lists[0])
    Number = lists[1].split(' ')
    Number = list(map(int, Number))
    Number.sort()
    Number = list(map(str, Number))
    Check = 0
    if N == len(Number) and 1 <= N <= 1000:
        for i,num in enumerate(Number):
            if 1 < int(num) < 1000:
                Check += 1

        seen = set()
        uniq = []
        for x in Number:
            if x not in seen:
                uniq.append(x)
                seen.add(x)

        return uniq
    else:
        return 0


def bus (list):
    Merge = []
    Ans = []

    Num = []
    Num = checkdata(list)
    if not Num == 0:
        if len(Num) == 1:
            Ans.append(Num[0])
        else:
            for i in range(1, len(Num)):
                if int(Num[i]) - int(Num[i - 1]) == 1:
                    if len(Merge) >= 0:
                        Merge.append(Num[i - 1])
                else:
                    if len(Merge) == 0:
                        Ans.append(Num[i - 1])
                    elif len(Merge) > 0:
                        if int(Num[i - 1]) - int(Num[i - 2]) == 1:
                            Merge.append(Num[i - 1])

                            if len(Merge) > 2:
                                msg = str(min(Merge)) + '-' + str(max(Merge))
                                Ans.append(msg)
                                Merge.clear()
                            else:
                                for j, x in enumerate(Merge):
                                    Ans.append(x)
                                Merge.clear()
                        else:
                            Ans.append(Num[i - 1])
                    else:
                        Ans.append(Num[i])

                # last number
                if i == len(Num) - 1:
                    if len(Merge) > 0:
                        if int(Num[i]) - int(Num[i - 1]) == 1:
                            if len(Merge) >= 0:
                                Merge.append(Num[i])

                        if len(Merge) > 2:
                            msg = str(min(Merge)) + '-' + str(max(Merge))
                            Ans.append(msg)
                            Merge.clear()
                        else:
                            for i, x in enumerate(Merge):
                                Ans.append(x)
                            Merge.clear()
                    else:
                        Ans.append(Num[i])

                #print(Ans)

        stra = ' '.join(map(str, Ans))
        print(stra)



line = input()
data.append(line)
for round in range(1):
    lines = input()
    data.append(lines)
bus(data)