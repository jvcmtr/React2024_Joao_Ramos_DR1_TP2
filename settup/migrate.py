from utils import ler_arquivo, escrever_arquivo

LEITURA = './exercicio@.'
ESCRITA = './ex@/exercicio@.'

def leitura(i):
    i = str(i)
    return LEITURA.replace("@", i)

def escrita(i):
    i = str(i)
    return ESCRITA.replace("@", i)

for i in range(10, 17):
    txt = ler_arquivo( leitura(i)+'html')
    escrever_arquivo( escrita(i)+'html' , txt)
    txt = ''
    txt = ler_arquivo( leitura(i)+'css' )
    if txt != "" :
        escrever_arquivo( escrita(i)+'css' , txt)

print('\n\n')
for i in range(1, 17):
    print(f'<li><a href="./ex{i}/exercicio{i}.html">Exercício {i}</a></li>')