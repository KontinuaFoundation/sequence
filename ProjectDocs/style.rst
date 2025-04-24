Style Guide
===========

This is a guide to the style and voice of the textbook for writers and
editors. When several people contribute to a book, it is important that
the flow of the experience not be damaged by sudden changes in the style
and voice.

This style guide will expand as we debate and codify the rules, so it is
important to have a default for undecided questions. We will be using
`The Google Developer Documentation Style
Guide <https://developers.google.com/style/>`__ as our default.

Voice
-----

Our text will have a less formal, more conversational tone than most
math textbooks. However, it will not try to be funny, like the Dummies
books do.

Kontinua and the authors will be referred to as “We.” The reader will be
referred to as “You.” For example: “You are not expected to understand
this yet, but we will explain it in the next chapter.”

The ideas we teach are complicated, so we will try to keep the prose
simple. Try for a 4th grade reading level.

We do not generally use contractions. While they are natural to write,
most readers (especially readers for whom English is not their first
langauge) find them less easy to read.

We try to use inclusive language: “The passenger checked their bag at
the door” is better than “The passenger checked his bag at the door.”

We do not avoid terms and metaphors that acknowledge wrongs, whether
historical or contemporary. For example, we are OK with “The system uses
master-slave replication.”

We avoid sports metaphors. Most people who use English are not American,
and sports metaphors are needlessly confusing for them.

It is OK to order the reader around: “Open a new file and save it as
``foo.txt``.”

Python code should be formatted as it would be by the ``black`` code
formatter tool.

Images and Plots
----------------

Keep in mind that we are trying to make these books inexpensive to
produce.

For people making small batches, they will be printed on a laser
printer. Keep in mind how much toner your diagrams are consuming. Some
of the printers will be Black and White — make sure your diagram looks
good in grayscale.

For companies making large batches, we want to keep the printing down to
two colors: Black and SDKBlue. What is SDKBlue? CMYK =
:math:`[1.0,.54,.04,.19]`

Indexing
--------

Please index your chapters as you go along. I typically add the
``\index`` tags at the end of the paragraph that starts a topic.

Generally, index tags are not capitalized unless they are proper nouns.

::

   \newterm{Lunch} is a meal that is eaten in the middle of the day. Some 
   people have peanut butter and jelly sandwiches for lunch.\index{lunch}
   \index{sandwich!peanut butter and jelly}

Internationalization
--------------------

The build system is designed to allow the text to be customized for
different langauges and locales. For example, when you are editing
``Chapters/vectors/en_US/student.tex``, you are editing the US English
version of the Vectors chapter of the student guide.

In general, diagrams and other resources that might need to be
internationalized should go into that same directory.

Page size
---------

Once again, for cost reasons, we will use the two most common paper
sizes in the world: Letter and A4. For these sizes, there will be a
standard sized margin.

We will also do a “Tablet Size”, which will be smaller and have a
minimal border. The goal is to have a format that will look good when
read on a tablet like a 10” iPad.

Tools
-----

You can assume that the reader has access to a computer with:

-  A text editor
-  A python 3 interpreter
-  A spreadsheet program

They are expected to have the following python frameworks installed:

-  matplotlib
-  numpy
-  scikit-learn
-  scipy
-  pandas
-  tensorflow

TeX formatting
--------------

Please wrap your text to 80 columns. LaTeX will rewrap them, but 80
columns makes it easy for anyone to open them in any text editor.

Please don’t add libraries to the individual ``.tex`` files. We will
agree on a set of libraries and they will all be added in the preable.

If you chapter includes code, please include the source code in the
repository.
