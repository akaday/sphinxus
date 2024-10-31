"""
Lumache - A Sphinxus Extension

This module provides additional functionality for generating documentation
in various formats, customizing themes and templates, and offering advanced
configuration options.
"""

from sphinx.application import Sphinx

def generate_html(source_dir, build_dir, theme='alabaster', custom_css=None, custom_js=None):
    """
    Generate HTML documentation from the source directory with optional customizations.

    :param source_dir: The source directory containing the reStructuredText files.
    :param build_dir: The directory where the generated HTML files will be stored.
    :param theme: The theme to use for the HTML documentation.
    :param custom_css: A list of custom CSS files to include.
    :param custom_js: A list of custom JavaScript files to include.
    :returns: None
    """
    app = Sphinx(
        srcdir=source_dir,
        confdir=None,
        outdir=build_dir,
        doctreedir=build_dir + '/doctrees',
        buildername='html',
        confoverrides={
            'html_theme': theme,
            'html_css_files': custom_css or [],
            'html_js_files': custom_js or [],
        }
    )
    app.build()

def generate_pdf(source_dir, build_dir):
    """
    Generate PDF documentation from the source directory.

    :param source_dir: The source directory containing the reStructuredText files.
    :param build_dir: The directory where the generated PDF files will be stored.
    :returns: None
    """
    app = Sphinx(
        srcdir=source_dir,
        confdir=None,
        outdir=build_dir,
        doctreedir=build_dir + '/doctrees',
        buildername='latex'
    )
    app.build()

def generate_epub(source_dir, build_dir):
    """
    Generate ePub documentation from the source directory.

    :param source_dir: The source directory containing the reStructuredText files.
    :param build_dir: The directory where the generated ePub files will be stored.
    :returns: None
    """
    app = Sphinx(
        srcdir=source_dir,
        confdir=None,
        outdir=build_dir,
        doctreedir=build_dir + '/doctrees',
        buildername='epub'
    )
    app.build()

class DocumentationBuilder:
    """
    A class for building documentation using Lumache.
    """

    def __init__(self, source_dir, build_dir):
        """
        Initialize the DocumentationBuilder with the source and build directories.

        :param source_dir: The source directory containing the reStructuredText files.
        :param build_dir: The directory where the generated documentation files will be stored.
        """
        self.source_dir = source_dir
        self.build_dir = build_dir

    def build_html(self, theme='alabaster', custom_css=None, custom_js=None):
        """
        Build HTML documentation with optional customizations.

        :param theme: The theme to use for the HTML documentation.
        :param custom_css: A list of custom CSS files to include.
        :param custom_js: A list of custom JavaScript files to include.
        :returns: None
        """
        generate_html(self.source_dir, self.build_dir, theme, custom_css, custom_js)

    def build_pdf(self):
        """
        Build PDF documentation.

        :returns: None
        """
        generate_pdf(self.source_dir, self.build_dir)

    def build_epub(self):
        """
        Build ePub documentation.

        :returns: None
        """
        generate_epub(self.source_dir, self.build_dir)
