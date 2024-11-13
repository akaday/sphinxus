API Reference
=============

This section provides detailed documentation for the available functions and classes in Sphinxus.

Functions
---------

.. function:: sphinxus.generate_html(source_dir, build_dir)

   Generate HTML documentation from the source directory.

   :param source_dir: The source directory containing the reStructuredText files.
   :param build_dir: The directory where the generated HTML files will be stored.
   :returns: None

   Example usage:

   .. code-block:: python

      import sphinxus

      sphinxus.generate_html('docs/source', 'docs/build')

.. function:: sphinxus.generate_pdf(source_dir, build_dir)

   Generate PDF documentation from the source directory.

   :param source_dir: The source directory containing the reStructuredText files.
   :param build_dir: The directory where the generated PDF files will be stored.
   :returns: None

   Example usage:

   .. code-block:: python

      import sphinxus

      sphinxus.generate_pdf('docs/source', 'docs/build')

.. function:: lumache.generate_html(source_dir, build_dir, theme='alabaster', custom_css=None, custom_js=None)

   Generate HTML documentation from the source directory with optional customizations.

   :param source_dir: The source directory containing the reStructuredText files.
   :param build_dir: The directory where the generated HTML files will be stored.
   :param theme: The theme to use for the HTML documentation.
   :param custom_css: A list of custom CSS files to include.
   :param custom_js: A list of custom JavaScript files to include.
   :returns: None

   Example usage:

   .. code-block:: python

      import lumache

      lumache.generate_html('docs/source', 'docs/build', theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])

.. function:: lumache.generate_pdf(source_dir, build_dir)

   Generate PDF documentation from the source directory.

   :param source_dir: The source directory containing the reStructuredText files.
   :param build_dir: The directory where the generated PDF files will be stored.
   :returns: None

   Example usage:

   .. code-block:: python

      import lumache

      lumache.generate_pdf('docs/source', 'docs/build')

.. function:: lumache.generate_epub(source_dir, build_dir)

   Generate ePub documentation from the source directory.

   :param source_dir: The source directory containing the reStructuredText files.
   :param build_dir: The directory where the generated ePub files will be stored.
   :returns: None

   Example usage:

   .. code-block:: python

      import lumache

      lumache.generate_epub('docs/source', 'docs/build')

Classes
-------

.. class:: sphinxus.DocumentationBuilder

   A class for building documentation using Sphinxus.

   .. method:: __init__(self, source_dir, build_dir)

      Initialize the DocumentationBuilder with the source and build directories.

      :param source_dir: The source directory containing the reStructuredText files.
      :param build_dir: The directory where the generated documentation files will be stored.

   .. method:: build_html(self)

      Build HTML documentation.

      :returns: None

      Example usage:

      .. code-block:: python

         builder = sphinxus.DocumentationBuilder('docs/source', 'docs/build')
         builder.build_html()

   .. method:: build_pdf(self)

      Build PDF documentation.

      :returns: None

      Example usage:

      .. code-block:: python

         builder = sphinxus.DocumentationBuilder('docs/source', 'docs/build')
         builder.build_pdf()

.. class:: lumache.DocumentationBuilder

   A class for building documentation using Lumache.

   .. method:: __init__(self, source_dir, build_dir)

      Initialize the DocumentationBuilder with the source and build directories.

      :param source_dir: The source directory containing the reStructuredText files.
      :param build_dir: The directory where the generated documentation files will be stored.

   .. method:: build_html(self, theme='alabaster', custom_css=None, custom_js=None)

      Build HTML documentation with optional customizations.

      :param theme: The theme to use for the HTML documentation.
      :param custom_css: A list of custom CSS files to include.
      :param custom_js: A list of custom JavaScript files to include.
      :returns: None

      Example usage:

      .. code-block:: python

         builder = lumache.DocumentationBuilder('docs/source', 'docs/build')
         builder.build_html(theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])

   .. method:: build_pdf(self)

      Build PDF documentation.

      :returns: None

      Example usage:

      .. code-block:: python

         builder = lumache.DocumentationBuilder('docs/source', 'docs/build')
         builder.build_pdf()

   .. method:: build_epub(self)

      Build ePub documentation.

      :returns: None

      Example usage:

      .. code-block:: python

         builder = lumache.DocumentationBuilder('docs/source', 'docs/build')
         builder.build_epub()
