"""
AWS Django settings for {{ cookiecutter.package_name }} project.

Juniper release will remove aws.py file. https://openedx.atlassian.net/browse/DEPR-14
"""

from __future__ import unicode_literals

from .production import plugin_settings  # pylint: disable=unused-import
