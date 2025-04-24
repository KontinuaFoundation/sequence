===============================
How to write/edit the workbooks
===============================

You must have a github account.

If you haven't been made a collaborator, you will need to do your
edits in your own fork.  Go to
https://github.com/KontinuaFoundation/sequence/tree/master and use the menu
to create a fork.

First, you need to follow the instructions for cloning the repository
and building the book. You can find these in the
`README.rst <https://github.com/KontinuaFoundation/sequence/blob/master/README.rst>`_.
Be sure to use the URL for *your* fork when you do the clone.

Next, create a new branch::

  git checkout myawesomebranch

Make all the edits you want (more on that below). Double-check that the book still
builds. (If editing takes more than a day or two, you may want to re-sync
your fork so that you aren't too far out of sync with everyone
else. You can do this through the web interface on github.)

Commit and push what you have to your fork::

  git commit -a -m 'Made the plot blue'
  git push

To make a pull request for your branch, go to the original repository
on github (https://github.com/KontinuaFoundation/sequence/pulls) and find
your branch in your fork.  Make a pull request from it.

=======
Editing
=======

The source is in the ``Chapters`` directory.  For each workbook, there is a
text file with the names of the directories that go into that
workbook. For example, there is a ``book_01.txt`` which lists several
directories::

  matter_energy_intro
  atomic_mass
  work_energy
  units_conversions
  simple_machines
  buoyancy
  heat

Inside the ``matter_energy_intro`` chapter, there is a directory for
each language (using the ISO code). At this point, it is just ``en_US``,
but one day there will be more.  Inside ``en_US`` is ``student.tex``.
That is the LaTeX for this chapter.

The first line should just be::

  \chapter{Matter and Energy}

All the normal preamble stuff is in the ``Build/Support`` directory.

Most of the libraries you would want are included.  Take a look at
other chapters to get a good feel for how we do it.

There is also a ``digital_resources.json`` file. These are the links to
videos and other digital resources teh student would want.  It also
defines the dependencies of the chapter: what are the prequisites?
What objectives does the chapter attempt to cover?

Anything you put in the repository becomes property of The Kontinua Foundation, Inc.

============
New Chapters
============

If you want to create a new chapter, you will need to give it a unique ID like ``smells``.

Add ``smells`` in the appropriate line in the appropriate ``book_??.txt``.

Create ``Chapters/smells/en_US/`` directory and put a new ``student.tex`` and
``digital_resources.json`` in it.

Add all that to the repo.  If you are working on a Mac, please don't add any ``DS_Store`` files.

======
Images
======

Images should be PNG or SVG.  An image should be in the same directory as
the ``student.tex`` that references it.

If you use another application to create the image, please include the original source.
For example, I have done a few diagrams in OmniGraffle. I have included the ``.graffle`` file.

Overall, I'm trying to do diagrams in LaTeX whenever possible.  Maintanence is
just so much easier.

======
Code
======

Code should be in Python (Although I think I"m going to do some data structures
code in C++.  The student should see pointers and understand the stack and heap, right?).

Include it in the directory for the chapter that uses it.

======
Style
======

You can refer to the style guide
`The Style Guide <style.rst>`__
