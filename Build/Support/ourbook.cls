%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Version Feb 17, 2024
%% Previous Version: Nov 8, 2020

%% Ourbook.cls, modification of book.cls, by 
%% Amy Hendrickson, TeXnology Inc, 
%% www.texnology.com
%%
%% amyh@texnology.com
%%
%% for books published by Aaron Hillegass, charmedliferaft@gmail.com

%% Additions to code found beneath this line:
%% Changes and additions for Aaron Hillegass
%%
%% Additional code in this package found in preamble.tex and bookfooter.tex
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% This is file `ourbook.cls', based on LaTeX standard book.cls
%% generated with the docstrip utility.
%%
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}

\ProvidesClass{ourbook}
              [2020/10/28, based on
 Standard LaTeX document book class]
\newcommand\@ptsize{}
\newif\if@restonecol
\newif\if@titlepage
\@titlepagetrue
\newif\if@openright
\newif\if@mainmatter \@mainmattertrue
\if@compatibility\else
\DeclareOption{a4paper}
   {\setlength\paperheight {297mm}%
    \setlength\paperwidth  {210mm}}
\DeclareOption{a5paper}
   {\setlength\paperheight {210mm}%
    \setlength\paperwidth  {148mm}}
\DeclareOption{b5paper}
   {\setlength\paperheight {250mm}%
    \setlength\paperwidth  {176mm}}
\DeclareOption{letterpaper}
   {\setlength\paperheight {11in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{legalpaper}
   {\setlength\paperheight {14in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{executivepaper}
   {\setlength\paperheight {10.5in}%
    \setlength\paperwidth  {7.25in}}
\newif\iflandscape
\DeclareOption{landscape}
   {\global\landscapetrue
\setlength\@tempdima   {11in}%
    \setlength\paperheight {8.5in}%
    \setlength\paperwidth  {\@tempdima}}%
\fi
\if@compatibility
  \renewcommand\@ptsize{0}
\else
\DeclareOption{10pt}{\renewcommand\@ptsize{0}}
\fi
\DeclareOption{11pt}{\renewcommand\@ptsize{1}}
\DeclareOption{12pt}{\renewcommand\@ptsize{2}}
\if@compatibility\else
\DeclareOption{oneside}{\@twosidefalse \@mparswitchfalse}
\fi
\DeclareOption{twoside}{\@twosidetrue  \@mparswitchtrue}
\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\if@compatibility\else
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\fi
\DeclareOption{titlepage}{\@titlepagetrue}
\if@compatibility\else
\DeclareOption{notitlepage}{\@titlepagefalse}
\fi
\if@compatibility
\@openrighttrue
\else
\DeclareOption{openright}{\@openrighttrue}
\DeclareOption{openany}{\@openrightfalse}
\fi
\if@compatibility\else
\DeclareOption{onecolumn}{\@twocolumnfalse}
\fi
\DeclareOption{twocolumn}{\@twocolumntrue}
\DeclareOption{leqno}{\input{leqno.clo}}
\DeclareOption{fleqn}{\input{fleqn.clo}}
\DeclareOption{openbib}{%
  \AtEndOfPackage{%
   \renewcommand\@openbib@code{%
      \advance\leftmargin\bibindent
      \itemindent -\bibindent
      \listparindent \itemindent
      \parsep \z@
      }%
   \renewcommand\newblock{\par}}%
}

\ExecuteOptions{letterpaper,10pt,twoside,onecolumn,final,openright}
\ProcessOptions
\input{bk1\@ptsize.clo}


\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}
\setlength\parskip{0\p@ \@plus \p@}
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301
\setcounter{topnumber}{2}
\renewcommand\topfraction{.7}
\setcounter{bottomnumber}{1}
\renewcommand\bottomfraction{.3}
\setcounter{totalnumber}{3}
\renewcommand\textfraction{.2}
\renewcommand\floatpagefraction{.5}
\setcounter{dbltopnumber}{2}
\renewcommand\dbltopfraction{.7}
\renewcommand\dblfloatpagefraction{.5}
\if@twoside
  \def\ps@headings{%
      \let\@oddfoot\@empty\let\@evenfoot\@empty
      \def\@evenhead{\unskip\thepage\hfil\slshape\leftmark}%
      \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
      \let\@mkboth\markboth
    \def\chaptermark##1{%
      \markboth {\MakeUppercase{%
        \ifnum \c@secnumdepth >\m@ne
          \if@mainmatter
            \@chapapp\ \thechapter. \ %
          \fi
        \fi
        ##1}}{}}%
    \def\sectionmark##1{%
      \markright {\MakeUppercase{%
        \ifnum \c@secnumdepth >\z@
          \thesection. \ %
        \fi
        ##1}}}}
\else
  \def\ps@headings{%
    \let\@oddfoot\@empty
    \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
    \let\@mkboth\markboth
    \def\chaptermark##1{%
      \markright {\MakeUppercase{%
        \ifnum \c@secnumdepth >\m@ne
          \if@mainmatter
            \@chapapp\ \thechapter. \ %
          \fi
        \fi
        ##1}}}}
\fi
\def\ps@myheadings{%
    \let\@oddfoot\@empty\let\@evenfoot\@empty
    \def\@evenhead{\thepage\hfil\slshape\leftmark}%
    \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
    \let\@mkboth\@gobbletwo
    \let\chaptermark\@gobble
    \let\sectionmark\@gobble
    }
  \if@titlepage
  \newcommand\maketitle{\begin{titlepage}%
  \let\footnotesize\small
  \let\footnoterule\relax
  \let \footnote \thanks
  \null\vfil
  \vskip 60\p@
  \begin{center}%
    {\LARGE \@title \par}%
    \vskip 3em%
    {\large
     \lineskip .75em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
      \vskip 1.5em%
    {\large \@date \par}%       % Set date in \large size.
  \end{center}\par
  \@thanks
  \vfil\null
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}
\else
\newcommand\maketitle{\par
  \begingroup
    \renewcommand\thefootnote{\@fnsymbol\c@footnote}%
    \def\@makefnmark{\rlap{\@textsuperscript{\normalfont\@thefnmark}}}%
    \long\def\@makefntext##1{\parindent 1em\noindent
            \hb@xt@1.8em{%
                \hss\@textsuperscript{\normalfont\@thefnmark}}##1}%
    \if@twocolumn
      \ifnum \col@number=\@ne
        \@maketitle
      \else
        \twocolumn[\@maketitle]%
      \fi
    \else
      \newpage
      \global\@topnum\z@   % Prevents figures from going at top of page.
      \@maketitle
    \fi
    \thispagestyle{plain}\@thanks
  \endgroup
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}
\def\@maketitle{%
  \newpage
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\LARGE \@title \par}%
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
    \vskip 1em%
    {\large \@date}%
  \end{center}%
  \par
  \vskip 1.5em}
\fi
\newcommand*\chaptermark[1]{}
\setcounter{secnumdepth}{2}
\newcounter {part}
\newcounter {chapter}
\newcounter {section}[chapter]
\newcounter {subsection}[section]
\newcounter {subsubsection}[subsection]
\newcounter {paragraph}[subsubsection]
\newcounter {subparagraph}[paragraph]
\renewcommand \thepart {\@Roman\c@part}
\renewcommand \thechapter {\@arabic\c@chapter}
\renewcommand \thesection {\thechapter.\@arabic\c@section}
\renewcommand\thesubsection   {\thesection.\@arabic\c@subsection}
\renewcommand\thesubsubsection{\thesubsection .\@arabic\c@subsubsection}
\renewcommand\theparagraph    {\thesubsubsection.\@arabic\c@paragraph}
\renewcommand\thesubparagraph {\theparagraph.\@arabic\c@subparagraph}
\newcommand\@chapapp{\chaptername}
\newcommand\frontmatter{%
    \cleardoublepage
  \@mainmatterfalse
  \pagenumbering{roman}}
\newcommand\mainmatter{%
    \cleardoublepage
  \@mainmattertrue
  \pagenumbering{arabic}}
\newcommand\backmatter{%
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
  \@mainmatterfalse}

\newcommand\part{%
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
  \thispagestyle{plain}%
  \if@twocolumn
    \onecolumn
    \@tempswatrue
  \else
    \@tempswafalse
  \fi
  \null\vfil
  \secdef\@part\@spart}

\def\@part[#1]#2{%
    \ifnum \c@secnumdepth >-2\relax
      \refstepcounter{part}%
      \addcontentsline{toc}{part}{\thepart\hspace{1em}#1}%
    \else
      \addcontentsline{toc}{part}{#1}%
    \fi
    \markboth{}{}%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >-2\relax
       \huge\bfseries \partname~\thepart
       \par
       \vskip 20\p@
     \fi
     \Huge \bfseries #2\par}%
    \@endpart}
\def\@spart#1{%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \Huge \bfseries #1\par}%
    \@endpart}
\def\@endpart{\vfil\newpage
              \if@twoside
               \if@openright
                \null
                \thispagestyle{empty}%
                \newpage
               \fi
              \fi
              \if@tempswa
                \twocolumn
              \fi}

\newcommand\chapter{\if@openright\cleardoublepage\else\clearpage\fi
                    \thispagestyle{plain}%
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
                       \if@mainmatter
                         \refstepcounter{chapter}%
                         \typeout{\@chapapp\space\thechapter.}%
                         \addcontentsline{toc}{chapter}%
                                   {\protect\numberline{\thechapter}#1}%
                       \else
                         \addcontentsline{toc}{chapter}{#1}%
                       \fi
                    \else
                      \addcontentsline{toc}{chapter}{#1}%
                    \fi
                    \chaptermark{#1}%
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@topnewpage[\@makechapterhead{#2}]%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}





\def\@schapter#1{\if@twocolumn
                   \@topnewpage[\@makeschapterhead{#1}]%
                 \else
                   \@makeschapterhead{#1}%
                   \@afterheading
                 \fi}
\def\@makeschapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \raggedright
    \normalfont
    \interlinepenalty\@M
    \Huge \bfseries  #1\par\nobreak
    \vskip 40\p@
  }}

\newcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
                                   {2.3ex \@plus.2ex}%
                                   {\color{sdkblue}\sectionfont%\normalfont\Large\bfseries
}}
\newcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\large\bfseries}}
\newcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\normalsize\bfseries}}
\newcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {3.25ex \@plus1ex \@minus.2ex}%
                                    {-1em}%
                                    {\normalfont\normalsize\bfseries}}
\newcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
                                       {3.25ex \@plus1ex \@minus .2ex}%
                                       {-1em}%
                                      {\normalfont\normalsize\bfseries}}
\if@twocolumn
  \setlength\leftmargini  {2em}
\else
  \setlength\leftmargini  {2.5em}
\fi
\leftmargin  \leftmargini
\setlength\leftmarginii  {2.2em}
\setlength\leftmarginiii {1.87em}
\setlength\leftmarginiv  {1.7em}
\if@twocolumn
  \setlength\leftmarginv  {.5em}
  \setlength\leftmarginvi {.5em}
\else
  \setlength\leftmarginv  {1em}
  \setlength\leftmarginvi {1em}
\fi
\setlength  \labelsep  {.5em}
\setlength  \labelwidth{\leftmargini}
\addtolength\labelwidth{-\labelsep}
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
\renewcommand\theenumi{\@arabic\c@enumi}
\renewcommand\theenumii{\@alph\c@enumii}
\renewcommand\theenumiii{\@roman\c@enumiii}
\renewcommand\theenumiv{\@Alph\c@enumiv}
\newcommand\labelenumi{\theenumi.}
\newcommand\labelenumii{(\theenumii)}
\newcommand\labelenumiii{\theenumiii.}
\newcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\theenumi(\theenumii)}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
\newcommand\labelitemi{\textbullet}
\newcommand\labelitemii{\normalfont\bfseries \textendash}
\newcommand\labelitemiii{\textasteriskcentered}
\newcommand\labelitemiv{\textperiodcentered}
\newenvironment{description}
               {\list{}{\labelwidth\z@ \itemindent-\leftmargin
                        \let\makelabel\descriptionlabel}}
               {\endlist}
\newcommand*\descriptionlabel[1]{\hspace\labelsep
                                \normalfont\bfseries #1}
\newenvironment{verse}
               {\let\\\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -1.5em%
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin 1.5em}%
                \item\relax}
               {\endlist}
\newenvironment{quotation}
               {\list{}{\listparindent 1.5em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \item\relax}
               {\endlist}
\newenvironment{quote}
               {\list{}{\rightmargin\leftmargin}%
                \item\relax}
               {\endlist}
\if@compatibility
\newenvironment{titlepage}
    {%
      \cleardoublepage
      \if@twocolumn
        \@restonecoltrue\onecolumn
      \else
        \@restonecolfalse\newpage
      \fi
      \thispagestyle{empty}%
      \setcounter{page}\z@
    }%
    {\if@restonecol\twocolumn \else \newpage \fi
    }
\else
\newenvironment{titlepage}
    {%
      \cleardoublepage
      \if@twocolumn
        \@restonecoltrue\onecolumn
      \else
        \@restonecolfalse\newpage
      \fi
      \thispagestyle{empty}%
      \setcounter{page}\@ne
    }%
    {\if@restonecol\twocolumn \else \newpage \fi
     \if@twoside\else
        \setcounter{page}\@ne
     \fi
    }
\fi
\newcommand\appendix{\par
  \setcounter{chapter}{0}%
  \setcounter{section}{0}%
  \gdef\@chapapp{\appendixname}%
  \gdef\thechapter{\@Alph\c@chapter}}
\setlength\arraycolsep{5\p@}
\setlength\tabcolsep{6\p@}
\setlength\arrayrulewidth{.4\p@}
\setlength\doublerulesep{2\p@}
\setlength\tabbingsep{\labelsep}
\skip\@mpfootins = \skip\footins
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}
\@addtoreset {equation}{chapter}
\renewcommand\theequation
  {\ifnum \c@chapter>\z@ \thechapter.\fi \@arabic\c@equation}
\newcounter{figure}[chapter]
\renewcommand \thefigure
     {\ifnum \c@chapter>\z@ \thechapter.\fi \@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurename~\thefigure}
\newenvironment{figure}
               {\@float{figure}}
               {\end@float}
\newenvironment{figure*}
               {\@dblfloat{figure}}
               {\end@dblfloat}
\newcounter{table}[chapter]
\renewcommand \thetable
     {\ifnum \c@chapter>\z@ \thechapter.\fi \@arabic\c@table}
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\fnum@table{\tablename~\thetable}
\newenvironment{table}
               {\@float{table}}
               {\end@float}
\newenvironment{table*}
               {\@dblfloat{table}}
               {\end@dblfloat}
\newlength\abovecaptionskip
\newlength\belowcaptionskip
\setlength\abovecaptionskip{10\p@}
\setlength\belowcaptionskip{0\p@}

\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{#1: #2}%
  \ifdim \wd\@tempboxa >\hsize
    #1: #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareRobustCommand*\cal{\@fontswitch\relax\mathcal}
\DeclareRobustCommand*\mit{\@fontswitch\relax\mathnormal}
\newcommand\@pnumwidth{1.55em}
\newcommand\@tocrmarg{2.55em}
\newcommand\@dotsep{4.5}
\setcounter{tocdepth}{2}
\newcommand\tableofcontents{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\contentsname
        \@mkboth{%
           \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}%
    \@starttoc{toc}%
    \if@restonecol\twocolumn\fi
    }
\newcommand*\l@part[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{2.25em \@plus\p@}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      {\leavevmode
       \large \bfseries #1\hfil \hb@xt@\@pnumwidth{\hss #2}}\par
       \nobreak
         \global\@nobreaktrue
         \everypar{\global\@nobreakfalse\everypar{}}%
    \endgroup
  \fi}
\newcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1.0em \@plus\p@
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode \bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}
\newcommand*\l@section{\@dottedtocline{1}{1.5em}{2.3em}}
\newcommand*\l@subsection{\@dottedtocline{2}{2em}{3.2em}}
\newcommand*\l@subsubsection{\@dottedtocline{3}{7.0em}{4.1em}}
\newcommand*\l@paragraph{\@dottedtocline{4}{10em}{5em}}
\newcommand*\l@subparagraph{\@dottedtocline{5}{12em}{6em}}
\newcommand\listoffigures{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listfigurename
      \@mkboth{\MakeUppercase\listfigurename}%
              {\MakeUppercase\listfigurename}}%
    \@starttoc{lof}%
    \if@restonecol\twocolumn\fi
    }
\newcommand*\l@figure{\@dottedtocline{1}{1.5em}{2.3em}}
\newcommand\listoftables{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listtablename
      \@mkboth{%
          \MakeUppercase\listtablename}{\MakeUppercase\listtablename}}%
    \@starttoc{lot}%
    \if@restonecol\twocolumn\fi
    }
\let\l@table\l@figure

\newdimen\bibindent
\setlength\bibindent{1.5em}
\newenvironment{thebibliography}[1]
     {\chapter*{\bibname
        \@mkboth{\bibname}{\bibname}}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\newcommand\newblock{\hskip .11em\@plus.33em\@minus.07em}
\let\@openbib@code\@empty
\newenvironment{theindex}
               {\if@twocolumn
                  \@restonecolfalse
                \else
                  \@restonecoltrue
                \fi
                \columnseprule \z@
                \columnsep 35\p@
                \twocolumn[\@makeschapterhead{\indexname}]%
                \@mkboth{\MakeUppercase\indexname}%
                        {\MakeUppercase\indexname}%
                \thispagestyle{plain}\parindent\z@
                \parskip\z@ \@plus .3\p@\relax
                \let\item\@idxitem}
               {\if@restonecol\onecolumn\else\clearpage\fi}
\newcommand\@idxitem{\par\hangindent 40\p@}
\newcommand\subitem{\@idxitem \hspace*{20\p@}}
\newcommand\subsubitem{\@idxitem \hspace*{30\p@}}
\newcommand\indexspace{\par \vskip 10\p@ \@plus5\p@ \@minus3\p@\relax}
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule\@width.4\columnwidth
  \kern2.6\p@}
\@addtoreset{footnote}{chapter}
\newcommand\@makefntext[1]{%
    \parindent 1em%
    \noindent
    \hb@xt@1.8em{\hss\@makefnmark}#1}
\newcommand\contentsname{Contents}
\newcommand\listfigurename{List of Figures}
\newcommand\listtablename{List of Tables}
\newcommand\bibname{Bibliography}
\newcommand\indexname{Index}
\newcommand\figurename{Figure}
\newcommand\tablename{Table}
\newcommand\partname{Part}
\newcommand\chaptername{Chapter}
\newcommand\appendixname{Appendix}
\def\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
\setlength\columnsep{10\p@}
\setlength\columnseprule{0\p@}
\pagestyle{headings}
\pagenumbering{arabic}
\if@twoside
\else
  \raggedbottom
\fi
\if@twocolumn
  \twocolumn
  \sloppy
  \flushbottom
\else
  \onecolumn
\fi

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Changes and additions for Aaron Hillegass:

\def\startonoddpage{\clearpage\ifodd\c@page\else\null\thispagestyle{empty}\newpage\fi}
\renewcommand\chapter{\startonoddpage
                    \thispagestyle{plain}%
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}

\def\@makechapterhead#1{%
\iflandscape\vglue-84pt\else\vglue-18pt\vglue-54pt\fi
  {\parindent \z@ \raggedright \normalfont
    \ifnum \c@secnumdepth >\m@ne
\color{sdkblue}
      \if@mainmatter
        \huge\chapternumfont \@chapapp
\space 
\thechapter
        \vskip 6pt
      \fi
    \fi
\hrule height 1.5pt
    \interlinepenalty\@M
    \Huge \chapternamefont #1\par\nobreak
\vskip-4pt}\vskip 40\p@}


\def\@makeschapterhead#1{%
\iflandscape\vglue-1in\else\vspace*{36pt}\fi
\noindent
\vskip-\parskip
\vskip8pt
\vskip24pt
\vtop{
{\fboxsep=0pt
\fboxrule=1.5pt
\fcolorbox{sdkblue}{white}{
\includegraphics
[width=1in]{../Support/color_spiral.pdf}}}
\vskip12pt
  {%\color{ForestGreen}
\color{sdkblue}
\parskip=0pt
\parindent \z@ \raggedright \normalfont
\hrule height 1.5pt
%    \interlinepenalty\@M
%\color{ForestGreen}
\color{sdkblue}
    \schapterfont
\vrule height 36pt width0pt\relax#1\par\nobreak
\vskip-4pt}}
    \vskip 40\p@
  }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Graphics

\usepackage{graphicx}
\usepackage{float}
\usepackage{tikz}
\usepackage{tkz-euclide}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{calc,patterns,angles,quotes}
\usepackage[american]{circuitikz}
\usepackage{tikz-3dplot}
\usepackage{cancel}
\usepackage{wrapfig}
\usepackage{listings}

\usepackage{mdframed}
\mdfsetup{skipabove=\topskip,skipbelow=\topskip}
\global\mdfdefinestyle{important}{%
  linecolor=sdkblue,linewidth=1pt % leftmargin=1cm,rightmargin=1cm
}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Colors

\usepackage{xcolor}
\definecolor{ltblue}{cmyk}{.1,0,0,0}

%% for tabs and page color
\definecolor{blu}{cmyk}{.75,.48,0,0}
\definecolor{dkblu}{cmyk}{.95,.78,0,0}

%%%% Colors specified by TUM
%% colors from swatches, all start with `s'

