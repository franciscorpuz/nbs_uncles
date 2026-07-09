import os
import sys
# Tell Sphinx to find your raw source code
sys.path.insert(0, os.path.abspath('../../src'))

# 1. Activate tools for docstrings and notebook rendering
extensions = [
    'sphinx.ext.autodoc',      # Extracts docstrings
    'sphinx.ext.napoleon',     # Translates NumPy style docstrings
    'sphinx.ext.viewcode',     # Links to your source code
    'myst_nb',                 # Renders .ipynb notebooks
]

# 2. Match your NumPy docstring style
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# 3. Read saved notebooks WITHOUT re-running code simulations
nb_execution_mode = "off"

# 4. Visual theme
html_theme = 'sphinx_rtd_theme'