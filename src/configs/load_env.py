import os
from utils.logger import logger
from dotenv import load_dotenv

logger.info("Carregando variáveis de ambiente do arquivo .env")

try:

    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()
    
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
    
    logger.info("Variáveis de ambiente do arquivo .env carregadas com sucesso")

except Exception as e:

    logger.error("Ocorreu um erro ao carregar as variáveis de ambiente do arquivo .env: %s", e)
