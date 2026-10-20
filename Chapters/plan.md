# Book-Level Improvement Plan

This plan covers the whole book: what to add, what to cut, what to merge and split, and the order of work. Chapter-level fixes are in each chapter's `notes.md`. This file does not repeat them.

## Basis and limits

- Sources: the 202 `notes.md` files, the title and word count of every chapter in `book_00.txt`, a scan of the 41 chapter folders that are not in `book_00.txt`, and a grep for FIXME/ADD/PLACEHOLDER markers and cross-references.
- Merge and split proposals rest on titles, lengths, overlaps seen in the notes, and the grep results. Before any merge or cut, reread the affected chapters in full.
- Word counts include LaTeX markup, so they are rough.

## 1. Book-wide problems to fix first

1. **Unfinished material is everywhere.** About 193 FIXME, ADD, or TODO lines appear in 88 chapters, and several chapters are placeholder-heavy. Set a rule: no chapter ships with a FIXME in the body. Either finish the section or delete it.
2. **Stub chapters.** Many chapters are under 500 words and do not teach a full lesson. Examples: `queues` (395), `hash_tables` (394), `lens` (316), `refraction` (297), `geocoding` (329), `multiv_func` (329), `json_xml` (7), `practice_polynomials` (53), `polynomials_intro` (639), `radio`, `power_generation`, `basic_spreadsheet`, `prerequisites`, and `stop_words` (near 0). Each stub gets a decision in Section 4 or 5.
3. **Answer format.** Answers appear inline after each exercise in some chapters and are missing in others. Pick one convention. A back-of-book answer key for odd-numbered exercises is the usual choice.
4. **Cross-references.** Several `\ref` labels do not match their `label=` (for example `ex:justify` vs `ex:means-justify`, `volume 2` vs `volume2`, `iterate 1` vs `iterate_1`). Some chapters point to chapters that do not exist, such as "the recursion chapter" (cited in `trees`) and "the chi-square chapter" (cited in `stat_tables`). Fix all labels and references in one pass, then check the build for undefined refs.
5. **Code.** Some listings have syntax errors that will confuse students: unbalanced f-strings and braces (`discrete_probability`, `shortest_path`), a duplicated block in `graph_algorithms`, a broken `Rectangle` import in `riemann_sums`, and undefined names such as `comb` without `math.` and `MAX` vs `CAPACITY` in `queues`. Run every Python and C listing in its stated environment. Put the test script next to the chapter.
6. **Factual and arithmetic errors.** The notes list many. The most serious are wrong answers to exercises: `conditional_prob` (95.1% should be about 87.6%), `series_tests` (the remainder example gives n = 41 instead of 123), `power_series` (radius 1, not ½), `polar_calc` (area inside r = 6 sin θ and outside the cardioid is 4π), `double_int_applications` (paraboloid area about 539, and the average-value formula), `riemann_sums` (0.6345, not 0.4202), `inferences_means` (paired-data direction), `gas` (5.57 mol), `seq_calc` (fish recurrence), `intro_c` and `linked_list_c` (size and malloc claims). Fix every wrong answer before anything else. A wrong answer in a practice set costs trust in the whole book.
7. **Notation and terminology.** Decide and enforce: "density" vs "charge density," "ref" vs "label," vector arrows (bold vs arrow), and whether to say "we" or "you." Use one unit system and one way to write degrees and radians in trig.
8. **Index.** Index entries were added chapter by chapter, which leaves duplicates (e.g., `bayes' theorem` in several forms) and inconsistent names. Do one index pass after the content is final.
9. **Reading level.** The audience is high school students aiming at a top engineering program. Some chapters are dense and proof-heavy (for example `series_tests`, `double_int_applications`, `partial_deriv_grad`). Add a short prerequisite line at the start of each chapter and a "why this matters" paragraph.

## 2. Important topics that are missing

Ordered by how much they matter for the stated goal.

