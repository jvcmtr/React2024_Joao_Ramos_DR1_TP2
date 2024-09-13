from utils import ler_arquivo, escrever_arquivo

txt = ""
template = """
<link rel="stylesheet" href="styles.css" />

<div class="nav-container">
  <h1>@TITLE</h1>
  <nav>
    <ul class="nav-list">
        <li><a href="./ex1/exercicio1.html">Exercício 1</a></li>
        <li><a href="./ex2/exercicio2.html">Exercício 2</a></li>
        <li><a href="./ex3/exercicio3.html">Exercício 3</a></li>
        <li><a href="./ex4/exercicio4.html">Exercício 4</a></li>
        <li><a href="./ex5/exercicio5.html">Exercício 5</a></li>
        <li><a href="./ex6/exercicio6.html">Exercício 6</a></li>
        <li><a href="./ex7/exercicio7.html">Exercício 7</a></li>
        <li><a href="./ex8/exercicio8.html">Exercício 8</a></li>
        <li><a href="./ex9/exercicio9.html">Exercício 9</a></li>
        <li><a href="./ex10/exercicio10.html">Exercício 10</a></li>
        <li><a href="./ex11/exercicio11.html">Exercício 11</a></li>
        <li><a href="./ex12/exercicio12.html">Exercício 12</a></li>
        <li><a href="./ex13/exercicio13.html">Exercício 13</a></li>
        <li><a href="./ex14/exercicio14.html">Exercício 14</a></li>
        <li><a href="./ex15/exercicio15.html">Exercício 15</a></li>
        <li><a href="./ex16/exercicio16.html">Exercício 16</a></li>
    </ul>
  </nav>
</div>
<p>
"""

tarefa = 0

def initTarefa(str, title):
    global txt, tarefa
    tarefa = int(str)
    txt = template.replace("@TITLE", title)

def endTarefa():
    global txt, tarefa, styleSheet
    if tarefa == 0 :
        return
    txt += " </p>"
    escrever_arquivo(f'./template/exercicio{tarefa}.html', txt)


def main():
    global txt, tarefa
    a = ler_arquivo('./settup/enunciado.txt')
    for line in a.split('\n'):
        if 'Tarefa' in line :
            endTarefa()
            initTarefa(line[6:9].strip(), line)
        else:
            txt += line + '\n'
    endTarefa()

if __name__ == '__main__':
  main()