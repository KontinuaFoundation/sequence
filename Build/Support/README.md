# Using `ourbook.cls`

`ourbook.cls` is the document class for every Kontinua workbook. It is based on
LaTeX's standard `book` class, with Kontinua's page design, exercise layout, fonts,
colors, and a large set of preloaded packages. This file explains the features a
chapter author can use. For how to install the tools and run a build, see
`Build/README.rst`.

## The basics

Each chapter lives in `Chapters/<name>/en_US/student.tex` and starts with
`\chapter{...}`. The build wraps the chapters of a volume between
`bookheader.tex` (which loads the class) and `bookfooter.tex` (which prints the
answers and the index), so a chapter file never contains `\documentclass`,
`\usepackage`, or `\begin{document}`. Everything a chapter needs must already be
loaded by the class. If you need a new package, add it to the class, not to the
chapter.

The page size is Letter unless the class gets the `a4paper` option. You do not
set it in a chapter: the build scripts add `letterpaper` or `a4paper` to the
`\documentclass` line, from the `Paper` setting in `Build/user.cfg`.

The class must be compiled with **LuaLaTeX** and `--shell-escape` (the shell
escape is for `minted`). Images and other files are looked up in the chapter's
own `en_US` folder.

Page design you get automatically:

* Chapters start on an odd (right-hand) page.
* Paragraphs are separated by a blank line's worth of space, with no indentation.
* Pages are `\raggedbottom`: extra space goes at the bottom of the page, not
  between paragraphs, lists, or equations.
* Lists (`itemize`, `enumerate`) are not indented: their labels line up with the
  surrounding text. This matters most in the narrow exercise column.
* Figures and tables are numbered within the chapter (Figure 3.2). `[H]` (from
  the `float` package) places a float exactly where it appears in the source.

## Exercises and answers

Exercises use the `exercise` package with delayed answers: every `Answer` is
collected and printed in the "Answers to Exercises" chapter at the end of the
volume.

```latex
\begin{Exercise}[title={Work Done on a Box}, label=ex:box]
A force $\vec{F} = [12, 5]$ N pushes a box whose displacement is
$\vec{d} = [3, 0]$ m. How much work is done?
\end{Exercise}
\begin{Answer}[ref=ex:box]
$W = \vec{F} \cdot \vec{d} = 36$ J.
\end{Answer}
```

* **`title`** is the exercise's name. If it contains a comma, wrap it in braces,
  as above. (Without braces, the comma ends the option.)
* **`label`** names the exercise, and **`ref`** in the `Answer` must match it
  exactly. Every exercise needs a unique label within its volume.
* The exercise text is set in the left part of the page. The right part is a
  bracketed **Working Space** for the student, closed by an **Answer on Page N**
  bracket. That page number is a link to the answer, and the answer's heading
  (Answer to Exercise N, on page M) links back.
* An exercise may break across pages if it is long.

### Making the working space taller

The working space is only as tall as the exercise text. For problems that need
room to work, add the **`space`** option:

```latex
\begin{Exercise}[title={Work Done on a Box}, label=ex:box, space=4cm]
```

This adds 4 cm of blank room below the exercise text. Any TeX length works
(`3cm`, `1.5in`, `120pt`, `0.2\textheight`), the option can go anywhere in the
list, and it affects only that one exercise. Prefer `space=` to putting
`\vspace{...}` inside the exercise text: it is easier to find and adjust later.

### Numbered parts

Inside an exercise, `\Question{...}` starts a numbered part (1., 2., ...):

```latex
\begin{Exercise}[title={Limits}, label=lim1]
Find each limit, or explain why it does not exist.
\Question{$\lim_{x \to 2} (x^2 - 1)$}
\Question{$\lim_{x \to 0} \frac{1}{x}$}
\end{Exercise}
```

An ordinary `enumerate` also works and is used more often.

## Boxes for important ideas

Key definitions, formulas, and rules go in an `important` box, a framed box in
the Kontinua blue:

```latex
\begin{mdframed}[style=important, frametitle={The Continuity Equation}]
$$A_1 v_1 = A_2 v_2$$
\end{mdframed}
```

`frametitle` is optional. Like exercise titles, a title containing a comma must
be wrapped in braces.

For the SQL chapters, the `translation` environment frames a question, its
relational algebra, and its SQL together:

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

## Theorems and definitions

The class defines `definition`, `theorem`, and `case` (with `subcase` numbered
inside it), each with an optional name:

```latex
\begin{definition}[Injection]
A function is \emph{injective} if ...
\end{definition}
```

