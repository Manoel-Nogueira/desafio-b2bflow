import requests
import configs.load_env as env
from utils.logger import logger

def send_message(data):

    logger.info(f"Enviando mensagem para {data['number']}")

    try:

        # Monta a requisição da API do Z-API
        url = f"https://api.z-api.io/instances/{env.ZAPI_INSTANCE_ID}/token/{env.ZAPI_INSTANCE_TOKEN}/send-text"
        payload = {"phone": data["number"], "message": data["message"]}
        headers = {"Client-Token": f"{env.ZAPI_INSTANCE_TOKEN}", "Content-Type": "application/json"}

        # Envia a requisição POST para a API do Z-API
        response = requests.post(url, json = payload, headers = headers)

        logger.info(f"Mensagem enviada com sucesso para {data['number']}")
        return response.text
    
    except Exception as e:

        logger.error(f"Ocorreu um erro ao enviar a mensagem para {data['number']}: \n{e}")
        return e
