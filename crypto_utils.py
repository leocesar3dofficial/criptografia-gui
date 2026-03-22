from cryptography.fernet import Fernet
import base64
import hashlib

def gerar_chave(senha: str) -> bytes:
    """
    Gera uma chave a partir da senha do usuário
    """
    hash_senha = hashlib.sha256(senha.encode()).digest()
    chave = base64.urlsafe_b64encode(hash_senha)
    return chave


def criptografar_arquivo(caminho_arquivo: str, senha: str):
    chave = gerar_chave(senha)
    fernet = Fernet(chave)

    with open(caminho_arquivo, 'rb') as arquivo:
        dados = arquivo.read()

    dados_criptografados = fernet.encrypt(dados)

    novo_arquivo = caminho_arquivo + ".enc"
    with open(novo_arquivo, 'wb') as arquivo:
        arquivo.write(dados_criptografados)


def descriptografar_arquivo(caminho_arquivo: str, senha: str):
    chave = gerar_chave(senha)
    fernet = Fernet(chave)

    with open(caminho_arquivo, 'rb') as arquivo:
        dados = arquivo.read()

    dados_descriptografados = fernet.decrypt(dados)

    novo_arquivo = caminho_arquivo.replace(".enc", "")
    with open(novo_arquivo, 'wb') as arquivo:
        arquivo.write(dados_descriptografados)