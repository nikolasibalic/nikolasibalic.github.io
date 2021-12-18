# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Nikola Šibalić'
copyright = '2021, Nikola Šibalić'
author = 'Nikola Šibalić'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'nbsphinx',
    'sphinx_copybutton',
    'sphinx_panels'
]

nbsphinx_codecell_lexer = 'ipython3'

intersphinx_mapping = {
    'python': ('https://docs.python.org/dev', (None, 'intersphinx/python-objects.inv')),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', (None, 'intersphinx/scipy-objects.inv')),
    'numpy': ('https://numpy.org/doc/stable', (None, 'intersphinx/numpy-objects.inv')),
    'matplotlib': ('https://matplotlib.org/stable', (None, 'intersphinx/matplotlib-objects.inv')),
}

autodoc_default_flags = ['members', 'inherited-members']
autosummary_imported_members= True

pygments_style = 'sphinx'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "github_url": "https://github.com/nikolasibalic",
    "use_edit_page_button": False,
    "show_toc_level": 1,
    # "show_nav_level": 2,
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "navbar_start": ["navbar-logo", "navbar-version"],
    # "navbar_center": ["navbar-nav", "navbar-version"],  # Just for testing
    # "navbar_end": ["navbar-icon-links", "navbar-version"]  # Just for testing
    # "footer_items": ["copyright", "sphinx-version", ""]
}