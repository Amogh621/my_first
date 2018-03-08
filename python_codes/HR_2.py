import sys
if __name__ == '__main__':
    n = int(raw_input())
    if n<1 or n>100:
        print 'Invalid Input'
    elif n%2!=0:
        print 'Weird'
    elif n in range(2,6):
        print 'Not Weird'
    elif n in range(6,21):
        print 'Weird'
    else:
        print 'Not Weird'