.. _quickstart:

Quickstart
==========

To use Clopy, you must define a ``template.py`` file in your template directory.
This file is used by Clopy to hook into your template to allow you to specify prompts and files
that will be copied over to the new directory.

Here is a sample file:

.. code-block:: python

    # template.py

    def bang(fp, cmd):
        license = input('What license will you use? [MIT or GPLv3]? : ')
        licensedict = {
            'license': license
        }
        tmpls = {
        'LICENSE': licensedict
        }


        # Initialize all templates
        outputs = init_all(fp, tmpls)

        # Output all files
        for name, out in outputs.items():
            output(path, name, out)

The only requirements for the ``template.py`` file are that:

- The template file is named exactly ``template.py``
- There exists the following function in ``template.py``:

.. code-block:: python

    def bang(fp, cmd)

The template file is a Jinja template that is initialized with the values
of the user input at runtime.
