import os
txt = ""
styleSheet = "<link rel=\"stylesheet\" href=\"styles.css\" />\n"
tarefa = 0


def escrever_arquivo(path, str, type='w'):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, type) as file:
            file.write(str)
        print(f" atualizado o arquivo : {path}")
    except Exception:
        print(f"@ERRO ao escrever o arquivo: {Exception}")


def ler_arquivo(path):
    try:
        f = open(path, "r")
        return "" + f.read()
    except:
        print(f"@ERRO ao ler o arquivo: {path}")
        return ""

def initTarefa(str):
    global txt, tarefa
    tarefa = int(str)
    txt = "<p> "

def endTarefa():
    global txt, tarefa, styleSheet
    if tarefa == 0 :
        return
    txt += " </p>"
    txt = styleSheet + ler_arquivo(f'./exercicio{tarefa}.html') + txt
    escrever_arquivo(f'./exercicio{tarefa}.html', txt)


def main():
    global txt, tarefa
    a = ler_arquivo('./settup/enunciado.txt')
    for line in a.split('\n'):
        if 'Tarefa' in line :
            endTarefa()
            initTarefa(line[6:9].strip())
        else:
            txt += line + '\n'
    endTarefa()

if __name__ == '__main__':
  main()