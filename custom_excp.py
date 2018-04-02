class Custom_excp(Exception):
    def __init__(self,err):
        self.err = err

def square(var):
    try:
           if var <= 0:
               raise Custom_excp("Not a natural number")
           else:
                return var*var
    except Custom_excp as e:
           print (e.err)
    return '********************'

if __name__ == '__main__':
    print("Enter a natural number:")
    var=int(input())
    print(square(var))
