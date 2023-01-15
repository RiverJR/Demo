import logging

import fire

from demo import data, schema

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def ping():
    print("pong")


def validate(schemafile, datafile):
    schema.validate(schemafile, datafile)


def to_xml(csvfile):
    data.to_xml(csvfile)


def cli():
    """Command line interface intended to be used as the entrypoint."""
    # Set root logger to warning to avoid noise from third party libraries
    logging.basicConfig(level=logging.WARNING)

    # Make Python Fire not use a pager when it prints a help text
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(
        {
            "ping": ping,
            "validate": validate,
            "xml": to_xml,
        },
    )
