# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 IDS Mannheim
#
# invenio-oaiserver-cmdi is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_oaiserver_cmdi import InvenioOAIServerCMDI
from invenio_oaiserver_cmdi.views import blueprint
from invenio_oaiserver_cmdi.oai import cmdi_etree

from lxml import etree

def test_version():
    """Test version import."""
    from invenio_oaiserver_cmdi import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    assert "invenio-oaiserver-cmdi" not in app.extensions
    ext = InvenioOAIServerCMDI(app)
    assert "invenio-oaiserver-cmdi" in app.extensions
    app = Flask("testapp")
    assert "invenio-oaiserver-cmdi" not in app.extensions
    ext = InvenioOAIServerCMDI()
    ext.init_app(app)
    assert "invenio-oaiserver-cmdi" in app.extensions

def test_config(app):
    assert 'OAISERVER_METADATA_FORMATS' in app.config
    assert 'cmdi' in app.config['OAISERVER_METADATA_FORMATS']
    assert app.config['OAISERVER_METADATA_FORMATS']['cmdi']['namespace'] == "http://www.clarin.eu/cmd/1"

def test_blueprint(app):
     assert "invenio_oaiserver_cmdi" not in app.blueprints
     app.register_blueprint(blueprint)
     assert "invenio_oaiserver_cmdi" in app.blueprints

record = {
    "_source": {
        "id" : "foobar",
        "files": {}
        }
    }
def test_oai(app):
    tree = cmdi_etree(record["_source"]["id"],record)
    assert "No CMDI file found in record" in etree.tostring(tree).decode("utf-8")
