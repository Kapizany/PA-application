from config.api import app
from api.Resources import users

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8000)