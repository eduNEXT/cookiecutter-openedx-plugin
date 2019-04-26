"""
App configuration for cookiecutter-openedx-plugin.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class CookiecutterOpenEdxpluginConfig(AppConfig):
    """
    Cookiecutter-openedx-plugin configuration.
    """
    name = 'cookiecutter_openedx_plugin'
    verbose_name = "Cookiecutter Open edX plugin."

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'cookiecutter_openedx_plugin',
                'regex': r'^cookiecutter_openedx_plugin/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'cookiecutter_openedx_plugin',
                'regex': r'^cookiecutter_openedx_plugin/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