1. **Triple integrals.** `double_int_applications` and `volume_double_integral` both promise a later chapter on triple integrals. It does not exist. Write it, and include cylindrical and spherical coordinates (the intro of `volume_double_integral` promises both).
2. **Taylor and Maclaurin series.** There is a draft at `taylor_series` (2062 words) that is not in `book_00.txt`. Add it after `power_series`.
3. **Chi-square tests.** `stat_tables` and `inferences_proportion` assume a chi-square chapter. A full draft exists at `chi_square` (3194 words) and is not in `book_00.txt`. Add it after the means and slopes inference chapters.
4. **Random variables, expected value, and variance.** These appear throughout (`limits`, `optimization`, `seq_calc`, `inferences_means`, `multiv_dist`), but no chapter teaches them. Add a chapter on discrete random variables before the distribution chapters.
5. **Recursion.** `trees` says "the recursion chapter" covers recursive binary search, but no such chapter exists. Add a short recursion chapter before trees: base case, recursive case, call stack, and recursive DFS.
6. **Algorithm analysis (Big-O).** Hash tables, queues, trees, and shortest path all use O(·) claims with no definition. Add a short chapter on counting steps and Big-O, placed before the data-structure block.
7. **Numerical root finding and approximation.** Newton's method and bisection would sit well with `euler_method` and `optimization`.
8. **Testing and debugging.** Students write programs in many chapters. A short chapter on print-debugging, assertions, and simple unit tests would help.
9. **Version control and a project workflow.** Optional, but useful if the book expects students to keep a repository of their scripts.
10. **Linear regression as a unit.** `inferences_slopes` refers to a Numerical Methods chapter for least squares. Decide whether least squares belongs in `num_methods_2` or its own chapter (see Section 6).
11. **Triangle and coordinate geometry.** Lines and planes in 3D (equations of a line and a plane, distance from a point to a plane) are used in `cross`, `determinants_inverse`, and `vector_sim` and never taught directly.
12. **A glossary and a formula sheet.** Not a chapter, but a required back-matter item.
13. **Cumulative review and mixed practice.** Each unit should end with a review chapter that mixes topics, as the AP exams do.

## 3. Topics covered too many times

Each row names the topics, where they appear, and what to keep.

| Topic | Where it appears | Keep / action |
|---|---|---|
| Python basics and lists | `intro_python1`, `pylists`, `intro_python2`, `classes`, `pymultpoly`, `stacks`, `queues`, `permutations` (sorting) | Keep `intro_python1` and `intro_python2`. Fold `pylists` into `intro_python1`. Move `permutations` sorting into Python. Put `classes` in `intro_python2`. |
| Polynomials | 10 chapters (`polynomials_intro` through `interpolating_polynomials`, plus `pymultpoly`) | Reduce to 3 chapters (Section 6). |
| Compound interest and population growth | `compound_interest`, `sequences`, `seq_calc`, `exponential_decay` | Keep one full treatment in `exponentials_logs` (new). Other chapters link to it. |
| Riemann sums and integrals | `riemann_sums`, `definite_integral`, `ftc`, `u-substitution`, `antiderivatives`, and an unlisted `int_methods` draft that repeats u-substitution | Keep `riemann_sums` (the definition and sigma notation), `definite_integral`, and `ftc`. Cut the `int_methods` repeat. |
| Bayes' theorem | `bayes`, `pop_prop` (Bayes' law for continuous probability), `bayes_classifier`, and the Monty Hall section | Keep `bayes` as the full treatment. Other chapters refer to it. |
| Descriptive statistics and tools | `basic_statistics`, `stat_spreadsheets`, `num_methods`, `num_methods_2`, `jamovi`, `intro_dataviz`, `matplotlib`, `pandas`, `sampling`, `biases1` | Merge the tool-specific chapters into one "data tools" chapter with three appendices (Excel, Python, jamovi). |
| Motion and forces | `intro_motion`, `kinematics`, `falling_bodies`, `newtons_second_law`, `free_body_diagrams`, `mass_weight_gravity` (gravity), `friction`, `inclines`, `projectiles` | Reduce to four chapters (Section 6). Gravity is taught once. |
| Energy and conservation | `work_energy`, `matter_energy_intro`, `conservation_mass_energy`, `heat`, `phase_change`, `temp_kinetic`, `gas`, `engine` | Merge the conservation and energy material into one chapter. Merge `gas` and `temp_kinetic`. |
| Vehicle applications | `boats`, `sailing`, `airplanes`, `rotorcraft`, `rocketry` | Merge boats and sailing. Keep one "flight" chapter for airplanes, rotorcraft, and rockets. |
| Vectors | `vectors`, `dot`, `vectors_matrices`, `vector_functions`, `vector_sim`, `spans_independence` (unlisted), `span`, `subspaces`, `dependence`, `linear_combo` | Keep one vectors chapter (with dot product), one linear-combinations chapter, and one independence/span chapter. Drop `spans_independence` if its content is already in `span` and `dependence`. |
| Derivatives | `differentiability`, `derivative_definition`, `derivative_rules`, `deriv_graphshape`, `implicit_diff`, `related_rates`, `optimization` | Merge `differentiability` into `derivative_definition`. Keep the rest. |
| Circular and oscillating motion | `circular`, `circular_2`, `oscillations`, `orbits`, `tides`, `polar_coord`, `polar_calc` | Merge `circular` and `circular_2`. Keep `polar_coord` and `polar_calc` as one polar unit. |
| Light | `emwaves`, `reflection`, `refraction`, `lens`, `camera`, `eye`, `diodes` | Merge reflection, refraction, and lens into one optics chapter. Keep camera and eye as applications. |
| Data representation | `intro_text`, `accents_scripts`, `hexbinary`, `floating`, `decompression`, `bitmap`, `intro_c` | Merge text, hexadecimal, and floating point into one chapter. `bitmap` stays. |
| Web | `http`, `api`, `html`, `json_xml` (empty) | Merge `http` and `api`. Keep `html` as a separate chapter. Fill or delete `json_xml`. |
| Data structures | `stacks`, `queues`, `hash_tables`, `trees`, `tree_traversal`, `linked_list_c`, `priority_queues`, `graph_algorithms`, `shortest_path` | Merge stacks and queues. Expand hash tables or merge them into a collections chapter. Keep the rest. |
| Geography | `long_lat_dist`, `geocoding`, `making_a_map` | One "Maps and Location Data" chapter. |
| Matrices and systems | `linear_algebra_intro`, `systems_matrices`, `matrices_applications`, `determinants_inverse`, `transformations`, `eigen`, `projections`, `gram-schmidt`, `decomposition`, `positive-semidefinite` | `systems_matrices` and `matrices_applications` overlap. Merge them. |
| Volumes | `volume_solids`, `volume_single_integral`, `volume_double_integral` | Merge `volume_solids` into the single-integral volumes chapter. |

