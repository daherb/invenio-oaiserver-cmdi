
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 IDS Mannheim.
#
# invenio-oaiserver-cmdi is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module adding CMDI support to the OAI server."""

from .ext import InvenioOAIServerCMDI

__version__ = "1.0"

__all__ = ("__version__", "InvenioOAIServerCMDI")
