# Quando importamos diretamente de alguma pasta e não identificamos a fonte, o import vem do __init__ da pasta:
# Já para importar de outros arquivos, colocamos o nome da pasta.nome_do_arquivo:
from WeconBiochem import app

if __name__ == '__main__':
    app.run(debug=True)