## 4. Chapters to delete

Delete or replace with a real chapter. Each of these has no teachable content as it stands.

- `json_xml` (7 words). Either write a real JSON chapter and move it into the web unit, or delete the entry.
- `practice_polynomials` (53 words). Replace with a practice set in the polynomials review chapter.
- `radio` (9 words), `power_generation` (24 words), `basic_spreadsheet` (0 words), `prerequisites` (1 word), `stop_words` (2 words). Delete unless a real draft is written.
- `sorting_c` and `stop_words` are commented out in `book_00.txt`. Delete their folders or finish them.
- The unlisted `spans_independence` draft (1715 words) repeats `span` and `dependence`. Delete it after moving any unique content.
- The unlisted `int_methods` draft (4935 words) repeats `u-substitution`. Keep only the integration-by-parts section, if it is not already covered, and move it into `u-substitution`.
- `conic_sections` (500 words) is thin. Move the conic definitions into `circles` (as parabola, ellipse, hyperbola sections) or into `functions` as a graphing section.
- `refraction` (297) and `lens` (316) are too thin to stand alone. Merge them (Section 5).
- `electric_motors_generators` (480) has no unique content beyond `induction`. Merge it.

## 5. Chapters to merge

Each row gives the new chapter name and its sources in order.

1. **Kinematics** = `intro_motion` + `kinematics` + `falling_bodies`.
2. **Forces and Motion** = `newtons_second_law` + `free_body_diagrams` + `friction` + `inclines`. Move gravity from `mass_weight_gravity` into this chapter, leaving `mass_weight_gravity` as a short "mass, weight, and gravity" section.
3. **Energy and Conservation** = `work_energy` + `matter_energy_intro` + `conservation_mass_energy`.
4. **Gases and Heat** = `gas` + `temp_kinetic` + `heat` + `phase_change`.
5. **Boats and Sailing** = `boats` + `sailing`.
6. **Flight** = `airplanes` + `rotorcraft` + `rocketry`.
7. **Optics** = `reflection` + `refraction` + `lens`. Keep `camera` and `eye` as applications.
8. **Data Representation** = `intro_text` + `accents_scripts` + `hexbinary` + `floating` + `decompression`.
9. **Web APIs** = `http` + `api`.
10. **Stacks and Queues** = `stacks` + `queues`.
11. **Maps and Location** = `long_lat_dist` + `geocoding` + `making_a_map`.
12. **Matrices and Systems** = `systems_matrices` + `matrices_applications`.
13. **Vectors** = `vectors` + `dot` + `cross`. Keep `cross` separate only if it grows past 1500 words.
14. **Triangles, Angles, and Parallels** = `angles` + `triangles` + `pythagorean_theorem` + `parallel_perpendicular`.
15. **Exponentials and Logarithms** = `exponents_review` + `logs` + `exponential_decay` + `compound_interest`.
16. **Polynomials I: Basics and Operations** = `polynomials_intro` + `add_subtract_polynomials` + `multiplying_polynomials` + `pymultpoly` + `common_products_polynomials`.
17. **Polynomials II: Factoring and Rational Functions** = `factoring_polynomials` + `rational_functions` + `partial_frac`.
18. **Polynomials III: Graphing and Interpolation** = `graphs_polynomials` + `interpolating_polynomials`. Move `differentiating_polynomials` into the derivatives unit.
19. **Circular Motion** = `circular` + `circular_2`.
20. **Derivatives** = `differentiability` + `derivative_definition`.
21. **Volumes** = `volume_solids` + `volume_single_integral`.
22. **Data Tools** = `basic_statistics` + `stat_spreadsheets` + `jamovi` (as appendices, with `pandas` kept separate for Python).
23. **Describing Data** = `num_methods` (the first half) + `intro_dataviz`.
24. **Relationships in Data** = `num_methods_2` + the bivariate material from `num_methods`.
25. **Discrete Probability and Counting** = `discrete_probability` + `combinatorics` + the counting parts of `permutations`.
26. **Continuous Distributions** = `cdf_uniform` + `normal_t` + `multiv_dist` + `multiv_normal`.
27. **Expected value and variance** (new) before the distributions chapter.
28. **Atomic and Molecular Mass** stays. **Chemical Reactions** (531 words) merges into `atomic_mass` as "Balancing Reactions."
29. **Concrete, Metals, Fertilizer, and Manufacturing** = one "Materials" chapter if the book keeps this unit. Otherwise delete (Section 4 and 7).

