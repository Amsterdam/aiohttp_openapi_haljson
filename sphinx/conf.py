# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file. See <http://www.sphinx-doc.org/en/stable/config.html>
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sphinx_rtd_theme
import urllib.request
#import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('..'))


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',  # must be loaded _after_ napoleon.
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

master_doc='index'

# General information about the project.
project = 'aiohttp_extras'
# noinspection PyShadowingBuiltins
copyright = '2017, Gemeente Amsterdam'
author = 'Amsterdam City Data'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

add_module_names = False

default_role = 'py:obj'

# nitpicky = False

# This value contains a list of modules to be mocked up. This is useful when
# some external dependencies are not met at build time and break the building
# process. You may only specify the root package of the dependencies themselves
# and ommit the sub-modules:
autodoc_mock_imports = ['aiohttp.web_exceptions']


# -- Options for extensions -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6/', 'python.inv'),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', 'sphinx.inv'),
    'aiohttp': ('http://aiohttp.readthedocs.io/en/stable/', 'aiohttp.inv'),
    'jwt': ('https://pyjwt.readthedocs.io/en/latest/', 'jwt.inv'),
}

for inventory in intersphinx_mapping:
    if not os.path.exists(intersphinx_mapping[inventory][1]):
        urllib.request.urlretrieve(
            intersphinx_mapping[inventory][0] + 'objects.inv',
            filename=intersphinx_mapping[inventory][1]
        )
        os.system(
            """
                {{
                    printf "\\x1f\\x8b\\x08\\x00\\x00\\x00\\x00\\x00";
                    tail -n +5 '{0}';
                }} | gunzip --quiet >'{0}.txt'
            """.format(intersphinx_mapping[inventory][1])
        )


autodoc_default_flags = [
    'members',
    'private-members',
    #'special-members',
    #'undoc-members',
    'show-inheritance'
]

# Extract both the class docstring and the docstring in __init__ or __new__.
# By default, autoclass only extracts the class-level docstring.
# See also the `napoleon_include_init_with_doc` parameter.
#autoclass_content = 'both'

extlinks = {
    'epic': ('https://taiga.datapunt.amsterdam.nl/project/kpaska-datapunt-backend/epic/%s', 'epic #'),
    'story': ('https://taiga.datapunt.amsterdam.nl/project/kpaska-datapunt-backend/us/%s', 'user story #'),
    'task': ('https://taiga.datapunt.amsterdam.nl/project/kpaska-datapunt-backend/task/%s', 'task #'),
}


# Napoleon settings:

#napoleon_google_docstring = True
napoleon_numpy_docstring = False
# True to list __init___ docstrings separately from the class docstring.  False
# to fall back to Sphinx’s default behavior, which considers the __init___
# docstring as part of the class documentation.  Defaults to False.
napoleon_include_init_with_doc = True
#napoleon_include_private_with_doc = False
#napoleon_include_special_with_doc = True
#napoleon_use_admonition_for_examples = False
#napoleon_use_admonition_for_notes = False
#napoleon_use_admonition_for_references = False
#napoleon_use_ivar = False
#napoleon_use_param = True
#napoleon_use_keyword = True
#napoleon_use_rtype = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# Sphinx RTD theme:
html_theme_options = {
    #'typekit_id': 'hiw1hhg',
    #'analytics_id': None,
    #'sticky_navigation': False,
    #'logo_only': None,
    #'collapse_navigation': True,
    'collapse_navigation': False,
    #'display_version': True,
    #'navigation_depth': 4,
    #'prev_next_buttons_location': 'bottom',
    'canonical_url': 'https://amsterdam.github.io/aiohttp_openapi_haljson/',
}

html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
    ],
}
