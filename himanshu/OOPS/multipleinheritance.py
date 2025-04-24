class A:
    varA = "this is class a"

class B:
    varB="thi is class b"

class C(A,B): #this is multilevel inheritance that is inheriting both A and B
    varC="this is class C"
c1=C()

print(c1.varC)
print(c1.varA)