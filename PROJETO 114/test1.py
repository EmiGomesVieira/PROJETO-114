a = 33
b = "33"

# Comparar uma string com um inteiro não é possível diretamente. Precisamos converter 'b' para um inteiro.
b_int = int(b)

if b_int > a:
    print("b é maior que a")
elif b_int == a:
    print("a e b são iguais")
