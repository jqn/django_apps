import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./tmp/jqnapp.log',
                    # filemode='w',
                    )

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists', exc_info=True)

# Example with full stack trace
# while True:
#     try:
#         main_loop()
#     except Exception:
#         logger.error("Fatal error in main loop", exc_info=True)
