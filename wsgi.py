from api.app import create_app
import os
from api.utility.utils import load_env

load_env()
environment = os.getenv('BARD_ENV', 'dev')
application = create_app(environment)

if __name__ == '__main__':
    host = application.config['FLASK_RUN_HOST']
    port = application.config['FLASK_RUN_PORT']
    debugging = application.config['DEBUG']
    application.run(host=host, port=port, debug=debugging)