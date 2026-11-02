# Style Guide

This is a guide to the style and voice of the textbook for writers and editors.
When several people contribute to a book, it is important that the flow of the
experience not be damaged by sudden changes in the style and voice.

This style guide will expand as we debate and codify the rules, so it is
important to have a default for undecided questions. We use
[the Google Developer Documentation Style Guide](https://developers.google.com/style/)
as our default.

For how to write the LaTeX itself (exercises, worked problems, code, figures),
see [How to Write and Edit the Workbooks](writer.md).

## Voice

Our text will have a less formal, more conversational tone than most math
textbooks. However, it will not try to be funny, like the Dummies books do.

Kontinua and the authors will be referred to as "we." The reader will be referred
to as "you." For example: "You are not expected to understand this yet, but we
will explain it in the next chapter."

The ideas we teach are complicated, so we will try to keep the prose simple. Try
for a 4th grade reading level.

We do not generally use contractions in the workbooks. While they are natural to
write, most readers (especially readers for whom English is not their first
language) find them less easy to read.

We try to use inclusive language: "The passenger checked their bag at the door"
is better than "The passenger checked his bag at the door."

We do not avoid terms and metaphors that acknowledge wrongs, whether historical
or contemporary. For example, we are OK with "The system uses master-slave
replication."

We avoid sports metaphors. Most people who use English are not American, and
sports metaphors are needlessly confusing for them.

It is OK to order the reader around: "Open a new file and save it as `foo.txt`."

Python code should be formatted as it would be by the `black` code formatter.

## Images and Plots

Keep in mind that we are trying to make these books inexpensive to produce.

People making small batches will print them on a laser printer. Keep in mind how
much toner your diagrams are consuming. Some of the printers will be black and
white, so make sure your diagram looks good in grayscale.

For companies making large batches, we want to keep the printing down to two
colors: black and SDKBlue. SDKBlue is CMYK (1.0, 0.54, 0.04, 0.19). In LaTeX it
is the color `sdkblue`.

The [Illustration Guide](illustration_guide.md) describes the colors, fonts and
conventions for drawn illustrations.

## Indexing

Please index your chapters as you go along. We typically add the `\index` tags
right after the term, or at the end of the paragraph that starts a topic.

Index entries are not capitalized unless they are proper nouns or acronyms
(*Bernoulli's principle*, *DNS*). Otherwise the index ends up with pairs like
*Pressure* and *pressure* listed separately.

```latex
A meal eaten in the middle of the day is called \newterm{lunch}. Some
people have peanut butter and jelly sandwiches for lunch.
\index{sandwich!peanut butter and jelly}
```

`\newterm` indexes the term exactly as it is printed, so use it where the term is
lowercase (not at the start of a sentence). The [writer's guide](writer.md#new-terms-and-the-index)
shows the rest of the index syntax.

## Internationalization

The build system is designed to allow the text to be customized for different
languages and locales. For example, when you are editing
`Chapters/vectors/en_US/student.tex`, you are editing the US English version of
the Vectors chapter.

In general, diagrams and other resources that might need to be
internationalized should go into that same directory.

## Page size

Once again, for cost reasons, we use the two most common paper sizes in the
world: Letter and A4. You choose one with the `Paper` setting in
`Build/user.cfg`. The text block is the same size on both. The binding is on the inside edge,
so exercises reach into the left margin, and on right-hand pages their working
space also reaches into the right margin.

We would also like to make a "tablet size," which would be smaller and have a
minimal border. The goal is a format that looks good when read on a tablet like
a 10" iPad. It does not exist yet.

## Tools

You can assume that the reader has access to a computer with:

* A text editor
* A Python 3 interpreter
* A spreadsheet program

They are expected to have these Python packages installed, which the chapters
use:

* numpy
* matplotlib
* scipy
* pandas
* sympy
* statsmodels
* PyTorch (`torch`)

If your chapter needs a package that is not on this list, say so in the chapter
and tell the student how to install it.

## TeX formatting

Please wrap your text to 80 columns. LaTeX will rewrap it, but 80 columns makes it
easy for anyone to open the file in any text editor and to review changes.

Please don't add packages or commands to the individual `.tex` files. They all go
in `Build/Support/ourbook.cls`; see the [writer's guide](writer.md#how-a-chapter-is-put-together).

If your chapter includes code, please include the source code in the chapter's
directory.
