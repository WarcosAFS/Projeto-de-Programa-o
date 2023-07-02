a = True
print("="*len("  Dicionario  "))
print("  Dicionario  ")
print("="*len("  Dicionario  "))

word_english = ["yes","water"]
word_portuguese = ["sim","agua"]

while a:
    word = input("Qual palavra em ingles voce quer saber: ")
    
    if word == "ta bom por hoje":
        a = not a
    
    elif word in word_portuguese:
        z = word_portuguese.index(word)
        print(f'"{word}" se diz "{word_english[z]}"\n')
    else:
        word_portuguese.append(word)
        new_word = input("Me diga o significado disso em ingles e eu nunca mais vou esquecer: ")
        word_english.append(new_word)

print("Obrigado por ter me consultado\nAte a proxima")