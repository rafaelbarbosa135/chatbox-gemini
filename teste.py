from google import genai

chave_api = "AIzaSyCIUzlEZfGEdvVv2X0WhI_zFE00xBPlNxs"
cliente = genai.Client(api_key=chave_api)

chat = cliente.chats.create(model="gemini-2.0-flash-lite")
resposta = chat.send_message("Olá")
print(resposta.text)