\definecolor{sviolet}{cmyk}{.5,1,0,.4}
\definecolor{svioletblue}{cmyk}{1,1,0,.4}
\definecolor{sltvioletblue}{cmyk}{.85,.85,0,.4}
\definecolor{sblueblack}{cmyk}{1,.57,.12,.7}
\definecolor{sdkblue}{cmyk}{1,.54,.04,.19}
\definecolor{sblue}{cmyk}{.9,.48,0,0}
\definecolor{sltblue}{cmyk}{.65,.19,.01,.04}
\definecolor{sveryltblue}{cmyk}{.42,.09,0,0}
\definecolor{slightblue}{cmyk}{.32,.06,0,0}
\definecolor{sbluegreen}{cmyk}{1,.03,.3,.3}
\definecolor{sgreen}{cmyk}{1,0,1,.2}
\definecolor{syellowgreen}{cmyk}{.6,0,1,.2}
\definecolor{sltyellowgreen}{cmyk}{.35,0,1,.2}
\definecolor{screamywhite}{cmyk}{.03,.04,.14,.08}
\definecolor{syellow}{cmyk}{0,.1,1,0}
\definecolor{sltyellow}{cmyk}{0,.1,.8,0}
\definecolor{sveryltyellow}{cmyk}{0,.1,.3,0}
\definecolor{syelloworange}{cmyk}{0,.3,1,0}
\definecolor{sorange}{cmyk}{0,.65,.95,0}
\definecolor{sorangered}{cmyk}{0,.80,1,0}
\definecolor{sred}{cmyk}{.1,1,1,.1}
\definecolor{sredviolet}{cmyk}{0,1,1,.4}

