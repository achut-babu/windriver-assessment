# -*- coding: utf-8 -*-
"""Encrypt Decrypt Module Endpoints.

:achut's Windriver Assessment Solution.
"""

from flask_restful import Resource, request
from flask import current_app

class HealthCheckAPI(Resource):
    """A class housing http service that returns the health status of the App.
    """
    def get(self):
        """The implementation of the health check HTTP GET method which is serviced by the
        encrypt decrypt module.
        """
        return current_app.services.encrypt_decrypt_module_service.get_health_check()

class EncryptAPI(Resource):
    """A class housing http service that returns the encrytped string.
    """
    def post(self):
        """The implementation of the encrypt HTTP POST method which is serviced by the
        encrypt decrypt module.
        """
        return current_app.services.encrypt_decrypt_module_service.encrypt(request)

class DecryptAPI(Resource):
    """A class housing http service that returns the decrypted string.
    """
    def post(self):
        """The implementation of the decrypt HTTP POST method which is serviced by the
        encrypt decrypt module.
        """
        return current_app.services.encrypt_decrypt_module_service.decrypt(request)
