"""UserSrv
Usage:
	UserSrv.py --port=<int>
Options:
	-h --help     Show this screen.
	--port=<int>  port used
"""

# To run the server
# flask --app user_server run --port=8888

import logging
from docopt import docopt
from flask import Flask, Response

APP = Flask(__name__)

@APP.route('/isalive', methods=['GET'])
def is_alive():
	return Response(status=200)

if __name__ == '__main__':
	ARGS = docopt(__doc__)
	if ARGS['--port']:
		APP.run(host='localhost', port=ARGS['--port'])
	else:
		logging.error("Wrong command line arguments")