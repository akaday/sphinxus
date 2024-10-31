# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Sphinxus'
author = 'Author Name'
version = '1.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxus',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
