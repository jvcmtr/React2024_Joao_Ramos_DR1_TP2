import os

def escrever_arquivo(path, str, type='w'):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, type, encoding='utf8') as file:
            file.write(str)
        print(f" atualizado o arquivo : {path}")
    except :
        print(f"@ERRO ao escrever o arquivo: {Exception}")


def ler_arquivo(path):
    try:
        f = open(path, "r",  encoding="utf8")
        return "" + f.read()
    except:
        print(f"@ERRO ao ler o arquivo: {path}")
        return ""