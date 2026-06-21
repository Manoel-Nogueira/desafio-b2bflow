import configs.load_env as env
from supabase import create_client, Client
from utils.logger import logger

# Cria a conexão com o Supabase
supabase: Client = create_client(env.SUPABASE_URL, env.SUPABASE_KEY)

def select_users():

    logger.info("Selecionando usuários")

    try:

        # Seleciona o "name" e o "number" de todos os usuários da tabela "users"
        response = supabase.table("users").select("name, number").execute()
        logger.info("Usuários selecionados com sucesso")

        return response.data

    except Exception as e:

        logger.error(f"Ocorreu um erro ao selecionar os usuários: \n{e}")
        return e