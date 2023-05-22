# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 IDS Mannheim
#
# invenio-oaiserver-cmdi is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for CMDI support for the OAI server."""

from flask import Blueprint, render_template, current_app
import logging
LOGGER = logging.getLogger(__name__)
blueprint = Blueprint(
    "invenio_oaiserver_cmdi",
    __name__,
    template_folder="templates",
    static_folder="static",
)
