#I know it looks horrible but it works

A = 0b1101
B = 0b1010
C = A & B
print(bin(C))
D = A | B
print(bin(D))
E = ~A
print(bin(E))
print(A)
print(~A)
F = A ^ B
print(bin(F))
not_A = A ^ 0b1111
G = A << 1
H = A >> 2
I = A << 2
print(bin(G))
print(bin(H))
print(bin(I))
