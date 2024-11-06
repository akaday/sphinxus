import pytest
from lumache import generate_html, generate_pdf, generate_epub, DocumentationBuilder

def test_generate_html():
    # Test generating HTML documentation with default parameters
    generate_html('docs/source', 'docs/build')
    # Add assertions to verify the generated HTML files

def test_generate_html_with_customizations():
    # Test generating HTML documentation with custom theme, CSS, and JS
    generate_html('docs/source', 'docs/build', theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])
    # Add assertions to verify the generated HTML files with customizations

def test_generate_pdf():
    # Test generating PDF documentation
    generate_pdf('docs/source', 'docs/build')
    # Add assertions to verify the generated PDF files

def test_generate_epub():
    # Test generating ePub documentation
    generate_epub('docs/source', 'docs/build')
    # Add assertions to verify the generated ePub files

def test_documentation_builder_html():
    # Test DocumentationBuilder for HTML documentation
    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_html()
    # Add assertions to verify the generated HTML files

def test_documentation_builder_html_with_customizations():
    # Test DocumentationBuilder for HTML documentation with customizations
    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_html(theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])
    # Add assertions to verify the generated HTML files with customizations

def test_documentation_builder_pdf():
    # Test DocumentationBuilder for PDF documentation
    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_pdf()
    # Add assertions to verify the generated PDF files

def test_documentation_builder_epub():
    # Test DocumentationBuilder for ePub documentation
    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_epub()
    # Add assertions to verify the generated ePub files
