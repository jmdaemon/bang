.. _config:

Config
======

Clopy can be configured to use a ``templates.json`` file to read template file paths from as a shorthand.
This file is stored in the ``~/.config/clopy/templates`` directory.
An example config file is given in the root project directory.

.. code-block:: json

    {
        "templates": {
            "python": "~/Templates/python-template"
        }
    }

Now instead of doing this:

.. code-block:: console

   clopy new ~/Templates/python-template

You can run
   
.. code-block:: console

   clopy new python

And Clopy will look up the directory associated with the directory keyword.


Configuring Templates
---------------------

Templates can also have configuration files.
These files are located in ``~/.config/clopy/templates/```.
These configuration files are stored in TOML format that you can use to define your own configuration variables
for your templates.
