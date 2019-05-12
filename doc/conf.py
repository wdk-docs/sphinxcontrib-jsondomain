import alabaster

project = 'sphinxcontrib-jsondomain'
copyright = '2019, Band Cap'
release = '2.0'
version = '2.0.19'
needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinxcontrib-jsondomain',
]

master_doc = 'index'
html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_path = [alabaster.get_path()]
html_sidebars = {
    '**': ['about.html',
           'navigation.html'],
}
html_theme_options = {
    'description': 'Describe JSON documents',
    'github_user': 'wdk-docs',
    'github_repo': 'sphinxcontrib-jsondomain',
    'extra_nav_links': {'Index': 'genindex.html'},
}
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
