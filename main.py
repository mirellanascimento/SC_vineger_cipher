alfabeto = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
                'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
                'w': 22, 'x': 23, 'y': 24, 'z': 25}

freq_port = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]
freq_eng = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]


def key_length():
    pass

def decipher(text, key):
    decipher_text = ""
    i = 0
    for value in text:
        value = value.lower()
        if value in alfabeto:
            if i == len(key):
                i = 0
            c = alfabeto[value]
            k = alfabeto[key[i]]

            d = (c - k) % 26
            dt = list(alfabeto)[list(alfabeto.values()).index(d)]

            decipher_text+= dt
            i+=1
        else:
            decipher_text+=value

    return decipher_text  


def cipher(text, key):  
    cipher_text = ""
    i = 0
    for value in text:
        value = value.lower()
        if value in alfabeto:
            if i == len(key):
                i = 0
            t = alfabeto[value]
            k = alfabeto[key[i]]

            c = (t + k) % 26
            ct = list(alfabeto)[list(alfabeto.values()).index(c)]

            cipher_text+= ct
            i+=1
        else:
            cipher_text+=value

    return cipher_text


def read_file():

    filename = input("Insira o nome do arquivo: ")

    with open(f"{filename}.txt", encoding='utf-8') as file:
        text = file.read()

    return text

def main():
    
    while True:

        print("\nMENU:")
        print("1 - Cifrar")
        print("2 - Decifrar")
        print("3 - Ataque de recuperacao de senha")
        print("4 - Sair")
        
        entrada = int(input("Escolha uma das opçoes: "))

        if entrada == 1:
            text = read_file()
            key = input("Insira a senha: ").lower()
            criptograma = cipher(text, key)
            print(f"\nMensagem criptografada: \n{criptograma}")
        elif entrada == 2:
            text = read_file()
            key = input("Insira a senha: ").lower()
            mensagem = decipher(text, key)
            print(f"\nMensagem descriptografada: \n{mensagem}")
            continue
        elif entrada == 3:
            continue
        elif entrada == 4:
            print("\nPrograma encerrado!!")
            break
        else:
            print("Entrada invalida!")

if __name__ == '__main__':
    main()