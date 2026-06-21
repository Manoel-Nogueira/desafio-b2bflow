
# Cria a mensagem de apresentação
def presentation_message(data):

    message = f"Olá, {data["name"]} tudo bem com você?"

    return {"message": message, "number": data["number"]}