if __name__ == '__main__':
    n = int('4')
#    arr = map(int, '2 3 6 6 5'.split())
    arr = map(int, '57 57 -57 57'.split())
    arr.sort()
    s=set(arr)
    l=list(s)
    print l
#    print l[len(l)-2]
    print sorted(l)[-2]
