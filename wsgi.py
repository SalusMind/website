import sys
sys.path.append('../')

from app import app
from common import config

if __name__ == '__main__':
    if config.DEBUG:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run()
