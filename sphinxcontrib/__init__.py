# -*- coding: utf-8 -*-
"""
    sphinxcontrib
    ~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2009 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

__import__('pkg_resources').declare_namespace(__name__)

import os
from os import path
from sphinx.locale import get_translation

MESSAGE_CATALOG_NAME = 'sphinxcontrib-jsondomain'  # name of *.pot, *.po and *.mo files
_ = get_translation(MESSAGE_CATALOG_NAME)
text = _('Hello jsondomain!')

def setup(app):
    package_dir = path.abspath(path.dirname(__file__))
    locale_dir = os.path.join(package_dir, 'locale')
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_dir)
