import logging

import xmlschema

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def validate(schemafile, datafile):
    # Crate XML Schema object
    schema = xmlschema.XMLSchema(schemafile)
    # Validate an XML file against the schema
    a = schema.is_valid(datafile)
    logger.info(a)
    try:
        schema.validate(datafile)
    except xmlschema.XMLSchemaValidationError as err:
        logger.error("Error in %s %s", err.path, err.reason)
