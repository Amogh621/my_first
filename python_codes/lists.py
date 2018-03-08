n=int(raw_input())
if n<2 or n>5:
    print 'Invalid Input.'
else:
    l=[]
    #l.append(for _ in range(n):
    #    name = raw_input()
    #    score = float(raw_input()))   #not working
    for _ in range(n):
        name = raw_input()
        score = float(raw_input())
        l.append([name,score])
    l.sort(key=lambda l: l[1])
    l1=[]
    for x in l:
        l1.append(x[1])
    min2=min(l1)
    for x in l1:
        if x>min2:
            min2=x
            break;
    l2=[]
    for x in l:
        if x[1]==min2:
            l2.append(x[0])
    l2.sort()
    print l2