## New terms and the index

`\newterm{word}` prints the word in italics and adds it to the index. Use it at
the place where a term is defined. For other index entries, use `\index{...}`
directly, including subentries (`\index{energy!kinetic}`) and cross-references
(`\index{ER diagram|see{entity-relationship diagram}}`).

The index is case-sensitive, so `\newterm{Memoization}` and
`\newterm{memoization}` make two separate entries. Until the proposed change
below is in place, add a lowercase `\index{...}` by hand when a term must be
capitalized at the start of a sentence. Better yet, reword so that the term
appears in lowercase.

## Code

### Code blocks

Use `minted` for code. Blocks get line numbers, a frame, a small Inconsolata
font, and automatic line wrapping:

```latex
\begin{minted}{python}
def greet(name):
    print("Hello,", name)
\end{minted}
```

The languages in use are `python`, `text` (for program output, data files, and
anything else that should not be highlighted), `html`, `c`, `cpp`, `javascript`,
`sql`, `shell`, `css`, `json`, and `bash`. Show the output of a program in a
`verbatim` or `minted{text}` block right after the code, and make sure it is the
real output.

For a short piece of code inside a sentence, use `\mintinline{python}{x = 5}`.
For a piece of code that must not be highlighted, `\verb|...|` and
`\texttt{...}` also work. Note that `\verb` cannot appear inside the argument of
another command.

### Code names in running text

Use these commands for names in sentences:

| Command | For |
|---|---|
| `\filename{two\_rooms.py}` | file and folder names |
| `\pyfunction{full\_adder}` | function names |
| `\pyvar{nand\_count}` | variable names |
| `\pytype{Graph}` | type and class names |

All four use the monospaced font, and all four let a long name **break across
lines after an underscore, a period, or a slash** (with no hyphen), so a name
like `\filename{recipe/public/style.css}` cannot run past the edge of the narrow
exercise column. Write underscores as `\_`. The commands are safe to use in
section titles: the PDF bookmark shows the plain name.

## Math

`amsmath`, `amssymb`, and `esint` (for `\oiint`) are loaded, and math is set in
the Euler fonts. Extras defined by the class:

* `\vecb{1 \\ 2 \\ 3}` makes a column vector (a `bmatrix`).
* `\boxed{...}` puts a displayed result in a box.
* `\cancel{...}` (from the `cancel` package) strikes out a term.

## Figures and diagrams

Loaded and ready to use:

* **Images:** `graphicx`, with `float` for `[H]` placement, `subcaption` for
  side-by-side subfigures, and `wrapfig` for text that wraps around a figure.
* **TikZ** with the libraries `calc`, `patterns`, `angles`, `quotes`, `graphs`,
  `graphs.standard`, `arrows.meta`, `positioning`, `fit`, and `shapes`.
* **pgfplots** (compatibility level 1.18) with the `polar` and `fillbetween`
  libraries, for graphs of functions and data.
* **tikz-3dplot** for 3D diagrams (`\tdplotsetmaincoords`).
* **circuitikz** with American symbols, for circuits and logic gates
  (`and port`, `or port`, `not port`, `nand port`, `nor port`, `xor port`).
  The styles `thick C` (an orange capacitor) and `mybattery` are predefined.
* **forest** for trees, and `algorithm` with `algpseudocode` for pseudocode.
* **Graph styles:** `kontinuaNode`, `kontinuaEdge`, and `directed` draw graph
  nodes and edges in the Kontinua style.

Draw every diagram in TikZ (or one of the TikZ-based packages above). The class
does not load PSTricks or Mermaid, and the build has no tools for them. If a diagram needs computed coordinates,
such as field lines, generate the TikZ code with a small script and keep the
script in the chapter folder, as `charge/en_US/field_lines_tikz.py` does.

## Colors

`sdkblue` is the Kontinua blue used for headings, links, and boxes. The full
palette (`sblue`, `sltblue`, `sgreen`, `syellow`, `sorange`, `sred`, `sviolet`,
and lighter and darker variants), plus `ltgray`, `veryltgray`, `dkCerulean`,
`dkCyan`, and `ltCyan`, is defined near the top of the class. Any `xcolor` name
or mix (`red!60!black`) also works.

## Fonts

| Use | Font |
|---|---|
| Body text | TeX Gyre Pagella |
| Math | Euler |
| Code | Inconsolata (straight quotes, slashed zero) |
| Headings and titles | Open Sans and Marcellus |

