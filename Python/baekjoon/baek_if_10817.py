A, B, C = map(int, input().split())

if 1<=A<=100 and 1<=B<=100 and 1<=C<=100:
    if A>B:
        if C>A:
            print(A)
        if A>=C:
            if B>C:
                print(B)
            else:
                print(C)
    if B>=A:
        if C>B:
            print(B)
        if B>=C:
            if A>C:
                print(A)
            else:
                print(C)



        
