Installation
============

To install Sphinxus, follow these steps:

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install Sphinxus using pip:

```bash
pip install sphinxus
```

3. Set up a new documentation project:

```bash
sphinx-quickstart
```

4. Configure your `conf.py` file to use Sphinxus:

```python
extensions = [
    'sphinxus',
    # other extensions
]
```

Reinitializing Sphinx
----------------------

If you need to reinitialize Sphinx to set up the necessary files in the source directory, follow these steps:

1. Delete the existing `docs` directory or move it to a backup location.
2. Run the `sphinx-quickstart` command again to create a new documentation project:

```bash
sphinx-quickstart
```

3. Configure your `conf.py` file to use Sphinxus and any other extensions you need.
4. Rebuild the documentation using the `sphinx-build` command.