## 6. Chapters to split

Each entry names the chapter, its size, and the two or three pieces.

1. **`partial_deriv_grad`** (15,147 words, the largest chapter). Split into (a) partial derivatives, (b) gradients and directional derivatives, and (c) optimization with multiple variables and Lagrange multipliers (only if the book wants them).
2. **`double_int_applications`** (7,423). Split into (a) mass, charge, and center of mass, and (b) moments of inertia, radius of gyration, surface area, and average value.
3. **`double_int_regions`** (7,165). Split into (a) type I and II regions and iterated integrals over them, and (b) polar double integrals.
4. **`series_tests`** (6,268). Split into (a) divergence, integral, and comparison tests, and (b) absolute convergence, ratio, root, and the test-selection strategy.
5. **`limits`** (6,957). Split into (a) limits and continuity, and (b) the intermediate value theorem and limit laws.
6. **`charge`** (6,463). Split into (a) electrostatics and charge, and (b) magnetism and forces on charges.
7. **`oscillations`** (6,717). Split into springs and simple harmonic motion, and pendulums and damping.
8. **`simple_machines`** (6,934). Split into levers and pulleys (statics) and work and mechanical advantage (energy).
9. **`riemann_sums`** (5,851). Split into (a) approximations and sigma notation, and (b) the Python program, real-world data, and the trapezoidal rule.
10. **`functions`** (5,642). Split into (a) functions and their graphs, and (b) inverses, composition, and transformations (merge with `transforms`).
11. **`experiments`** (5,574). Split into (a) experimental design and sampling, and (b) controlled experiments and inference from them. Some of this overlaps `sampling` (merge that duplication).
12. **`num_methods`** (6,175). Split into univariate description and visualization, and (in `num_methods_2`) bivariate description.
13. **`reflection`** (5,012). Split into reflection and optics, and photons and quantum behavior (the photons section is not a reflection topic).
14. **`momentum`** (4,569) only if the energy chapter does not absorb it. Otherwise keep it whole.
15. **`derivative_definition`** (4,293) and **`deriv_graphshape`** (5,156). Split the first into the limit definition and derivative rules, and keep the second as the shape-of-a-function chapter.
16. **`intro_python2`** (4,431). Split into (a) the advanced syntax chapter (functions, classes, errors), and (b) libraries (numpy, matplotlib, pandas).
17. **`inferences_slopes`** (5,414) and **`stat_tables`** (4,892). Move the table appendix out of the chapter to the back matter, and split slopes into regression basics and inference.

