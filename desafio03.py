# a) 1, 3, 5, 7, 9 (Sequência de números ímpares)
# Resposta: 9
a = [1, 3, 5, 7]
a.append(a[-1] + 2)
print(a)

# b) 2, 4, 8, 16, 32, 64, 128 (Dobra o valor do número anterior)
# Resposta: 128
b = [2, 4, 8, 16, 32, 64]
b.append(b[-1] * 2)
print(b)

# c) 0, 1, 4, 9, 16, 25, 36, 49 (Sequência de quadrados perfeitos)
# Resposta: 49
c = [0, 1, 4, 9, 16, 25, 36]
c.append(c[-1] + 13)
print(c)

# d) 4, 16, 36, 64, 100 (Sequência de quadrados perfeitos pares)
# Resposta: 100
d = [4, 16, 36, 64]
d.append(d[-1] + 36)
print(d)

# e) 1, 1, 2, 3, 5, 8, 13 (Sequência de Fibonacci)
# Resposta: 13
e = [1, 1, 2, 3, 5, 8]
e.append(e[-1] + 5)
print(e)


# f) Resposta: 20
# 2, 10, 12, 16, 17, 18, 19, 20 (Sequência crescente com incremento )
f = [2, 10, 12, 16, 17, 18, 19]
f.append(f[-1] + 1)
print(f)
