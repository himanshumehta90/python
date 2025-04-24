#recursion: when a function calls itself repeatedly:
#  it is same as loops:

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)