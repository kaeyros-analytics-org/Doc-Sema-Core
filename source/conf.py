# Configuration file for the Sphinx documentation builder.

project = 'Documentation Sema Universe'
copyright = '2026, Kaeyros Analytics SAS'
author = 'Kaeyros Analytics SAS'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'fr'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/sema_core_logo.png'
html_show_copyright = True
html_show_sphinx = False
html_show_sourcelink = False

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}


def setup(app):
    app.add_css_file('custom.css')
