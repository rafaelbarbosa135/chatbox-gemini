import tkinter as tk
from tkinter import scrolledtext
from google import genai
import threading

chave_api = "AIzaSyCIUzlEZfGEdvVv2X0WhI_zFE00xBPlNxs"
cliente = genai.Client(api_key=chave_api)
chat_sessao = cliente.chats.create(model="gemini-2.0-flash-lite")

def enviar_mensagem():
    texto = entrada.get()
    if not texto.strip():
        return

    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"Você: {texto}\n\n")
    chat.insert(tk.END, "Gemini: digitando...\n\n")
    chat.config(state=tk.DISABLED)
    entrada.delete(0, tk.END)
    botao.config(state=tk.DISABLED)

    def chamar_api():
        try:
            resposta = chat_sessao.send_message(texto)
            texto_resposta = resposta.text
        except Exception as e:
            texto_resposta = f"Erro: {str(e)}"

        chat.config(state=tk.NORMAL)
        chat.delete("end-3l", "end-1c")
        chat.insert(tk.END, f"{texto_resposta}\n\n")
        chat.config(state=tk.DISABLED)
        chat.see(tk.END)
        botao.config(state=tk.NORMAL)

    threading.Thread(target=chamar_api, daemon=True).start()

janela = tk.Tk()
janela.title("Meu chatbox")
janela.geometry("600x500")

chat = scrolledtext.ScrolledText(janela, state=tk.DISABLED, wrap=tk.WORD,
                                  font=("Arial", 12), padx=10, pady=10)
chat.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

frame = tk.Frame(janela)
frame.pack(fill=tk.X, padx=10, pady=(0, 10))

entrada = tk.Entry(frame, font=("Arial", 12))
entrada.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)
entrada.bind("<Return>", lambda e: enviar_mensagem())

botao = tk.Button(frame, text="Enviar", command=enviar_mensagem,
                  font=("Arial", 12), padx=12)
botao.pack(side=tk.LEFT, padx=(8, 0))

janela.mainloop()

