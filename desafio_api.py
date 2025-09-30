# primeiro instale o pip install requests

import requests

# 1. Defina o URL do endpoint que você deseja consumir
# Substitua este URL pelo seu endpoint real
URL_DO_ENDPOINT = "https://web-production-d2cba.up.railway.app/hell" 

try:
    # Faz a requisição GET ao endpoint
    resposta = requests.get(URL_DO_ENDPOINT)

    # 2. Verifica se a requisição foi bem-sucedida (código de status 200)
    if resposta.status_code == 200:
        # 3. Assume que a mensagem "funcionou" é o texto puro da resposta
        # Se o endpoint retornar JSON (ex: {"status": "funcionou"}), você usaria:
        # dados_json = resposta.json()
        # mensagem = dados_json.get("status")

        mensagem = resposta.text
        
        print("--- SUCESSO ---")
        print(f"Status HTTP: {resposta.status_code}")
        print(f"Mensagem do Endpoint: {mensagem}")

        # Verifica se a mensagem é exatamente "funcionou"
        if "funcionou" in mensagem.lower():
            print("\nConfirmação: A mensagem 'funcionou' foi recebida!")
        
    else:
        # Trata erros de requisição (4xx ou 5xx)
        print("--- FALHA NA REQUISIÇÃO ---")
        print(f"Status HTTP: {resposta.status_code}")
        print(f"Detalhes: {resposta.text[:100]}...") # Mostra os primeiros 100 caracteres da resposta
        
except requests.exceptions.RequestException as e:
    # Trata erros de conexão (ex: servidor fora do ar, URL incorreto)
    print("--- ERRO DE CONEXÃO ---")
    print(f"Não foi possível conectar ao endpoint: {e}")
