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
try:
    Vn=int(input())
    Vk=int(input())
    t=int(input())
    func(Vn,Vk,t)
except TypeError:
    print("Вы ввели не числа")
except ZeroDivisionError:
    print("Время не может равняться нулю")




