def biggest():
    if(a>=b):
        if(a>c):
            biggest=a
        else:
            biggest=c
    else:
        if b>c:
            biggest=b
        else:
            biggest=c
            print("biggest num is:", biggest)


a=int(input())
b=int(input())
c=int(input())
biggest();