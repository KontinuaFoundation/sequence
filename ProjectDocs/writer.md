# How to Write and Edit the Workbooks

This guide is for new Kontinua contributors. It covers how to get your changes
into the project, how a chapter is laid out, and the parts of our LaTeX that you
will not find in an ordinary LaTeX tutorial: our own environments and commands,
and the packages we rely on.

Related documents:

* [The Style Guide](style.md): voice, tone, indexing and page design.
* [`Build/README.rst`](../Build/README.rst): installing the tools and building
  chapters and workbooks.
* [`Build/Support/README.md`](../Build/Support/README.md): the complete reference
  for our document class, `ourbook.cls`.

## Getting your changes in

You must have a GitHub account.

If you haven't been made a collaborator, you will need to do your edits in your
own fork. Go to <https://github.com/KontinuaFoundation/sequence> and use the
**Fork** button to create one.

First, follow the instructions for cloning the repository and building the books
in [`Build/README.rst`](../Build/README.rst). Be sure to use the URL for *your*
fork when you clone.

Next, create a new branch:

```sh
git checkout -b myawesomebranch
```

Make all the edits you want (more on that below). Double-check that the chapters
you changed still build. If editing takes more than a day or two, you may want to
sync your fork so that you aren't too far out of step with everyone else. You can
do this with the **Sync fork** button on GitHub.

Commit and push what you have to your fork:

```sh
git commit -a -m 'Made the plot blue'
git push -u origin myawesomebranch
```

