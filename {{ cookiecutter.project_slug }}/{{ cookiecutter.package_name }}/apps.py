"""
App configuration for {{ cookiecutter.package_name }}.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class {{ cookiecutter.class_name }}Config(AppConfig):
    """
    {{ cookiecutter.project_desc }} configuration.
    """
    name = '{{ cookiecutter.package_name }}'
    verbose_name = '{{ cookiecutter.project_desc }}'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': '{{ cookiecutter.package_name }}',
                'regex': r'^{{ cookiecutter.package_name }}/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': '{{ cookiecutter.package_name }}',
                'regex': r'^{{ cookiecutter.package_name }}/',
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
