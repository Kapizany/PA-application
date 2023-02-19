from config.api import app, apm
from api.Resources import users
from elasticapm.handlers.logging import LoggingHandler


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)