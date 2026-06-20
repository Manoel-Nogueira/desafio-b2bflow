import services.supabase_service as supabase_service

users = supabase_service.select_users()

print(users)