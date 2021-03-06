# -*- coding: utf-8 -*-

"""A module which allows the Flask Application to
be as a local development server.

We create new a Flask application when using the 'Procfile' method of
launching the application.

See Procfile in the root folder for more.

:achut's Windriver Assessment Solution.
"""

import logging
import api

from .version import __version__ as version

logger = logging.getLogger(__name__)

#
# Create the RESTful Flask Application instance.
#
app = api.create_app()
logger.info('Welcome to API Version {}...'.format(version))
