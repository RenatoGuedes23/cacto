import logging.config
from config.logger.format_logger import logging_config

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())