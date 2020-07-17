



citations = [9,4,9,8,4]
def hIndex(citations):
    n = len(citations)
    c = sorted(citations)


    for i in range(n):
        if c[i] >= n-i:
            print(n-i) 
    print(0)


hIndex(citations)