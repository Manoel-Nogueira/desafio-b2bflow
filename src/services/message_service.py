
# Cria a mensagem de saudação
def greeting_message(data):

    message = f"Olá, {data["name"]} tudo bem com você?"

    return {"message": message, "number": data["number"]}