To make a pull request, go to the
[original repository's pull requests](https://github.com/KontinuaFoundation/sequence/pulls),
find your branch in your fork, and make a pull request from it.

Anything you put in the repository becomes property of The Kontinua Foundation,
Inc.

## Where things live

The source is in the `Chapters` directory. Each chapter has a short, unique ID,
such as `emwaves`, and its own directory.

For each workbook there is a text file, `Chapters/book_01.txt` and so on, that
lists the IDs of the chapters in that workbook, in order. `Chapters/book_00.txt`
lists every chapter of the whole sequence. The [outline](outline.md) shows every
workbook's chapters and their sections.

Inside each chapter directory there is a directory for each language (using the
ISO code). At this point, it is just `en_US`, but one day there will be more.
Inside `en_US` are:

* **`student.tex`**: the LaTeX for this chapter.
* **`digital_resources.json`**: links to videos and other digital resources the
  student would want. It also defines the dependencies of the chapter: what are
  the prerequisites? What objectives does the chapter cover? See
  [Digital Resources](digital_resources.md).
* **Images, code, and any other files the chapter uses.** These go right next to
  `student.tex`.

To see what your chapter looks like, build just that chapter. From the chapter's
`en_US` directory, run:

```sh
python3 ../../../Build/build_chapter.py
```

This makes `student.pdf` in the same directory. Building whole workbooks is
described in [`Build/README.rst`](../Build/README.rst).

## New chapters

To create a new chapter, give it a unique ID like `smells`. The
`Build/init_chapter.py` script creates the directory with a starting
`student.tex` and `digital_resources.json`:

```sh
cd Build
python3 init_chapter.py smells
```

Then add `smells` in the appropriate place in the appropriate `book_NN.txt` and in
`book_00.txt`, and add it all to the repository. If you are working on a Mac,
please don't add any `.DS_Store` files.

## Writing LaTeX for Kontinua

### How a chapter is put together

A `student.tex` is **not** a complete LaTeX document. It has no `\documentclass`,
no preamble, and no `\begin{document}`. The build scripts paste each chapter into
a larger document that uses our own class, `Build/Support/ourbook.cls`. That class
loads every package and defines every command the chapters use.

This has some consequences:

* The first line of `student.tex` should just be:

  ```latex
  \chapter{Matter and Energy}
  ```

* **Do not** put `\usepackage`, `\newcommand`, `\definecolor` or other preamble
  material in a chapter. If you need a package or a command that we don't have,
  add it to `ourbook.cls` (with a comment explaining what it is for) or ask a
  maintainer to.
* All the chapters of a workbook end up in one document, so every `\label` and
  every exercise label must be unique across the whole workbook, not just your
  chapter. Give them names that are unlikely to collide, and start each one with
  the kind of thing it labels:

  ```latex
  \label{fig:prolate_spheroid}
  \label{eq:snells_law}
  \label{tab:em_spectrum}
  ```

* We build with **LuaLaTeX**, not pdfLaTeX, and the build runs with
  `--shell-escape` (`minted` needs it). Fonts are chosen in the class with
  `fontspec`; don't change fonts in a chapter.
* Paragraphs are separated by a blank line and are not indented. You don't need
  `\noindent`, `\newpage`, `\clearpage` or hand-tuned `\vspace` to make a page
  look right. Don't use them unless you have a very good reason.
* Wrap your lines at about 80 columns. LaTeX rewraps them anyway, and short lines
  make changes easier to review.

Most of what you need is already loaded. When in doubt, look at how other
chapters do it.

### Exercises and answers

Exercises are the heart of the workbooks. We use the `exercise` package, heavily
customized in `ourbook.cls`. Every exercise is followed immediately by its
answer:

```latex
\begin{Exercise}[title={Volume of a Rugby Ball}, label=rugby_ball]
A rugby ball is about 30 cm long and has a circumference of 60 cm at
its midpoint. A cubic centimeter of lead has a mass of 11.34 grams.

How much would a solid (not hollow) lead rugby ball weigh?
\end{Exercise}
\begin{Answer}[ref=rugby_ball]
...
\end{Answer}
```

What you need to know:

* Exercises are numbered automatically. Please give every exercise a `title`. If
  the title contains a comma, wrap it in braces, as above.
* An exercise needs a `label` so its `Answer` can refer to it: the `ref` of the
  `Answer` must match the `label` of its `Exercise`. Remember that labels must be
  unique across the whole workbook.
* The answers are **not** printed where you write them. They are collected and
  printed at the back of the workbook, under "Answers to Exercises." The exercise
  gets an "Answer on Page *n*" link, and the answer gets a link back to the
  exercise.
* The question is set in a **narrow column** (a bit less than half the page
  width), pushed into the left margin so it is easy to spot. The rest of the
  width is blank *working space* for the student's pencil, marked by a "Working
  Space" line at the top and an "Answer on Page" line at the bottom. Keep
  questions short, and avoid wide tables, wide displayed equations and long lines
  of code inside an exercise. They will not fit.
* If the student needs more room to work, add the `space` option. It takes any
  TeX length and adds that much blank space below the question:

  ```latex
  \begin{Exercise}[title={Pendulum Period}, label=pend_period, space=4cm]
  ```

* For an exercise with several separate questions, an `enumerate` list is most
  common. You can also number them with `\Question`:

  ```latex
  \begin{Exercise}[title={Adding Polynomials Practice}, label=addpns]
  Add the following polynomials:
  \Question{$2x^3 - 5x^2 + 3x - 9$ and $x^3 - 2x^2 - 2x - 9$}
  \Question{$3x^5 - 5x^3 + 3x^2 - x - 3$ and $2x^4 - 2x^3 - 2x^2 + x - 9$}
  \end{Exercise}
  ```

* `minted` code blocks and `\verb` work inside both `Exercise` and `Answer`.

### Worked problems

Before you ask the student to do something, you will often want to show them
how. A worked problem shows a problem and its full solution together, in a thin
blue box numbered within the chapter ("Worked Problem 3"):

```latex
\begin{Worked}
\begin{Problem}
A Wi-Fi signal has frequency $2.4$ GHz. What is its wavelength?
\end{Problem}
\begin{Solution}
$\lambda = \frac{3.0 \times 10^8}{2.4 \times 10^9} = 0.125$ m,
or $12.5$ cm. That is why Wi-Fi antennas are a few centimeters long.
\end{Solution}
\end{Worked}
```

* You can give a worked problem a title. It prints as "Worked Problem 3: A gear
  train":

  ```latex
  \begin{Worked}[A gear train]
  ```

* Every `Worked` needs both a `Problem` and a `Solution`, in that order. A line
  divides them in the box.
* Unlike an exercise answer, the solution is printed right there, in the box.
  Don't put a `Worked` inside an `Exercise` or an `Answer`.
* The box can break across pages. Anything can go inside it: displayed math,
  lists, figures, `minted` code and `\verb`.
* Please don't write worked problems by hand with `\textbf{Example}` and
  `\textbf{Solution}` labels. Use `Worked` so they all look alike.

### Highlighted boxes and key ideas

To set off an important formula, a definition or a summary, use `mdframed` with
our `important` style (a thin blue frame). Give it a title with `frametitle`:

```latex
\begin{mdframed}[style=important, frametitle={Volume of a Sphere}]
A sphere of radius $r$ has volume $V = \frac{4}{3}\pi r^3$.
\end{mdframed}
```

Some chapters end with a summary box in exactly this form:

```latex
\begin{mdframed}[style=important, frametitle={Key Ideas}]
\begin{itemize}
\item ...
\item ...
\end{itemize}
\end{mdframed}
```

A few chapters use the `amsthm` environments `definition`, `theorem`, `case` and
`subcase`. They work, but a titled `mdframed` box is more common.

### New terms and the index

Every workbook has an index, made with `imakeidx`. Please index generously: when
you introduce or explain an important idea, index it. The
[Style Guide](style.md#indexing) says how to word index entries.

When you introduce a new term, use `\newterm`. It puts the term in italics *and*
adds it to the index:

```latex
An object that is not accelerating is in \newterm{equilibrium}.
```

`\newterm` indexes the word exactly as you typed it, so if the term starts a
sentence and is capitalized, add a separate lowercase `\index` entry instead of
relying on `\newterm`.

For anything else, use `\index`. Put it right after the word it refers to, with
no space before it, or at the end of the paragraph that introduces the topic. The
usual `makeindex` syntax applies:

```latex
\index{wavelength}                       % a plain entry
\index{polynomial!adding}                % a sub-entry, under "polynomial"
\index{SHM|see{simple harmonic motion}}  % a cross-reference
\index{elementary charge|seealso{coulomb}}
\index{Bezout's identity@B\'ezout's identity}  % sort as one thing, print as another
```

### Computer code

We use the `minted` package, which colors code with Pygments. **Use `minted` for
all code**, and always name the language:

```latex
\begin{minted}{python}
def wavelength(f):
    return 3.0e8 / f   # meters
\end{minted}
```

The languages we use most are `python`, `text` (for program output), `html`,
`c`, `cpp`, `javascript`, `sql`, `shell` and `css`. Code blocks automatically get line
numbers and a vertical line along their left side. Python code should be formatted as the `black` code
formatter would format it.

For a little code in the middle of a sentence, use `\mintinline`:

```latex
The \mintinline{python}{range(1, 5)} function stops before 5.
```

When you name something from a program in a sentence, use one of these commands
instead of `\texttt`:

| Command | For |
| --- | --- |
| `\pyfunction{average}` | a function or method |
| `\pyvar{total_count}` | a variable |
| `\pytype{dict}` | a type or class |
| `\filename{two\_rooms.py}` | a file or directory name |

They all print in the monospaced font, but unlike `\texttt` they can break across
lines after an underscore, a period or a slash. That matters in the narrow
exercise column, where a long name would otherwise run into the working space.
Write underscores as `\_` inside them.

For explaining SQL queries, the database chapters use the `translation` box,
which shows a request in English, the relational algebra and the SQL:

```latex
\begin{translation}
\request{Which labs have no equipment?}
\algebra{\pi_{\text{Loc}}(\text{Location}) - \pi_{\text{Loc}}(\text{Equipment})}
\sqlrow
\begin{minted}{sql}
SELECT ...
\end{minted}
\end{translation}
```

For pseudocode, the `algorithm` and `algpseudocode` packages are loaded.

Code the student is meant to run should also be saved as a file in the chapter's
directory and listed in `digital_resources.json`. Code should be in Python,
unless the chapter is about another language (the data structures chapters use C
and C++, and the web chapters use HTML, CSS and JavaScript).

### Math

`amsmath`, `amssymb` and `amsthm` are loaded, so `align`, `equation*`, `bmatrix`
and the rest are all available. Many chapters use `$$ ... $$` for displayed
equations; `\[ ... \]` works too.

A few extras:

| Command | What it does |
| --- | --- |
| `\vecb{1 \\ 2 \\ 3}` | a column vector (shorthand for a `bmatrix`) |
| `\boxed{...}` | a displayed result in a box |
| `\cancel{x}` | a strike-through, for showing cancellation (`cancel` package) |
| `\oiint` | a closed surface integral (`esint` package) |

### Figures and diagrams

We would rather draw diagrams in LaTeX than paste in pictures, because they are
much easier to maintain. These drawing packages are loaded:

* `tikz`, with the `calc`, `patterns`, `angles`, `quotes`, `graphs`,
  `arrows.meta`, `positioning` and `fit` libraries
* `pgfplots` for graphs of functions and data, with the `polar` and
  `fillbetween` libraries
* `circuitikz` for circuit diagrams
* `tikz-3dplot` for 3-D drawings
* `tkz-euclide` for geometric constructions
* `forest` for trees

For graphs in the computer science chapters (nodes and edges), use the
`kontinuaNode`, `kontinuaEdge` and `directed` TikZ styles so they all look alike.
[Mathcha](https://www.mathcha.io/editor) can help you draw a detailed TikZ
picture.

Every figure, whether TikZ or an image, should be in a `figure` environment with
a caption and a label. We use the `[H]` placement from the `float` package, which
puts the figure exactly where it appears in the source:

```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth]{ghgEffect.png}
\caption{The greenhouse effect.}
\label{fig:greenhouse}
\end{figure}
```

`subcaption` (for side-by-side figures) and `wrapfig` (for a small figure with
text flowing around it) are also loaded.

#### Images

Images should be PNG. Put them in the same directory as the `student.tex` that
uses them, and refer to them by file name alone, as above.

If you use another application to create the image, please include the original
source too (for example, an Illustrator `.ai` file or an OmniGraffle `.graffle`
file). The [Illustration Guide](illustration_guide.md) describes the look of our
illustrations.

#### Color

The workbooks are printed in two colors: black and our blue, `sdkblue`. Some
will be printed on black-and-white laser printers. So stick to black, gray and
`sdkblue` (the class also defines lighter and darker shades, such as `sltblue`
and `dkblu`), make sure your diagram still reads in grayscale, and go easy on the
toner. The [Style Guide](style.md#images-and-plots) has more about this.

### Links

`hyperref` is loaded, so cross-references and page numbers are clickable in the
PDF. For web addresses, use `\url{https://...}`, or
`\href{https://...}{link text}` when you want the link to have its own words.
