
import logging.config

logging.basicConfig(format='%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG, force=True)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

logger = logging.getLogger()
