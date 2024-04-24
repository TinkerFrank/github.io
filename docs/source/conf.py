# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TinkerFrank'
copyright = '2024, TinkerFrank'
author = 'Frank'
release = '0.2'
version = 'Engineering | Machine Learning | Cybersecurity | Entrepeneurship'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_rtd_dark_mode',
    'sphinx_design',
    'sphinxcontrib.video',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.png'  # Adjust the path according to your file locationsphin

# html_theme_options = {
#     ...
#     "repository_url": "https://github.com/{your-docs-url}",
#     "use_repository_button": True,
#     ...
# }

html_theme_options = {
    'logo_only': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# File-wide metadata
html_context = {
    'display_github': True,
    'github_user': 'TinkerFrank',
    'github_repo': 'tinkerfrank.github.io',
    'github_version': 'main/docs/source/',
}

