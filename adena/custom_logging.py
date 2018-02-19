import logging

class MyLogger(logging.Logger):

    def __init__(self, name, is_debug=True):
        self.is_debug = is_debug
        super(MyLogger, self).__init__(name)

    def debug(self, msg, *args, **kwargs):
        print("inside")
        if self.is_debug:
            return super(MyLogger, self).debug(msg, *args, **kwargs)
        else:
            pass

logging.setLoggerClass(MyLogger)
logging.basicConfig()


'''testing below'''

logger = logging.getLogger(__name__)
logger.debug('1st warning')
logger.debug('2nd warning')
print("test complete")