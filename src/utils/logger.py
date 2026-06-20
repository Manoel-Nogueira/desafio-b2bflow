import logging

# Cria um logger
logger = logging.getLogger(__name__)

if not logger.hasHandlers():

    # Configura o logger
    logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")