% for tables?
%\rowcolors{2}{white}{slightblue}

\definecolor{shadecolor}{cmyk}{0,0,0,.12}
\definecolor{ltgray}{cmyk}{0,0,0,.6}
\definecolor{veryltgray}{cmyk}{0,0,0,.4}
\definecolor{gray75}{gray}{0.75}
\definecolor{dkCerulean}{cmyk}{.94,0.11,0,.2}
\definecolor{dkCyan}{cmyk}{.94,0,0,.3}
\definecolor{ltCyan}{cmyk}{.64,0,0,0}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Fonts

%% If wanted, makes more graceful math fonts:
\usepackage{euler}

\usepackage{fontspec}

%%% Set Main Text Font
\setmainfont{TeX Gyre Pagella}[Ligatures=TeX, WordSpace=1.2]
%\setmainfont{TimesNewRomanMTStd}[Ligatures=TeX, WordSpace=1.2]

%% Special Use Fonts
%%% Running heads
\def\runningheadfont{\fontsize{12}{0}%
\fontspec{MarcellusSC-Regular.ttf}[Ligatures=TeX]
\addfontfeature{LetterSpace=6.0}
%\color{ltgray}
}

\def\runningheadchapfont{\fontsize{10}{0}%
%\fontspec{MarcellusSC-Regular.ttf}}
\fontspec{OpenSans-Regular}[Ligatures=TeX]
\addfontfeature{LetterSpace=3.0}
%\color{ltgray}
}

