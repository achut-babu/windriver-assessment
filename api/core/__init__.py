# -*- coding: utf-8 -*-

"""A list of CORE servcies which are used by the modules defined throughout
the Flask Application.

This allows us to build re-usable modular core services which may be used from
within modules of this application. For now, we have only two such core
services but setting it up like this allows us to scale the application when
we add more core services for e.g. like caching, events, sessions etc...

:achut's Windriver Assessment Solution.
"""

from .services import ServiceRegistry

__all__ = [
    'ServiceRegistry',
    'encrypt_decrypt_module'
]
