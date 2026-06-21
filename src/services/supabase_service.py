import os
from supabase import create_client, Client
from dotenv import load_dotenv
from utils.logger import logger

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

# Cria a conexão com o Supabase
supabase: Client = create_client(URL, KEY)

def select_users():

    logger.info("Selecionando usuários")

    try:

        # Seleciona o "name" e o "number" de todos os usuários da tabela "users"
        response = supabase.table("users").select("name, number").execute()
        logger.info("Usuários selecionados com sucesso")

        return response.data

    except Exception as e:

        logger.error("Ocorreu um erro ao selecionar os usuários: %s", e)
        return []