Lumache Examples
================

This section provides examples demonstrating the usage of the `lumache` module.

Generating HTML Documentation
-----------------------------

To generate HTML documentation using the `lumache` module, use the following code:

.. code-block:: python

    import lumache

    lumache.generate_html('docs/source', 'docs/build', theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])

Generating PDF Documentation
----------------------------

To generate PDF documentation using the `lumache` module, use the following code:

.. code-block:: python

    import lumache

    lumache.generate_pdf('docs/source', 'docs/build')

Generating ePub Documentation
-----------------------------

To generate ePub documentation using the `lumache` module, use the following code:

.. code-block:: python

    import lumache

    lumache.generate_epub('docs/source', 'docs/build')

Using the DocumentationBuilder Class
------------------------------------

The `DocumentationBuilder` class provides a convenient way to build documentation in various formats. Here are some examples:

Building HTML Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build HTML documentation using the `DocumentationBuilder` class, use the following code:

.. code-block:: python

    from lumache import DocumentationBuilder

    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_html(theme='sphinx_rtd_theme', custom_css=['custom.css'], custom_js=['custom.js'])

Building PDF Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

To build PDF documentation using the `DocumentationBuilder` class, use the following code:

.. code-block:: python

    from lumache import DocumentationBuilder

    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_pdf()

Building ePub Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build ePub documentation using the `DocumentationBuilder` class, use the following code:

.. code-block:: python

    from lumache import DocumentationBuilder

    builder = DocumentationBuilder('docs/source', 'docs/build')
    builder.build_epub()
