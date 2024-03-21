def gcd_recursive(m,n): #Tinh uoc chung lon nhat cua m va n bang de qui
    if n== 0:
        return m
    else:
        return gcd_recursive(n,m%n)

def gcd_iteratve(m,n): #Tinh uoc chung lon nhat cua m va n bang vong lap
    while n != 0:
        m,n = n,m %n
    return m

#Nhap hai so nguyen m va n
m = int(input("Nhap so nguyen duong m: "))
n = int(input("Nhap so nguyen duong n: "))
#Tinh uoc chug lon nhat bang de qui
gcd_recursive_result = gcd_recursive(m,n)
print(f"Uoc chung lon nhat cua {m} va {n} (de quy): {gcd_recursive_result}")
#Tinh uoc chung ln nhat bang vong lap
gcd_iteratve_result = gcd_iteratve(m,n)
print(f"Uoc chung lon nhat cua {m} va {n} (vong lap): {gcd_iteratve_result}")


    