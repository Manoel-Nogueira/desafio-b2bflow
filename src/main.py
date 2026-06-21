import configs.load_env as load_env
import services.supabase_service as supabase_service
import services.message_service as message_service
import services.zapi_service as zapi_service
from utils.logger import logger

logger.info("Iniciando o envio de mensagens")

# Seleciona os usuários do banco de dados
users = supabase_service.select_users()

for user in users:

    # Cria a mensagem de saudação para cada usuário
    message = message_service.greeting_message(user)

    # Envia a mensagem para o usuário via Z-API
    send_message = zapi_service.send_message(message)

logger.info("Envio de mensagens finalizado")