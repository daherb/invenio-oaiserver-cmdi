# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 IDS Mannheim
#
# invenio-oaiserver-cmdi is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
from flask import current_app, url_for, g
from lxml import etree
from invenio_rdm_records.oai import getrecord_fetcher
from invenio_rdm_records.proxies import current_rdm_records
import requests

def files_service():
    """Get the record files service."""
    return current_rdm_records.records_service.files

def cmdi_etree(pid, record):
    pid_value = record["_source"]["id"]
    # We use the default preview to determine the CMDI file to be delivered
    if ("default_preview" in record["_source"]["files"]):
        file_key = record["_source"]["files"]["default_preview"]
        read_kwargs = {"id_": pid_value, "file_key": file_key, "identity": g.identity}
        file_content = files_service().get_file_content(**read_kwargs)
        with file_content.get_stream('r') as stream:
            cmdi = stream.read()
        return etree.fromstring(bytes(cmdi, "utf-8"))
    # Otherwise return a empty CMD document
    etree.register_namespace('cmd',"http://www.clarin.eu/cmd/1") #some name
    root = etree.Element("{http://www.clarin.eu/cmd/1}CMD")
    root.append(etree.Comment(" No CMDI file found in record " + pid_value + " "))
    return root
