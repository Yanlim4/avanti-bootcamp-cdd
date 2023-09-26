def primo(numero):
    primo = 0

    for i in range(1, (numero + 1)):        
        if numero % i == 0:
            primo += 1
        
    if primo == 2 :
        print(f"O {numero} é primo")
    else:
        print(f"O {numero} não é primo")