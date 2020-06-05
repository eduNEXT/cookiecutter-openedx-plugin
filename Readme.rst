This is a cookiecutter template for new Open edX plugins.

It enables creation of the plugin with the best practices we at eduNEXT have compiled over time.

We talk about it here:

- https://youtu.be/0AdPHfjQ0wQ
- https://docs.google.com/presentation/d/1ESyWbojf7tAtn4ODPTiUNOOh9JDuVmebdhpEBT5NSF8/edit?usp=sharing

Usage
=====

To create a new plugin+ using this cookiecutter template, first make sure you have cookiecutter installed.

Then run::

        $ cookiecutter https://github.com/eduNEXT/cookiecutter-openedx-plugin.git

Enter the variables when prompted.


- project_desc -> human readable description of your plugin
- package_name -> python package name. You can use _ for spaces
- project_slug -> Normally also the repo name. You can use - or _ for spaces
- class_name -> used when defining the app config python class

Once the openedx plugin is initialized, you should run in the root of the plugin **`make upgrade`** in order to generate the .txt requirements files used in the tests and for local development.
