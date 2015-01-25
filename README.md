Computational Linguistics 2
===========================


Overview
--------

This is the primary course website for Computational Linguistics 2 (Lin 637), offered by the [Department of Linguistics] [department] at [Stony Brook University] [sbu]. For a brief list of topics, check the [syllabus] [syllabus].

This repository is publicly available and hosts the LaTeX source code for the lecture notes. Compiled pdfs of each chapter are available under the [pdf] [pdf] folder.


Prerequisites
-------------

This course assumes a certain degree of familiarity with generative syntax, phonology, and basic mathematics (sets, functions, relations, first-order logic). Please take the [online survey] [survey] to ensure that you satisfy the prerequisites. If you have weaknesses, consult the relevant material suggested in the [readings repository] [readings].

In addition, you will have to use Python, markdown and LaTeX at various points during this course. The [link list](#Link_List) at the end of this document has some useful tutorials.


Readings
--------

Course readings are made available through the private [readings repository] [readings]. You must be enrolled in this class in order to get access.


Homeworks
---------

Each homework will be hosted in its own private repository. Only course participants have access to these repositories.

Homework 1: coming soon


Compilation Instructions
------------------------

If you want to compile the lecture notes yourself, or use them as the basis for your own course, carefully follow the steps below.

1) Make sure you have all necessary software installed and set up correctly, in particular

  - a recent LaTeX distribution with _Tikz_ >= 3.00 and recent versions of _minted_ and _forest_
  - the Python pygments package (required by minted)

2) Clone the repository via git, or download and extract the [zip file](../../archive/master.zip).
 Note that the project folder will also contain an empty _build_ folder, which is used for temporary files to speed up compilation.

3) Use your standard tex --> pdf compilation tool chain, but ensure that pdflatex is run with the parameters --shell-escape and --etex


Link List
---------

coming soon


[department]: http://linguistics.stonybrook.edu
[pdf]: ../../tree/master/pdf
[readings]: ../../../readings
[sbu]: http://www.stonybrook.edu
[survey]: https://testmoz.com/432409
[syllabus]: ../../tree/master/pdf/0_syllabus.pdf
