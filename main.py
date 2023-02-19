import logging
from config.api import app, apm
from api.Resources import users
from elasticapm.handlers.logging import LoggingHandler


if __name__ == '__main__':
    handler = LoggingHandler(client=apm.client)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=8000)