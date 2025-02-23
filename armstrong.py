#this is also efficient

def checkArmstrong(n):
    #write your code here !!!!!!!!!
    sumo = 0
    num = n
    length = 0
    while (n>0):
        length += 1
        n //= 10

    n = num
    while (n>0):
        sumo += ((n%10)**length)
        n = n//10
    return sumo==num