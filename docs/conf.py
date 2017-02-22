import sys
import os
import shlex
import sys

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
]

templates_path = ['_templates']

master_doc = 'index'

project = u'HoverPy'
copyright = u'2017, SpectoLabs'
author = u'SpectoLabs'

version = '0.2.2'
# The full version, including alpha/beta/rc tags.
release = version

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

if 'READTHEDOCS' not in os.environ:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

html_context = {
   'css_files': [                                                           
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',            
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',       
            '_static/theme_overrides.css',   
        ],
    }


html_show_sphinx = False

html_show_copyright = True

htmlhelp_basename = 'hoverpydoc'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}


latex_documents = [
    (master_doc, 'hoverpy.tex', u'HoverPy Documentation',
     u'SpectoLabs', 'manual'),
]

man_pages = [
    (master_doc, 'HoverPy', u'HoverPy Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'HoverPy', u'HoverPy Documentation',
     author, 'HoverPy', 'Python library for Hoverfly API simulation tool',
     'Miscellaneous'),
]