\def\foliofont{\fontsize{12}{0}%
\fontspec{OpenSans-SemiBold}}

\def\schapterfont{\fontsize{32}{0}%
\fontspec{MarcellusSC-Regular.ttf}[Ligatures=TeX]}

\def\chapnamefont{\fontsize{20}{72}%
\fontspec{Marcellus-Regular.ttf}[Ligatures=TeX]}

%% tried chapnumfont and chaptitlefont 
%% with OpenSans but the effect was Boring!
\def\chapnumfont{\fontsize{40}{72}%
\fontspec{Marcellus-Regular.ttf}[Ligatures=TeX]
}

\def\chaptitlefont{\fontsize{36}{45}%
\fontspec{Marcellus-Regular.ttf}[Ligatures=TeX]}

%%%%%%%%%%%%%%%%%%%%%%
%% Section fonts
\def\sectionfont{\fontsize{13}{15}%
\fontspec{OpenSans-Bold}[Ligatures=TeX]
\color{sdkblue}}

\def\subsectionfont{\fontsize{11}{14}%
\fontspec{OpenSans-Bold}[Ligatures=TeX]%
\color{sdkblue}}
%%%%%%%%%%%%%%%%%%%%%%

\def\exercisenamefont{\fontsize{12}{14}%
\fontspec{OpenSans-BoldItalic}[Ligatures=TeX]%
\color{sdkblue}}

