import sys
import logging
from my_uv_template.processor import Processor

logger = logging.getLogger(__name__)

def main() -> None:
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    processor = Processor(sys.argv[1], sys.argv[2])
    print(processor.run())
    logger.info('Finished')
