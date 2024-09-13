from utils import ler_arquivo, escrever_arquivo

_PATH = './ex@/exercicio@.html'

def path(i):
    return _PATH.replace("@", str(i))

for i in range(1, 17):
    txt = ler_arquivo( path(i))
    txt = txt.replace('<a href="ex1/exercicio1.html">Exercício 1</a>', '<a href="../ex1/exercicio1.html">Exercício 1</a>')
    txt = txt.replace('<a href="ex2/exercicio2.html">Exercício 2</a>', '<a href="../ex2/exercicio2.html">Exercício 2</a>')
    txt = txt.replace('<a href="ex3/exercicio3.html">Exercício 3</a>', '<a href="../ex3/exercicio3.html">Exercício 3</a>')
    txt = txt.replace('<a href="ex4/exercicio4.html">Exercício 4</a>', '<a href="../ex4/exercicio4.html">Exercício 4</a>')
    txt = txt.replace('<a href="ex5/exercicio5.html">Exercício 5</a>', '<a href="../ex5/exercicio5.html">Exercício 5</a>')
    txt = txt.replace('<a href="ex6/exercicio6.html">Exercício 6</a>', '<a href="../ex6/exercicio6.html">Exercício 6</a>')
    txt = txt.replace('<a href="ex7/exercicio7.html">Exercício 7</a>', '<a href="../ex7/exercicio7.html">Exercício 7</a>')
    txt = txt.replace('<a href="ex8/exercicio8.html">Exercício 8</a>', '<a href="../ex8/exercicio8.html">Exercício 8</a>')
    txt = txt.replace('<a href="ex9/exercicio9.html">Exercício 9</a>', '<a href="../ex9/exercicio9.html">Exercício 9</a>')
    txt = txt.replace('<a href="ex10/exercicio10.html">Exercício 10</a>', '<a href="../ex10/exercicio10.html">Exercício 10</a>')
    txt = txt.replace('<a href="ex11/exercicio11.html">Exercício 11</a>', '<a href="../ex11/exercicio11.html">Exercício 11</a>')
    txt = txt.replace('<a href="ex12/exercicio12.html">Exercício 12</a>', '<a href="../ex12/exercicio12.html">Exercício 12</a>')
    txt = txt.replace('<a href="ex13/exercicio13.html">Exercício 13</a>', '<a href="../ex13/exercicio13.html">Exercício 13</a>')
    txt = txt.replace('<a href="ex14/exercicio14.html">Exercício 14</a>', '<a href="../ex14/exercicio14.html">Exercício 14</a>')
    txt = txt.replace('<a href="ex15/exercicio15.html">Exercício 15</a>', '<a href="../ex15/exercicio15.html">Exercício 15</a>')
    txt = txt.replace('<a href="ex16/exercicio16.html">Exercício 16</a>', '<a href="../ex16/exercicio16.html">Exercício 16</a>')
    escrever_arquivo(path(i), txt)














a = """
         <a href="ex1/exercicio1.html">Exercício 1</a>
        <a href="ex2/exercicio2.html">Exercício 2</a>
        <a href="ex3/exercicio3.html">Exercício 3</a>
        <a href="ex4/exercicio4.html">Exercício 4</a>
        <a href="ex5/exercicio5.html">Exercício 5</a>
        <a href="ex6/exercicio6.html">Exercício 6</a>
        <a href="ex7/exercicio7.html">Exercício 7</a>
        <a href="ex8/exercicio8.html">Exercício 8</a>
        <a href="ex9/exercicio9.html">Exercício 9</a>
        <a href="ex10/exercicio10.html">Exercício 10</a>
        <a href="ex11/exercicio11.html">Exercício 11</a>
        <a href="ex12/exercicio12.html">Exercício 12</a>
        <a href="ex13/exercicio13.html">Exercício 13</a>
        <a href="ex14/exercicio14.html">Exercício 14</a>
        <a href="ex15/exercicio15.html">Exercício 15</a>
        <a href="ex16/exercicio16.html">Exercício 16</a>""".split('\n')

b = """
        <a href="exercicio1.html">Exercício 1</a>
        <a href="exercicio2.html">Exercício 2</a>
        <a href="exercicio3.html">Exercício 3</a>
        <a href="exercicio4.html">Exercício 4</a>
        <a href="exercicio5.html">Exercício 5</a>
        <a href="exercicio6.html">Exercício 6</a>
        <a href="exercicio7.html">Exercício 7</a>
        <a href="exercicio8.html">Exercício 8</a>
        <a href="exercicio9.html">Exercício 9</a>
        <a href="exercicio10.html">Exercício 10</a>
        <a href="exercicio11.html">Exercício 11</a>
        <a href="exercicio12.html">Exercício 12</a>
        <a href="exercicio13.html">Exercício 13</a>
        <a href="exercicio14.html">Exercício 14</a>
        <a href="exercicio15.html">Exercício 15</a>
        <a href="exercicio16.html">Exercício 16</a>""".split('\n')
# for i in range(1,len(a)):
#     print(f'txt = txt.replace(\'{a[i].strip()}\', \'{a[i].strip().replace('href="ex', f'href="../ex')}\')')