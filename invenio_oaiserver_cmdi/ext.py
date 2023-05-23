# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 IDS Mannheim
#
# invenio-oaiserver-cmdi is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module for CMDI support for the OAI server."""

from . import config
    
class InvenioOAIServerCMDI(object):
    """invenio-oaiserver-cmdi extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-oaiserver-cmdi"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            app.config.setdefault(k, getattr(config, k))
        # Add CMDI to the metadata formats
        app.config.setdefault('OAISERVER_METADATA_FORMATS',{}).update({"cmdi": \
        {
            "serializer": ("invenio_oaiserver_cmdi.oai:cmdi_etree"),
            "schema": "https://infra.clarin.eu/CMDI/1.x/xsd/cmd-envelop.xsd",
            "namespace": "http://www.clarin.eu/cmd/1",
        }})