\def\exercisetitlefont{\fontsize{15}{16}%
\fontspec{OpenSans-Bold}[Ligatures=TeX]%
\color{sdkblue}}

\def\answertitlefont{\fontsize{14}{16}%
\fontspec{OpenSans-Bold}[Ligatures=TeX]%
\color{sdkblue}}

%\def\chapternumfont{\fontsize{16}{45}%
\def\chapternumfont{\fontsize{18}{45}%
\fontspec{MarcellusSC-Regular.ttf}[Ligatures=TeX]}

\def\chapternamefont{\fontsize{30}{36}% was 36
\fontspec{Marcellus-Regular.ttf}[Ligatures=TeX]}

%% Part fonts
\def\partnamefont{\fontsize{20}{30}%
\fontspec{MarcellusSC-Regular.ttf}[Ligatures=TeX]}

\def\partnumfont{\fontsize{20}{20}%
\fontspec{MarcellusSC-Regular.ttf}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Section heads
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
                                   {3pt%2.3ex \@plus.2ex
}%
                                   {\color{sdkblue}\sectionfont}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Running heads

\def\ps@headings{\let\@mkboth\markboth
\let\@oddfoot\empty
\let\@evenfoot\@oddfoot
%%
 \def\@evenhead{\vtop{\hbox to\textwidth{%
\color{ltgray}%
{\color{black}\foliofont\thepage}\qquad\normalsize\runningheadfont\leftmark\hfill}\vskip6pt
\color{veryltgray}\hrule height 1.5pt width \textwidth}}
 \def\@oddhead{\vtop{\hbox to\textwidth{%
\color{ltgray}
\hfill
\normalsize\runningheadfont\rightmark\qquad\color{black}\foliofont\thepage}\vskip6pt
\color{veryltgray}\hrule height 1.5pt width \textwidth}}
%%
 \def\chaptermark##1{\markboth {\runningheadchapfont 
Chapter \thechapter.
\hskip6pt\relax\uppercase{##1}}{}}%
 \def\sectionmark##1{\markright {{\runningheadchapfont Section 
\thesection}
\hskip 6pt\relax\uppercase{##1}}}}

\pagestyle{headings}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Table of Contents, Headings in TOC

\newcommand{\smnormalsize}{\@setfontsize\smnormal{10pt}{12pt}}

\def\@dottedtocline#1#2#3#4#5{%
\ifnum #1>\c@tocdepth \else \vskip \z@ plus.2\p@ {\leftskip #2\relax%
\rightskip \@tocrmarg  \parfillskip -\rightskip \parindent #2\relax%
\@afterindenttrue \interlinepenalty \@M \leavevmode \@tempdima #3\relax %
\advance \leftskip \@tempdima \hbox {}\hskip -\leftskip {\smnormalsize
\color{sdkblue}#4}%
\nobreak% \leaders \hbox {$\m@th \mkern%
% \@dotsep mu.\mkern \@dotsep mu$}
\hfill\nobreak\hbox to\@pnumwidth {\hfil\it #5}\par }\fi}


\renewcommand\tableofcontents{%
    \chapter*{\contentsname
        \@mkboth{%
           \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}%
{\parskip=0pt
\rm
\hypersetup{linkcolor=black}   % color of internal links
    \@starttoc{toc}%
}
    \if@restonecol\twocolumn\fi
\hypersetup{linkcolor=sltblue}   % color of internal links
    }



\renewcommand*\l@part[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{2.25em \@plus\p@}%
    \begingroup
\color{sdkblue}
      \parindent \z@ \rightskip \@pnumwidth
      {\leavevmode
       \large \bfseries\uppercase{PART~#1}\hfil\par
}\par
       \nobreak
         \global\@nobreaktrue
         \everypar{\global\@nobreakfalse\everypar{}}%
    \endgroup
  \fi}

\renewcommand*\l@section{\vskip3pt\@dottedtocline{1}{24pt}{2.3em}}
\renewcommand*\l@subsection{\vskip3pt\@dottedtocline{2}{52pt}{3.2em}}
\renewcommand*\l@subsubsection{\@dottedtocline{3}{7.0em}{4.1em}}
\renewcommand*\l@paragraph{\@dottedtocline{4}{10em}{5em}}
\renewcommand*\l@subparagraph{\@dottedtocline{5}{12em}{6em}}

\def\l@chapter#1#2{%
    \vskip 12pt 
     \setlength\@tempdima{2em}% was 1.5
    \begingroup
\large
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
%% comment out line below for indented chapters ==>>
      \hskip -\leftskip
%% uncomment out line below for indented chapters ==>>
%\hskip-6pt
{\bf #1}\nobreak\hfil \nobreak\hbox
to\@pnumwidth{\hss\bfseries\itshape #2}\par
      \penalty\@highpenalty
    \endgroup\vskip1pt}

\def\l@starchapter#1#2{%
    \vskip 12pt 
     \setlength\@tempdima{2em}% was 1.5
    \begingroup
\large
      \parindent \z@ \rightskip \@pnumwidth 
      \parfillskip -\@pnumwidth
      \leavevmode
%      \advance\leftskip\@tempdima
%      \hskip -\leftskip
\noindent\hskip-24pt
{\bf #1}\nobreak\hfil \nobreak\hbox to\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup\vskip1pt}

\def\l@appendchapter#1#2{%
    \vskip 12pt 
     \setlength\@tempdima{2em}% was 1.5
    \begingroup
\large
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
%% comment out line below for indented chapters ==>>
      \hskip -\leftskip
%% uncomment out line below for indented chapters ==>>
%\hskip-6pt
{\bf #1}\nobreak\hfil \nobreak\hbox
to\@pnumwidth{\hss\bfseries\itshape #2}\par
      \penalty\@highpenalty
    \endgroup\vskip1pt}



\def\l@ssect#1#2{%
    \vskip 2pt 
     \setlength\@tempdima{2em}% was 1.5
    \begingroup
\normalsize
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
\hskip-21pt
{#1}\nobreak\hfil \nobreak\hbox to\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup\vskip1pt}

%%% Preface
\def\preface{\chapter*{Preface}
\addcontentsline{toc}{starchapter}{\protect\numberline{}Preface}%
\markboth{Preface}{Preface}}

%%% Bibliography
\newdimen\bibindent
\setlength\bibindent{1.5em}
\renewenvironment{thebibliography}[1]
     {\chapter*{\bibname}%
\markboth{Bibliography}{Bibliography}
\addcontentsline{toc}{starchapter}{\protect\numberline{}Bibliography}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist\newpage\thispagestyle{empty}}
\let\@openbib@code\@empty

%%% footnoterule
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule\@width.4\columnwidth
  \kern2.6\p@}

%%%
%% \theindex is redefined in preamble.tex, in order to
%% send index head to the TOC.


%\textwidth started at 5.41in

\iflandscape
\global\textwidth8.5in
\global\textheight7in
\oddsidemargin=36pt
\evensidemargin=0pt
\advance\voffset-1in
\else
\textwidth=6in
\advance\textheight 1.25in

\advance\voffset-.5in
\oddsidemargin=.5in
\evensidemargin=0pt
\fi

%%%%%%%%%%%%%%%
%% Material from here to endingput were in preamble.tex ==>>
%% put into ourbook.cls to make it work better in Git environment

\usepackage{multicol}
%\usepackage[letterpaper, margin=1in]{geometry} 
\usepackage[answerdelayed]{exercise}

\def\verbatim@font{\small\ttfamily}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% for exercises with working space for students:
\newdimen\ExtraWorkingSpace

\long\def\addworkingspace{\nobreak
\hsize=.5\textwidth\vtop\bgroup\hbox to
\textwidth\bgroup\vrule height 24pt width0pt\hskip-36pt\vtop\bgroup\hsize=.45\textwidth
\parskip=12pt
\linewidth=.45\textwidth\noindent{\color{white}.}\hskip-2pt\ignorespaces}

\def\endworkingspace{\vskip\ExtraWorkingSpace
\global\ExtraWorkingSpace=0pt
\vskip24pt 
\rlap{\hbox
to\textwidth{\hskip.5\textwidth\hskip16pt\vrule height 18pt depth0pt
\color{sdkblue}\footnotesize\bfseries\itshape 
\hrulefill\ \ \ 
Answer on
\hyperlink{x\ExerciseLabel}{Page \expandafter\pageref{y\ExerciseLabel}}
\ \ \ \hrulefill\hbox to -34pt{}}
\hskip30pt\vrule height 18pt depth 0pt
} \vskip18pt\egroup
\rlap{\hskip16pt\hskip.05\textwidth\vtop{\vskip-30pt\hsize=.5\textwidth
\advance\hsize by 18pt
\hrulefill\ \ \ \color{sdkblue}\bfseries\itshape\lower 3pt\hbox{Working
Space}\ \ \ \hrulefill
\vskip-27pt
\vrule depth 18pt height0pt\hfill
\vrule depth 18pt height0pt\vskip1sp
}}\egroup\egroup}

\newcount\questionnumber
\def\xQuestion{\parskip=0pt\advance\questionnumber by
1\vskip6pt\leftskip=36pt\noindent\llap{\hbox to 24pt{\hfill\the\questionnumber.\ \
}}}
\renewcommand{\@@@ExeEnv}{%
    \pagebreak[1]\vskip\ExerciseSkipBefore
    \@QuestionLevel1
    \refstepExecounter
    \begingroup\@getExerciseInfo\ExerciseHeader
    \addcontentsline{\ext@exercise}{\toc@exercise}{\ExerciseName\
        \theExercise\ \expandafter{\itshape \ExerciseTitle}\hspace{.66em}}
    \endgroup\AtBeginExercise
\setbox0=\vbox\bgroup\questionnumber=0
\let\Question\xQuestion\addworkingspace}

\let\saveendExercise\endExercise
\def\endExercise{\vskip1sp\endworkingspace\egroup\unvbox0
\vskip12pt\saveendExercise}

\renewcommand{\ExerciseHeader}{
\hbox to \hsize{\vrule height 24pt
width 0pt
\hskip-36pt
{\color{sdkblue}%
{\exercisenamefont\ExerciseHeaderDifficulty\ExerciseName\ %
\ExerciseHeaderNB}{\exercisetitlefont\ExerciseHeaderTitle\ExerciseHeaderOrigin}}\hfill}%
\nobreak}



\def\AnswerName{Answer to Exercise}%

\renewcommand{\AnswerHeader}{\vskip12pt\goodbreak
\hbox to \textwidth{\vrule height 24pt
width 0pt
{\answertitlefont
\AnswerName\ %
\ExerciseHeaderNB\ \itshape(on page
\pageref{\ExerciseLabel})%% Good!!
}\hfill}%\hypertarget{x\ExerciseLabel}{}%
\let\@auxout=\@mainaux
\expandafter\label{y\ExerciseLabel}\nobreak}


\setlength{\parskip}{\baselineskip}
\setlength{\parindent}{0pt}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{fancyvrb}
\usepgflibrary{shapes}
%\usepackage{bera}

\long\def\boxed#1{{\fboxsep=6pt\fbox {\m@th $\displaystyle #1$}}}


\newcommand{\pyfunction}[1] {{\tt #1}}
\newcommand{\pyvar}[1] {{\tt #1}}
\newcommand{\pytype}[1] {{\tt #1}}
\newcommand{\filename}[1] {{\tt #1}}
\newcommand{\newterm}[1] {{\it #1}} 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% [original] allows us to use version of theindex defined below

\usepackage[original]{imakeidx}

%% had to make these changes to get Index into TOC

\def\theindex{\startonoddpage
\phantomsection
\addcontentsline{toc}{starchapter}{\protect\numberline{}Index}
\imki@maybeaddtotoc \if@twocolumn \@restonecolfalse \else \@restonecoltrue \fi 
\columnseprule \z@ \columnsep 35\p@ \twocolumn [\@makeschapterhead
{\vskip-24pt\indexname }]
\@mkboth { \indexname }{ \indexname }\thispagestyle {plain}
\parindent \z@ \parskip \z@ \@plus .3\p@ \relax \let \item \@idxitem}

\makeindex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\usepackage[pdfnewwindow=true,      % links in new window
    colorlinks=true,        % true: colored links
    linkcolor=sdkblue,   % color of internal links
    citecolor=sdkblue,   % color of links to bibliography
    filecolor=sdkblue,   % color of file links
    urlcolor=sdkblue,    % color of external links
final=true]
{hyperref}

%% To make less, and non-stretching, space around itemize

% this is possible but doesn't leave enough space between items:
%\usepackage{enumitem}
%\setlist{noitemsep}

\topsep=8pt
\itemsep=8pt
\parsep=8pt

\def\@listi{\leftmargin\leftmargini
            \parsep 4\p@ 
            \topsep 4\p@ 
            \itemsep4\p@ }
\let\@listI\@listi
\@listi




%% space above and below equations
\abovedisplayskip=11pt
\belowdisplayskip=11pt


%% So that extra space on the page is put
%% at the bottom, not around lists or equations
%% etc.
\raggedbottom

\endinput
%%
%% End of file `ourbook.cls'.
