import sys
import logging

DEBUG_FORMAT = ("[%(asctime)s] %(levelname)s %(name)s:%(lineno)d"
                "(%(funcName)s): %(message)s")
INFO_FORMAT = ("[%(asctime)s] %(message)s")
COLOR_FORMAT = ("[%(asctime)s] \033[%(color)sm%(message)s\033[39m")

ISO_8601 = "%Y-%m-%dT%H:%M:%S"


def setup_logging(verbosity):
    log_level = logging.INFO
    log_format = INFO_FORMAT
    if sys.stdout.isatty():
        log_format = COLOR_FORMAT

    if verbosity > 0:
        log_level = logging.DEBUG
        log_format = DEBUG_FORMAT
    if verbosity < 2:
        logging.getLogger("botocore").setLevel(logging.CRITICAL)

    hdlr = logging.StreamHandler()
    hdlr.setFormatter(Formatter(log_format, ISO_8601))
    logging.root.addHandler(hdlr)
    logging.root.setLevel(log_level)


class Formatter(logging.Formatter):
    def format(self, record):
        if 'color' not in record.__dict__:
            record.__dict__['color'] = 37
        msg = super(Formatter, self).format(record)
        return msg
