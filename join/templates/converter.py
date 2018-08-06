import os
from bs4 import BeautifulSoup

file_template = """
{% extends "base.html" %}
{% load static i18n %}
{% block content %}
<replace_me>
{% endblock %}
"""

if __name__ == '__main__':
    for file_name in os.listdir('./pages'):
        with open(os.path.join('./pages', file_name), encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, "html.parser")
            wrapper_boxed = soup.find("div", {"class": "wrapper-boxed"})
            content = file_template.replace("<replace_me>", str(wrapper_boxed))
            with open('./pages_templates/{}'.format(file_name), 'w+', encoding='utf-8') as out_f:
                out_f.write(content)

