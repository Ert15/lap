
def m(n):
    r = 1
    for x in n :
        r *= x
    return r

n = [2, 3, 4, 5]
result = m(n)
print(result)



def c(s):
    u = sum(1 for char in s if char.isupper())
    l = sum(1 for char in s if char.islower())
    return u, l


s = "Hello World"
u, l = c(s)
print(u)
print(l)





def i(s):
    r = s[::-1]
    return s == r

s = "ertre"
if i(s):
    print(f"{s} - это палиндром.")
else:
    print(f"{s} - не палиндром.")




def a(t):
    for x in t:
        if not x:
            return False
    return True


b = (True, True, True, False)
r = a(b)
print(r)










