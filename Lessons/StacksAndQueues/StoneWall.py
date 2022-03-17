def solution(H):
    squares = 0
    IncSeries = [0]
    for h in H:
        if h < IncSeries[-1]:
            while len(IncSeries) != 0 and h < IncSeries[-1]:
                IncSeries.pop()
            if IncSeries == []:
                IncSeries = [h]
                squares += 1
            if h > IncSeries[-1]:
                IncSeries.append(h)
                squares += 1
        elif h > IncSeries[-1]:
            IncSeries.append(h)
            squares += 1
    return squares

DemoList = [8,8,5,7,9,8,7,4,8]
print( solution(DemoList) )