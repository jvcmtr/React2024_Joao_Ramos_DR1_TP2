import os
txt = ""
template = """
<link rel="stylesheet" href="styles.css" />

<div class="nav-container">
  <h1>@TITLE</h1>
  <nav>
    <ul class="nav-list">
      <li><a href="exercicio1.html">Exercício 1</a></li>
      <li><a href="exercicio2.html">Exercício 2</a></li>
      <li><a href="exercicio3.html">Exercício 3</a></li>
      <li><a href="exercicio4.html">Exercício 4</a></li>
      <li><a href="exercicio5.html">Exercício 5</a></li>
      <li><a href="exercicio6.html">Exercício 6</a></li>
      <li><a href="exercicio7.html">Exercício 7</a></li>
      <li><a href="exercicio8.html">Exercício 8</a></li>
      <li><a href="exercicio9.html">Exercício 9</a></li>
      <li><a href="exercicio10.html">Exercício 10</a></li>
      <li><a href="exercicio11.html">Exercício 11</a></li>
      <li><a href="exercicio12.html">Exercício 12</a></li>
      <li><a href="exercicio13.html">Exercício 13</a></li>
      <li><a href="exercicio14.html">Exercício 14</a></li>
      <li><a href="exercicio15.html">Exercício 15</a></li>
      <li><a href="exercicio16.html">Exercício 16</a></li>
    </ul>
  </nav>
</div>
<p>
"""

tarefa = 0


def escrever_arquivo(path, str, type='w'):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, type, encoding='utf8') as file:
            file.write(str)
        print(f" atualizado o arquivo : {path}")
    except Exception:
        print(f"@ERRO ao escrever o arquivo: {Exception}")


def ler_arquivo(path):
    try:
        f = open(path, "r",  encoding="utf8")
        return "" + f.read()
    except:
        print(f"@ERRO ao ler o arquivo: {path}")
        return ""

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