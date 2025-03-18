=================
Digital Resources
=================

You can think of each chapter as made up of several learning
objectives.  The sequence, then, is a directed graph — each chapter
covers some objectives and relies upon some prerequisite objectives.

Each of these objectives gets a short unique ID. For example, "atmos" might represent
the objective of having the student understand the idea of atmospheric pressure.

In addition to an ID, each objective gets:

* A description: "Atmospheric pressure and altitude" (required)
* Some online video links (optional)
* Some online reference links (optional)

Besides a list of objectives that a chapter supplies and the list of objectives that
are prerequisites,  the chapter can have some files the student can use.  For example, maybe
a Python program that the student can download and run.

===================
gather_resources.py
===================

In the Build directory, there is a Python program called ``gather_resources.py``.

This program walks the chapter directories, parsing each ``digital_resources.json`` and
creating a web page for each book. Here, for example, is the section for "The Physics of Gases":

.. image:: webresources.png
    :width: 700 px

It is run as you would expect from inside the ``Build`` directory::

    python3 gather_resources.py


======================
digital_resources.json
======================

Here is an example of ``digital_resources.json`` file for a chapter::

    {
    "files": [
    {
      "path": "ar_plot.py",
      "desc": "Python program that generated PDF of molecular speeds"
    }
      ],
        "requires": [
        "atom",
        "fma",
        "mole",
        "energy-forms"
      ],
     "covers": [
        {
          "id": "atmos",
         "desc": "Atmospheric pressure and altitude",
          "videos": [
            "https://youtu.be/xJHJsA7bYGc?si=-GvNXz-qVjSrAIhd"
          ],
          "references": [
            "https://en.wikipedia.org/wiki/Atmospheric_pressure"
          ]
        },
        {
          "id": "gas-temp",
          "desc": "How the temperature of a gas relates to the speed of the molecules",
          "videos": [
            "https://youtu.be/1S9cuYascPQ?si=-3l1h9QrUsXhvhZC"
          ],
         "references": [
           "https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Map%3A_Physical_Chemistry_for_the_Biosciences_(Chang)/02%3A_Properties_of_Gases/2.06%3A_Kinetic_Theory_of_Gases",
            "https://en.wikipedia.org/wiki/Kinetic_theory_of_gases"
          ]
        },
        {
          "id": "abs-zero",
          "desc": "Absolute zero",
          "videos": [
           "https://youtu.be/TNUDBdv3jWI?si=KCVL8xng5c-vvzbb"
          ],
          "references": [
            "https://en.wikipedia.org/wiki/Absolute_zero"
          ]
        },
        {
          "id": "ideal-gas-law",
          "desc": "The Ideal Gas Law",
          "videos": [
            "https://youtu.be/qObcdZj8YTM?si=KqJZqU7QSIuc91ol"
          ],
          "references": [
           "https://en.wikipedia.org/wiki/Ideal_gas_law"
          ]
        }
      ]
    }

The structure makes sense, right?  Yes, but it is a real hassle to try to type it, and
every chapter needs one. So:

==================
KontinuaResourceEditor
==================

There is a Mac application that makes it easy to create these files.  Here is `the source <https://github.com/KontinuaFoundation/KontinuaResourceEditor>`_.
