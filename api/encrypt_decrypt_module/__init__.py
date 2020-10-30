# -*- coding: utf-8 -*-
"""Encrypt Decrypt Module.

:achut's Windriver Assessment Solution.
"""

import flask
import six
from flask_restful import Api

from .resources import encrypt_decrypt_module_api
from .services import EncryptDecryptModuleService

ROUTES = {
    '/health': encrypt_decrypt_module_api.HealthCheckAPI,
    '/encrypt': encrypt_decrypt_module_api.EncryptAPI,
    '/decrypt': encrypt_decrypt_module_api.DecryptAPI
}

def init(app):
    """The entry point for the module. This called as part of the overall
    Flask application Initialization.

    :param:`app` - The instance of the current Flask App.
    """
    blueprint = flask.Blueprint('encrypt_decrypt_module', __name__,
                                url_prefix='/api')
    api = Api(blueprint)

    for pattern, endpoint in six.iteritems(ROUTES):
        api.add_resource(endpoint, pattern)

    app.register_blueprint(blueprint)
    app.services.register_service('encrypt_decrypt_module_service',
                                  EncryptDecryptModuleService())
