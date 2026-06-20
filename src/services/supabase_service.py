import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carregando variáveis de ambiente do arquivo .env
load_dotenv()
URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

# Criando conexão com o Supabase
supabase: Client = create_client(URL, KEY)

def select_users():

    try:

        # Selecionando todos os usuários da tabela "users"
        response = supabase.table("users").select("*").execute()
        return response.data

    except Exception as e:

        return e