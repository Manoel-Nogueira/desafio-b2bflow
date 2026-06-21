import services.supabase_service as supabase_service
import services.message_service as message_service

# Seleciona os usuários do banco de dados
users = supabase_service.select_users()

for user in users:

    # Cria a mensagem de apresentação para cada usuário
    message = message_service.presentation_message(user)
    
    print(message)
