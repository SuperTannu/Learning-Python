
"""
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d/%m/%y %H:%M:%S")
import Modules
import logging.config

logging.config.fileConfig("logging.ini")
logging.getLogger("simpleExample")

logger= logging.getLogger(__name__)

streamh=logging.StreamHandler()
fileh=logging.FileHandler('file.log')

streamh.setLevel(logging.WARNING)
fileh.setLevel(logging.ERROR)

formatter=logging.Formatter("%(name)s - %(levelname)s - %(message)s")
streamh.setFormatter(formatter)
fileh.setFormatter(formatter)

logger.addHandler(streamh)
logger.addHandler(fileh)

logger.warning('this is a warning')
logger.error('this is an error')

try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:
    logging.error(e,exc_info=True)


from logging.handlers import RotatingFileHandler

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler=RotatingFileHandler('app.log', maxBytes=2000, backupCount=3)
logger.addHandler(handler)

for i in range(10):
    logger.info('Hello, Worlds!')
"""

