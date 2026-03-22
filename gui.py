import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_utils import criptografar_arquivo, descriptografar_arquivo


class AppCriptografia:
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramenta de Criptografia de Arquivos")

        self.arquivo = ""

        # Botão selecionar arquivo
        self.btn_arquivo = tk.Button(root, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.btn_arquivo.pack(pady=5)

        # Label arquivo selecionado
        self.lbl_arquivo = tk.Label(root, text="Nenhum arquivo selecionado")
        self.lbl_arquivo.pack(pady=5)

        # Campo senha
        self.lbl_senha = tk.Label(root, text="Senha:")
        self.lbl_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack(pady=5)

        # Botões
        self.btn_criptografar = tk.Button(root, text="Criptografar", command=self.criptografar)
        self.btn_criptografar.pack(pady=5)

        self.btn_descriptografar = tk.Button(root, text="Descriptografar", command=self.descriptografar)
        self.btn_descriptografar.pack(pady=5)

    def selecionar_arquivo(self):
        self.arquivo = filedialog.askopenfilename()
        if self.arquivo:
            self.lbl_arquivo.config(text=self.arquivo)

    def criptografar(self):
        if not self.validar():
            return
        try:
            criptografar_arquivo(self.arquivo, self.entry_senha.get())
            messagebox.showinfo("Sucesso", "Arquivo criptografado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def descriptografar(self):
        if not self.validar():
            return
        try:
            descriptografar_arquivo(self.arquivo, self.entry_senha.get())
            messagebox.showinfo("Sucesso", "Arquivo descriptografado com sucesso!")
        except Exception:
            messagebox.showerror("Erro", "Senha incorreta ou arquivo inválido.")

    def validar(self):
        if not self.arquivo:
            messagebox.showwarning("Aviso", "Selecione um arquivo.")
            return False
        if not self.entry_senha.get():
            messagebox.showwarning("Aviso", "Informe uma senha.")
            return False
        return True