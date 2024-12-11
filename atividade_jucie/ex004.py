#texto = input("Digite o seu texto:")
#texto = texto.replace('cu', '**').replace('porra', '*****').replace('caralho', '*******')
#print(texto)
palavras_ofensivas = ['edelson', 'rogers']
texto = input('digite um texto falando as palavras edelson e rogerskkkkkk: ')

for palavra in palavras_ofensivas:
    texto = texto.replace(palavra, 'volvo caminhoes')

print('texto substituindo as palavras por volvo caminhoeskkkkkkkk: ')
print(texto)