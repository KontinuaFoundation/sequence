# Releases

To coordinate the efforts of the writers, editors and illustrators with the
efforts of the digital team (e-readers, Mentoris, the web version), this document
explains how releases of the sequence will happen.

## Timing

We will do three releases every year: in April, in August and in December. These
times align with semesters in the US: the April release will be for summer
studies, the August release for fall, and December for spring.

Releases are named `year.month[.build]`. For example, if the April 2061 release
had a mistake that forced us to release it three times, the releases would be
`2061.04`, `2061.04.1` and `2061.04.2`. All three would be basically the same,
with some bug fixes. We will only make the latest version available for
download.

When the workbooks exist in multiple languages, a release will include versions
for all languages.

## PDFs

Currently, the PDFs of the workbooks are released:

* In US English
* In Letter size

(These options will expand over time. The build can already make A4 workbooks.)

In addition, a PDF of each chapter is posted at
[kontinuafoundation.github.io](https://kontinuafoundation.github.io). That site
is updated automatically; see [Administration](admin.md).

## Digital resources

Associated with each chapter and language is a `digital_resources.json` file with
links to resources that supplement the reader's experience (see
[Digital Resources](digital_resources.md)). These are part of the release.

## Metadata

For each release, some metadata is also produced for the digital side.

For each language, the reader apps need to know:

* Workbooks: chapter (title, identifier, start page)
* Subject index: subject → workbook/chapter

`Build/gather_ebook_resources.py` writes each workbook's chapters, their
starting pages and the topics they cover, and `Build/upload_collection.py`
uploads that with the PDFs.

Mentoris needs to know the following differences:

* Inserted new chapters: title in every language, identifier, location (workbook
  and order)
* Deleted old chapters
* Moved chapters
* Renamed chapters

These differences are always in reference to the previous major release. In
other words, the differences for `2061.04.2` are based on `2060.12`, not
`2061.04.1`.

## Feedback

Wherever we receive feedback, it is important that users include which release
they are giving feedback on.

## Celebration

A release will be a big deal. There will be some celebration and PR.
