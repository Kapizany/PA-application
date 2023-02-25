from config.api import api
from werkzeug.exceptions import HTTPException
from config.logs import Logging
from config.cognito import cognito

logger = Logging(__name__)

@api.errorhandler(HTTPException)
def ahndle_http_exceptions(error):
    logger.error(f"HTTP Error: {error.description}")
    return {'message': error.description}, error.code

@api.errorhandler(Exception)
def handle_generic_exception(error):
    if hasattr(error, 'response') and error.response.get('Error') and error.response.get('Error').get('Code') in cognito.exceptions._code_to_exception:
        logger.error(f"{error.response['Error']['Code']} {error.response['Error']['Message']}")
        return {'message': f"{error.response['Error']['Code']}: {error.response['Error']['Message']}"}, error.response.get('ResponseMetadata').get('HTTPStatusCode')
    logger.error(f"Error: {error.args[0]}")
    return {'message': error.args[0]}, 500