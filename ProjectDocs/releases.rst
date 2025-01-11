Releases
===========

To coordinate the efforts of the writers, editors, and illustrators
with the efforts of the digital team (e-readers, mentoris, web
version), we need to document how releases of the sequence will
happen. This is that document.

Timing
-----

We will do three releases every year: In April, in August, and in
December.  These times align with semesters in the US: The April
release will be for summer studies, the August release for fall, and
December for spring.

The releases will be described by `year.month[.build]`.  For example,
if the 2061 April release had a stupid mistake that forced us to
release it three times, the releases would be `2061.04`, `2061.04.1`,
and `2061.04.2`.  All three would be assumed to basically the same
with some bug fixes. We will only make only the last one available for
download.

When it exists in multiple languages, the release will include
versions for all languages.

PDFs
-----

Currently, the PDFs of the workbooks will be released:

* in US English

* in Letter-size

(These options will expand over time.)

In addition, a PDF of each chapter will be posted at
`kontinuafoundation.github.io <https://kontinuafoundation.github.io>`_

Digital Resources
---------

Associated with each chapter/language is a `digital_resources.json`
file with links to resources to supplement the reader's experience.
These will be part of the release.

Meta Data
---------

For each release, some meta data will also be produced for the digital side.

For each language, the reader apps need to know:
* Workbooks: Chapter (title, identifier, start page)
* Subject index: subject -> workbook/chapter

Mentoris needs to know differences:
* Inserted new chapters: title in every languange, identifier, location (workbook and order).
* Deleted old chapters
* Moved chapters
* Renamed chapters

These diffs will always be in reference to the previous major release.
That is the diffs for `2061.04.2` will be based on `2060.12` not
`2061.04.1`

Feedback
--------

In every place that we receive feedback, it is important that users
include what release they are giving feedback on.

Celebration
-----------

A release will be a big deal. There will be some celebration and PR.