Pagella and Euler come with TeX Live. Inconsolata, Open Sans, and Marcellus are
Google fonts that each author installs; they are not in the repository. See
"Fonts" in `Build/README.rst`.

## Links

`hyperref` is loaded: `\ref`, `\pageref`, the table of contents, and the answer
links are clickable, and `\url{...}` and `\href{url}{text}` make web links. All
links are colored `sdkblue`.

---

## Proposed features

These three features are not in the class yet. Each section describes the
problem, a proposed design, and how the chapters could move to it.

### Index entries that do not depend on capitalization

**Problem.** `\newterm{X}` indexes `X` exactly as written. 125 of the book's 1,121
`\newterm` uses start with a capital letter, usually because the term begins a
sentence or appears in a heading. The index already has duplicate pairs such as
*Memoization / memoization*, *Pressure / pressure*, and *Binary search / binary
search*. Simply lowercasing every entry would mangle names and acronyms
(*Bernoulli*, *DNS*).

**Design.** Give `\newterm` an optional argument for the index entry:

```latex
\newterm[memoization]{Memoization}              % prints Memoization, indexes memoization
\newterm{memoization}                           % unchanged: indexes what it prints
\newterm[energy!rotational kinetic]{rotational kinetic energy}  % a subentry
```

A possible implementation:

```latex
\NewDocumentCommand\newterm{om}{%
  \textit{#2}\index{\IfNoValueTF{#1}{#2}{#1}}}
```

**Migration.** Every existing use keeps working. A short script can list the
capitalized `\newterm`s, and a person can decide for each whether it needs
`[lowercase]`. Proper nouns and acronyms stay as they are.

### Worked examples

**Problem.** Worked examples are written by hand in two styles:
`\textbf{Example}:` … `\textbf{Solution}:` (202 times in 74 chapters) and
`\textbf{Worked example.}` (89 times). They look slightly different from chapter
to chapter, an example can be separated from its solution by a page break, and
there is no way to refer to "Example 3.2".

**Design.** Add `example` and `solution` environments:

```latex
\begin{example}[A garden hose]\label{ex:hose}
A garden hose 2.0 cm across carries water at 1.5 m/s. ...
\begin{solution}
The cross-sectional area is ...
\end{solution}
\end{example}
```

* Examples are numbered within the chapter (Example 3.2), so the text can say
  "as in Example~\ref{ex:hose}".
* The heading is set in the section font and color, so examples are easy to spot
  when a student flips back through the chapter.
* The problem statement is kept on the same page as the start of its solution
  (for example, with `\needspace` or a breakable box), but a long solution may
  still break across pages.
* Examples could also be collected in a list of examples, the way the `exercise`
  package already records a list of exercises.

**Migration.** The two current patterns are regular enough for a script to
convert most of them, followed by a check of each converted chapter's PDF. The
environments can be added to the class first, with chapters converted one at a
time.

### "Before you start" and "Key ideas" boxes

**Problem.** A student who opens a chapter cannot see at a glance what it
assumes or what it will teach. The information already exists: each chapter's
`digital_resources.json` lists its prerequisites (`requires`), and each
`summary.md` has a "Key ideas" list.

**Design.** Two boxed environments in the style of the `important` box, with a
distinct color and icon:

```latex
\begin{beforeyoustart}
\item Vectors and the dot product (Vectors chapter)
\item Newton's second law (Forces and Motion chapter)
\end{beforeyoustart}

... chapter ...

\begin{keyideas}
\item Continuity: $A_1 v_1 = A_2 v_2$ for an incompressible fluid.
\item Bernoulli: faster flow at the same height means lower pressure.
\end{keyideas}
```

* `beforeyoustart` goes right after the chapter's opening hook, and `keyideas`
  goes at the end of the chapter, before the exercises.
* Both are `itemize` lists inside the box, so they use the class's unindented
  list style.

**Migration.** Two approaches, which can be combined:

1. **Generated.** A build step reads `requires` from `digital_resources.json`,
   maps each id to the chapter that `covers` it, and writes the
   `beforeyoustart` box with chapter titles (and volume numbers). The same step
   could turn the "Key ideas" list in `summary.md` into the `keyideas` box. The
   boxes then stay current as chapters move between volumes. This requires
   cleaning up the `requires` lists first: several still name topics that a
   chapter no longer uses (see the prerequisite-checker item in
   `Chapters/suggestions.md`).
2. **Hand-written.** Authors write the boxes directly in `student.tex`. This is
   simpler and allows better wording, but the boxes can drift out of date.
