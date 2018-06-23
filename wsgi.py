import sys
sys.path.append('../')

from app.website import app
from common import config


if __name__ == '__main__':
    if config.DEBUG:
        website.app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        website.app.run()
