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

html_theme = 'pydata_sphinx_theme'
html_title = 'Guide utilisateur Sema Universe'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/sema_core_logo.png'
html_favicon = '_static/sema_core_logo.png'
html_show_copyright = True
html_show_sphinx = False
html_show_sourcelink = False
html_permalinks = False

html_theme_options = {
    'logo': {
        'image_light': '_static/sema_core_logo.png',
        'image_dark': '_static/sema_core_logo.png',
        'text': 'Sema Core',
        'alt_text': 'Sema Core',
    },
    'navbar_start': ['navbar-logo'],
    'navbar_center': [],
    'navbar_persistent': ['search-button-field'],
    'navbar_end': ['navbar-icon-links'],
    'icon_links': [
        {
            'name': 'Plateforme Sema',
            'url': 'https://dashboard.dev.sem-a.com/fr',
            'icon': 'fa-solid fa-arrow-up-right-from-square',
        },
        {
            'name': 'Site Sema',
            'url': 'https://www.sem-a.com/fr',
            'icon': 'fa-solid fa-globe',
        },
    ],
    'search_bar_text': 'Rechercher dans la documentation...',
    'navigation_depth': 3,
    'collapse_navigation': False,
    'show_nav_level': 2,
    'show_toc_level': 2,
    'show_prev_next': True,
    'secondary_sidebar_items': ['page-toc'],
    'primary_sidebar_end': [],
}
