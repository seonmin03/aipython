a=list(map(int, input().split()))

if sum(a)>100:
    if a[0]>40 and a[1]>40:
        print("PASS")
    elif a[0]<40:
        print("ENG FAIL")
    else:
        print("MATH FAIL")
else:
    print("FAIL")