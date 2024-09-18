{% set is_open_source = cookiecutter.license != 'Not open source' -%}
# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* License: {{ cookiecutter.license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

# Features
* TODO

# Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the template [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage).
