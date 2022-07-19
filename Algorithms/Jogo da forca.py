#Feito em uma brincadeira e como forma de testes, para ser otimizado posteriormente em C++

#Import de biblioteca(s)

from random import choice

#Variáveis e arrays

arr = ["computador", "programar", "jogos", "software", "desenvolvimento",
"teste", "estrutura", "linguagem", "ferramenta", "dados", "internet", "rede"
"portas", "servidores", "hardware", "algoritmos", "robo", "dinamismo", "framework",
"debug", "classes", "objetos", "bytes", "aplicativo", "sistemas"]
rsp = ["-" for i in range(15)]
used = []
wrd = choice(arr)
count = 6

#Código(Jogo)

print("Olá, bem vindo ao jogo da forca!\nA palavra já foi gerada, o jogo começou!")
while count > 0:
    st = input("\nDigite a sua letra ou palavra: ").lower()
    if st in wrd and st not in used:
        print("Boa, acertou!\nA palavra está assim:")
        if len(st) > 1 and wrd != st:
                for i in range(len(st)):
                    for j in range(len(wrd)):
                        if wrd[j] == st[i]:
                            rsp[j] = st[i]
                if "".join(rsp)[0:len(wrd)] == wrd:
                    break 
        elif wrd == st:
            for i in range(len(wrd)):
                print(wrd[i], end = " ")
            print("\n")
            break
        else:
            for i in range(len(wrd)):
                if wrd[i] == st:
                    rsp[i] = st
            if "".join(rsp)[0:len(wrd)] == wrd:
                break
        for i in range(len(wrd)):
            print(f"{rsp[i]}", end = " ")
        used.append(st)
    elif st in wrd and st in used:
        print("Você já tentou essa letra/palavra!\nNão pode tenta-la novamente...")
    else:
        count -= 1
        print(f"Não foi dessa vez...\nEssa letra/palavra não existe na palavra a ser descoberta!\nTentativas restantes: {count}")

if count == 0:
    print("Infelizmente você não acertou a palavra nas 6 tentativas\nBoa sorte na próxima! :)")
    print(f"A palavra era: {wrd}")

else:
    print("Parabéns, você venceu o jogo! Espero te ver novamente jogando! :)")
    print(f"A palavra era: {wrd}")
