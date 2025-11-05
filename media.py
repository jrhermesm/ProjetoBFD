aluno=input('Digite o nome do aluno: ')
nota1=float(input(f'Digite a primeira nota do aluno {aluno}: '))
nota2=float(input(f'Digite a primeira nota do aluno {aluno}: '))
media=(nota1+nota2)/2
situacao='A'
if media>=7:
    situacao='Aprovado'
elif media >=4:
    situacao="em Recuperação"
else:
    situacao='Reprovado' 

print(f'a média do {aluno} é {media:.2f} e o seu status é de {situacao}')
