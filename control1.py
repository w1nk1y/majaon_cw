def decorator(func):
    def wrapper(Vn,a,t):
        print(func(Vn,Vk,t))
        r=Vn*t+a*t**2/2
        print(r)
    return wrapper

@decorator
def func(Vn,Vk,t):
    a=(Vk-Vn)/t
    return a

Vn=int(input())
Vk=int(input())
t=int(input())


func(Vn,Vk,t)



