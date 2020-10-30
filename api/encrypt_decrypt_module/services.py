# -*- coding: utf-8 -*-
"""Encrypt Decrypt Module Services.

:achut's Windriver Assessment Solution.
"""

import logging

from .constants import ENCRYPT_DECRYPT_MODULE_NAME
import json
from .util import Util
from flask import make_response
import base64

util = Util()
class EncryptDecryptModuleService(object):
    """A collection of services implemented by the encrypt decrypt module which can be
    accessed via Flask current_app's service registry.
    """
    def __init__(self):
        """A basic Initialization for the class which just sets up the logger
        for further use within the class.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Initializing Services for module - %s"
                         %(ENCRYPT_DECRYPT_MODULE_NAME)
        )


    def get_health_check(self):
        """A helper service method which just sends back a simple string
        response to the caller.

        :return:`response` - A simple string response (health status) sent to the caller.
        """
        return util.create_response(output="OK")

    def encrypt(self, request):
        """A helper service method which encrypts the input string and Returns
        encrypted string as response.

        :return:`response` - A json object with encrypted string.
        """
        try:
            data = request.get_json()
            if not data:
                return make_response(util.create_response(status="error", message="Request Body Empty"), 400)
            if not data.get("input") :
                return make_response(util.create_response(status="error", message="Input String Empty"), 400)

            input = data.get('input')
            output = base64.b64encode(input.encode("utf-8")).decode('utf-8')
            return util.create_response(input=input,output=output)
        except Exception as e:
            return make_response(util.create_response(status="error", message="Something Went Wrong."), 500)

    def decrypt(self, request):
        """A helper service method which decrypts the input string and Returns
        decrypted string as response.

        :return:`response` - A json object with decrypted string.
        """
        try:
            data = request.get_json()
            if not data:
                return make_response(util.create_response(status="error", message="Request Body Empty"), 400)
            if not data.get("input") :
                return make_response(util.create_response(status="error", message="Input String Empty"), 400)

            input = data.get('input')
            output = base64.b64decode(input.encode("utf-8")).decode('utf-8')
            return util.create_response(input=input,output=output)
        except Exception as e:
            return make_response(util.create_response(status="error", message="Something Went Wrong."), 500)