## 7. Unlisted drafts: decide before shipping

The folder list includes about 40 unlisted drafts. Most are short (under 350 words) and sit in a machine-learning block that `book_00.txt` has commented out. Decide as a book:

- **Keep as a "Data Science" unit** (only if the book wants that scope). Then finish the drafts and list them in `book_00.txt`. Start with `lin_reg_r2_anova`, `simple_linear`, `simple_logistic`, `confusion`, `train_val_test`, and `knn_classifier`. Then the neural network and deep learning chapters last.
- **Otherwise delete** the drafts. They are not in the book, and keeping them invites confusion.
- **Keep and list now**: `chi_square` (3194 words, needed by the stats unit), `taylor_series` (2062 words, needed by the series unit), `calc_probability` (4958 words, but first merge it with the probability chapters because it repeats them), and `economics` (4742 words, decide whether it fits a physics or math book at all).
- **Merge and list**: `int_methods` (remove its u-substitution repeat, keep integration by parts if needed) and `log_transform` (merge into the exponentials and logarithms chapter).
- **Commented out in book_00.txt** but present: `diagonalization` and `linear differential systems` (both linear algebra; `diagonalization` belongs after `eigen`, and `linear differential systems` belongs in the differential equations unit).

## 8. Ordering and prerequisites

- `sequences` (position 54) comes before limits and before the calculus chapters that use it. That is fine. But `seq_calc` (position 188) needs a clear pointer back to `sequences` and must not repeat its content.
- Data visualization (`intro_dataviz`, position 61) appears before the statistics that use it. Move it ahead of `basic_statistics`, or make the statistics chapter self-contained.
- `permutations` (sorting) appears before the Python sorting material. Move sorting into the Python unit.
- Statistics inference (`inferences_proportion`, `inferences_means`, `inferences_slopes`, `stat_tables`) should come after the normal distribution and before any chi-square chapter. Check the current order.
- The matrix block (`linear_algebra_intro` through `gram-schmidt`, `decomposition`, `positive-semidefinite`) should follow vectors. `bitmap` (position 143) is a computer-science chapter that refers forward to "the transformations chapter" (position 135, which comes earlier). Check that pointer and make it match the actual order.
- The probability block (`discrete_probability`, `combinatorics`, `permutations`, `conditional_prob`, `bayes`) needs a single prerequisite line before it: basic fractions and percentages.

## 9. Work order

Phase 1, correctness (before anything else):
1. Fix every wrong answer and code listing listed in Section 1, items 5 and 6.
2. Fix every broken label and ref. Confirm the book builds with no undefined references.

Phase 2, structure (decide, then act):
3. Apply the merges in Section 5, one unit at a time.
4. Apply the splits in Section 6 to the largest chapters first.
5. Apply the deletions in Section 4, after moving any unique content.
6. Decide the unlisted drafts (Section 7). Update `book_00.txt`.

Phase 3, gaps:
7. Write the missing topics in Section 2, in this order: random variables, recursion, Big-O, chi-square (from draft), Taylor series (from draft), triple integrals, then testing and debugging.

Phase 4, consistency:
8. Enforce the answer format, notation, and voice rules (Section 1, items 3 and 7).
9. Rebuild the index (Section 1, item 8).
10. Write the glossary, formula sheet, and answer key.

Phase 5, review:
11. Run every code listing. Recheck the arithmetic in the top 20 exercises by an independent method (a script or a second read).
12. Pilot the book with two or three students and fix what they get stuck on.

## 10. Definition of done

- Every chapter in `book_00.txt` builds, has no FIXME/ADD markers, has no undefined references, and has a `notes.md` that says "no open items."
- Every listed chapter has a prerequisite line, a summary, practice with answers in the agreed format, and a cumulative review at the end of its unit.
- Every code listing runs as shown in its stated environment.
- No topic appears as a full treatment in more than one chapter. Other chapters link to the one that owns it.
- No chapter is under 600 words unless it is a deliberate short lesson (for example, a review or a glossary entry).
