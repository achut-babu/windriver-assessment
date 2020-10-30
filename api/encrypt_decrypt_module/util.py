# -*- coding: utf-8 -*-
"""Encrypt Decrypt Module Services.

:achut's Windriver Assessment Solution.
"""
from flask import jsonify

class Util:
    def create_response(self, input='', output='', status='success', message=''):
        """Utility method that forms the API response
        """
        return jsonify(
            {
                "Input": input,
                "Output": output,
                "Status": status,
                "Message": message
            }
        )
