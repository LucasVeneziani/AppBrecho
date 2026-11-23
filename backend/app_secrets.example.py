"""Modelo do arquivo de segredos. Copie para app_secrets.py e preencha (o run.py faz isso sozinho).

O app_secrets.py está no .gitignore, então a chave nunca vai para o GitHub.
Não chame o arquivo de secrets.py: isso esconderia o módulo `secrets` do Python, usado pelo FastAPI.
"""

# Crie uma chave em https://openrouter.ai/keys
OPENROUTER_API_KEY = ""

# Qualquer modelo da OpenRouter que aceite imagem funciona. 
OPENROUTER_MODEL = "google/gemma-4-31b-it:free"

# True para pular a OpenRouter e a busca e devolver um resultado de exemplo (para testar a interface).
DEMO_MODE = False
