if __name__ == '__main__':
    N=int(raw_input())
    l1=[]
    for x in range(N):
        s=raw_input()
        l=s.split()
        if l[0]=='insert':
            l1.insert(int(l[1]),int(l[2]))
        elif l[0]=='remove':
            l1.remove(int(l[1]))
        elif l[0]=='append':
            l1.append(int(l[1]))
        elif l[0]=='print':
            print l1
        elif l[0]=='sort':
            l1.sort()
        elif l[0]=='pop':
            l1.pop()
        elif l[0]=='reverse':
            l1.reverse()
        else: print("Invalid Input.")
