==========
To-Do List
==========

If you want to volunteer, here are some things we really need done.

=======
Writing
=======

You can look through the book and find something missing, interesting, and useful.  If you
suggest it and volunteer to write it, we will probably OK it.

That said, here are some topics that definitely need to be tackled:

* Magnetism and Induction
* Angular momentum and gyroscopic forces
* How colors separate when refracted, rainbows, and chromatic aberration
* Simple linear regression and residuals
* How a transistor works
* Weather (why is there wind? What is a high-pressure system? Why does it rain?)

Certain chapters need "splitting-apart" as it covers topics that should come after, and other chapters need merging as there is duplicate information.

=================
Digital Resources
=================

Every chapter needs a ``digital_resources.json`` file. Most of them
don't have one. This involves reading the chapter, browsing the web for relevant videos and resources, and putting htem in the ``digital_resources.json`` file for that chapter using the editor app.  You need to have a Mac to run the editor.

More info: `Digital Resources
<https://github.com/KontinuaFoundation/sequence/blob/master/ProjectDocs/digital_resources.rst>`_.


======================
Problems and Solutions
======================

Every chapter needs at least six practice problems and six test problems.

The practice problems and solutions go into the appropriate ``student.tex``.

The test problems will be entered into the mentoris web application.
Besides a problem and a solution, the test problems will also need a grading rubric. 

(This is being worked on for supplemental quizzes, but the book problems could use more in-chapter examples!)

========
Indexing and Figures
========

I have neglected adding index tags in many chapters.  I would love someone to go through and add the tags.

Overall, you just go through the ``student.tex`` files.  Anywhere an idea is introduced at ``\index{peanut butter}``
or ``\index{butters!peanut}``

Additionally, all figures (TikZ pictures or inserted images or diagrams) should have the format of a LaTeX figure for consistency::


    \begin{figure}[htbp]
        \centering
        \includegraphics[width=0.8\textwidth]{example.png}
        \caption{Your descriptive caption here.}
        \label{fig:example}
    \end{figure}


=======
Editing
=======

Everything written so far is first draft quality.  I need an editor to read it and make it better. (Editor's note: He's working on it!)

============
Fund-raising
============

Thus far, I have done a poor job raising funds.  I'd really like to
hire a full-time writer, but we need a healthy endowment first.

Even if it is just asking your rich friends to write a check, I'd sure appreciate the
help.
