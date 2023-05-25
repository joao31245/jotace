nota = float(input('Qual a nota do aluno no primeiro bimestre?: '))
nota1 = float(input('Qual a nota do aluno no segundo bimestre?: '))
nota2 = float(input('Qual a nota do aluno no terceiro bimestre?: '))
nota3 = float(input('Qual a nota do aluno no quarto bimestre?: '))
media = (nota + nota1 + nota2 + nota3) / 4
print('A média do aluno foi {:.2f}' .format(media))
if media < 15:
    print('Caralho tu e mt burro')
else:
    print('Se esforçando pra aprender coisa inultio?')
