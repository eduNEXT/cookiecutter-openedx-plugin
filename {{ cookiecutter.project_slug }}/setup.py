"""
Setup file for cookiecutter-openedx-plugin Django plugin.
"""

from __future__ import print_function

import os
import re

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('cookiecutter_openedx_plugin', '__init__.py')


setup(
    name='cookiecutter-openedx-plugin',
    version=VERSION,
    description='Cookiecutter Open edX plugin template.',
    author='eduNEXT',
    author_email='contact@edunext.co',
    packages=[
        'cookiecutter_openedx_plugin'
    ],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [
            'cookiecutter_openedx_plugin = cookiecutter_openedx_plugin.apps:CookiecutterOpenEdxpluginConfig',
        ],
    }
)
