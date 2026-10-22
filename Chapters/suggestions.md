# Suggestions for the Next Pass

These suggestions come from editing and summarizing all 234 chapters in the 36 volumes. Word counts, exercise counts, and code and figure counts come from a script run over every `student.tex`. Prerequisite problems were confirmed by searching the text.

The series deliberately mixes physics, math, computer science, and statistics in every volume. That design is a strength: a curious student never stays in one subject long enough to get bored. The suggestions below keep that mix. They aim to fix the places where the mix breaks down: a chapter uses a tool before the student has it, a topic is taught three times, or a volume is one chapter long.

---

## 1. Top priorities

If you only do a few things, do these, in this order:

1. **Fix the prerequisite violations** (Section 2). A student who meets `sin θ` in Volume 1, or a derivative in Volume 17, decides the book is not for them. These are the cheapest high-value fixes.
2. **Rebuild the machine-learning unit in Volume 36** (Section 6). Its chapters are short (most around 500 words) and have almost no code or figures. For many students this is the reason they picked up the series, and right now it is the thinnest part of it.
3. **Add a short "Before you start" box and a "Key ideas" box to every chapter.** The `summary.md` files already contain the key ideas, and the prerequisites can come from a dependency file (Section 8).
4. **Add the missing topics a curious teenager will ask about** (Section 5): digital logic and AI ethics.
5. **Split the giant single-section chapters, and merge the duplicated ones** (Sections 3 and 4).

---

## 2. Reordering: prerequisite violations

Each item below is a place where a chapter uses something the student has not seen yet. I confirmed each one in the text.

| Where | Problem | Suggested fix |
|---|---|---|
| `kinematics` (Vol 1) | 7 Python/matplotlib listings; Python is taught in `intro_python1` (Vol 3) | Mark the code "Come back after the Python chapter," or move the plotting examples into `matplotlib` (now in Vol 4) |
| `intro_dataviz` (Vol 3) | Uses Python before `intro_python1`, which is in the same volume | Put `intro_python1` first in Vol 3, or make the dataviz chapter spreadsheet-first |
| `projectiles` (Vol 7) | Uses the quadratic formula; `solving_quadratics` is in Vol 9 | Move `solving_quadratics` to Vol 5 or 6, ahead of projectiles |
| `paradoxes` (Vol 10) | Monty Hall, the birthday problem, and Simpson's paradox all come before probability (Vol 28) | Keep them as teasers, but add explicit "you will prove this in Volume 28/29" pointers. `bayes` should refer back to the Monty Hall teaser |
| `polynomials_1` (Vol 16) | Needs `pylists`, which comes after it in the same volume | Swap the order, or fold the list material into `polynomials_1` (see Section 4) |
| `vector_functions`, `circular_motion`, `rotational_motion` (Vol 17) | Use derivatives (for example, "differentiate each component") two volumes before `derivative_definition` (Vol 19) | Move `vector_functions` to Vol 20. Either rewrite the derivative passages in `circular_motion` as slope or average-rate language, or move the rotational chapters after Vol 19 |
| `bitmap` (Vol 23) | Uses hexadecimal; `data_representation` is in Vol 26 | Move the binary/hex section of `data_representation` earlier (it could open the Vol 23 C sequence) |
| `train_val_test`, `knn_classifier`, `classification_regression` (Vol 36) | The framing chapter (`classification_regression`) comes after the methods it frames | Reorder the ML unit (Section 6) |
| `book_02` | `atomic_mass_reactions` (moles) comes before `matter_energy` (what atoms are); `matter_energy` also re-teaches energy after `energy_conservation` | Order: atoms and bonds → atomic mass and moles → work and energy. Move the energy half of `matter_energy` into `energy_conservation` |

### Volume-size imbalance

| Volume | Chapters | Problem |
|---|---|---|
| Vol 25 | 1 (`web_apis`) | A volume with one chapter, and it teaches HTTP APIs before HTML (Vol 26) |
| Vol 26 | 2 | `html`, `data_representation` |
| Vol 27 | 1 | `maps_location` (`matplotlib` moved to Vol 4) |
| Vol 36 | 24 | Larger than any three other volumes combined |

**Suggestions**
- Combine Volumes 25–27 into one "Data and the Web" volume, in this order: `data_representation`, `html`, a new CSS/JavaScript chapter, `web_apis`, `maps_location`.
- Move `numerical_multi_int` and `triple_integrals` from Vol 36 into Vol 35, which finishes multivariable integration.
- Split the rest of Vol 36 into two machine-learning volumes (Section 6).

### Orphaned chapter

One complete chapter is not in any volume:
- **`sql_2`** (3,231 words; commented out in `book_14.txt`). Uncomment it or place it right after `sql_1`; multi-table joins are what make databases interesting.

---

## 3. Chapters that are too long and should be split

The book's chapters typically run 1,000–3,000 words. These chapters are well beyond that, often with only one `\section`, so a student has no natural stopping place.

| Chapter | Words | Sections | Proposed split |
|---|---|---|---|
| `forces_motion` (Vol 1) | about 5,800 | 4 | **Newton's Laws** (the three laws, net force, normal force, free-body diagrams) / **Friction and Pulleys**. Move universal gravitation to `mass_weight_gravity` or `orbits`. |
| `gases_heat` (Vol 31) | 6,456 | 4 | **Temperature and the Gas Laws** / **Heat, Work, and the Laws of Thermodynamics**. Add entropy and the second law, which are currently missing. |
| `matter_energy` (Vol 2) | 6,330 | 2 | **Atoms and Chemical Bonds** / move the energy material into `energy_conservation`, and point the E = mc² section ahead to `nuclear_physics` (Vol 13). |
| `continuous_distributions` (Vol 30) | 5,633 | 6 | **CDFs, PDFs, and the Uniform Distribution** / **The Normal Distribution**. Move the multivariate normal next to `bayes_classifier` and `numerical_multi_int`, which reuse the snail data. |
| `data_tools` (Vol 3) | 5,227 | 3 | Keep it as **Spreadsheets**. Its mean/variance/standard-deviation material duplicates `num_methods` (Section 4). |
| `num_methods` (Vol 11) | 5,179 | 6 | **Center** / **Spread and Shape**. |
| `charge` (Vol 12) | 5,108 | 7 | **Electric Charge and Coulomb's Law** / **Electric Fields and Gauss's Law**. |
| `rotational_motion` (Vol 17) | 4,961 | **1** | **Torque and Equilibrium** / **Moment of Inertia and Angular Momentum**. It currently opens by reviewing rotational kinematics from `circular_motion`. |
| `circular_motion` (Vol 17) | 4,834 | **1** | **Uniform Circular Motion and Centripetal Force** / **Rotational Kinematics**. At minimum, add section headings. |
| `economics` (Vol 10) | 4,770 | 15 | **Markets: Trade, Supply, and Demand** / **Money, Investment, and Government**. It has only 2 exercises in 4,770 words; supply-and-demand equilibrium is algebra, so add numeric problems. |
| `data_representation` (Vol 26) | 4,740 | 5 | **Text and Integers** (ASCII/UTF-8, binary, hex, two's complement), which could move earlier as noted above / **Floating Point**. |
| `flight` (Vol 8) | 4,721 | 3 | **Airplanes** / **Quadcopters and Rockets**. It has 71 images, some of them unused. |
| `discrete_probability_counting` (Vol 28) | 4,463 | 3 | **Probability Rules** / **Counting**. Then merge the tiny `random_variables` (582 words) with the probability half. |
| `num_methods_2` (Vol 11) | 4,364 | 3 | **Scatter Plots and Correlation** / **The Regression Line**. |
| `int_methods` (Vol 32) | 4,169 | 5 | **Partial Fractions** / **Trigonometric Integrals and Substitutions**. |
| `polynomials_2` (Vol 16) | 4,150 | 3 | **Factoring** / **Rational Functions**. |
| `inferences_means` (Vol 30) | 4,126 | 5 | **One-Sample and Paired t** / **Two-Sample t**. |
| `web_apis` (Vol 25) | 4,047 | 2 | **Using APIs** (HTTP, JSON, calling a real API from Python, which is the fun part) / **Building an API in Node**. It has only **1 exercise**. |
| `derivative_rules` (Vol 19) | 4,004 | 10 | **Product, Quotient, and Chain Rules** / **Derivatives of Trig, Exponential, and Log Functions**. |
| `energy_conservation` (Vol 2) | 4,000 | **1** | Add sections. Optionally split into **Work and Energy** / **Power and Efficiency**. |
| `gradients_optimization`, `partial_derivatives` (Vol 20) | about 4,500 each | 2–3 | Add more section breaks. In `gradients_optimization`, split off the optimization and gradient-descent half; it is the natural bridge to the ML unit. |

**Other chapters with no or one `\section` that need headings:** `experiments`, `experimental_designs`, `regression_slope_basics`, `double_int_regions`, `double_int_polar`, `euler_method` (0), `stemming_lemmatization` (0).

---

## 4. Superfluous or duplicated material: merge candidates

| Topic | Taught in | Suggestion |
|---|---|---|
| **Linear regression** | `num_methods_2` (Vol 11), `regression_slope_basics` (Vol 30), `least_squares` + `simple_linear` + `lin_reg_r2_anova` (Vol 36). The same five-point quiz example appears in three chapters. | Vol 11 handles description, Vol 30 inference, and Vol 36 the derivation (calculus and matrices). Merge `simple_linear` into `least_squares`. Move `lin_reg_r2_anova` to Vol 30 next to `inferences_slopes`, where AP students need it. |
| **Mean, variance, standard deviation** | `data_tools` (Vol 3) and `num_methods` (Vol 11) | Teach the statistics once, in `num_methods`. Keep `data_tools` about spreadsheets, with a forward reference. |
| **Python classes** | `intro_python2` (Vol 4) and `classes` (Vol 16) | Keep the Polynomial class from `classes` as a section of `polynomials_1`. Drop the re-teaching. |
| **Python lists** | `intro_python1` (Vol 3) and `pylists` (Vol 16) | Same treatment: keep the coefficient-list material inside `polynomials_1`. |
| **Recursion** | `intro_python2`, `proofs` (induction), `sorting`, `recursion` (Vol 24) | Move `recursion` right after `intro_python2` and trim the recursion section in `intro_python2`, or cross-reference them. |
| **AC circuits** | `ac` (Vol 12) and the AC/impedance half of `pendulums` (Vol 17) | Move impedance into `ac`. Keep a short "springs and circuits obey the same equation" box in `pendulums`. |
| **Sequences** | `sequences` (Vol 9) and the review opening of `seq_calc` (Vol 33) | Trim `seq_calc`'s re-introduction to a one-paragraph recap. |
| **Data preparation** | `standardization` (500 words) + `one-hot` (400) | Merge into "Preparing Data for Models," with a pointer back to `log_transform` (Vol 11). |
| **Greek alphabet** | `greek` (Vol 1, a reference table) | Move it to an appendix volume along with `stat_tables`, the unit tables from `units_conversions`, and a formula sheet. |
| **Experimental design** | `experiments` + `experimental_designs` (Vol 19, one section each) | Fine as two chapters, but give them sections and remove the vocabulary overlap. |

**Possibly superfluous for the target reader:**
- `positive-semidefinite` (Vol 23): Goemans–Williamson Max Cut with cvxpy is graduate-level. It is a fun "here be dragons" chapter. Keep it only if it is clearly labeled as optional enrichment.
- Parts of `linked_list_c` that cover allocator padding and alignment.
- The B-tree, trie, and suffix-tree survey in `trees`.

Mark these as optional rather than cutting them.

---

## 5. What is missing

These are ranked by how much a curious high school student would care, and by how well each topic reuses tools the series already teaches.

### Physics
1. **Entropy and the second law of thermodynamics.** No chapter states the second law, even though `engine` discusses efficiency. A Carnot efficiency section would complete the story.

### Computer science
2. **Digital logic: from transistors to adders.** Logic gates appear nowhere, yet the pieces are all present: `sets` (logic tables), `diodes` (transistors are mentioned), and `data_representation` (binary). A chapter that builds an adder from NAND gates answers "how does a computer actually compute?"
3. **CSS and JavaScript.** There is an `html` chapter and a Node server, but nothing to make a page look good or respond to clicks. Students want to build something they can show friends.
4. **How the internet works.** Packets, IP addresses, routing as shortest paths (`shortest_path`), and DNS. A natural partner to `web_apis`.
5. **Dynamic programming.** It is mentioned once, in `intro_markov`. Memoization is already in `recursion`, so a chapter on DP (making change, edit distance for spell-check) would be a small step.
6. **Multi-table databases.** Already written as the orphan `sql_2`.

### Thinking and society
7. **AI ethics and algorithmic bias.** The ML unit never discusses fairness, privacy, or what happens when a model is wrong about a person. `biases1` covers human cognitive bias; a companion chapter on machine bias belongs at the end of the ML unit.
8. **Personal finance.** Loans, credit-card interest, and saving. It reuses `exponentials_logarithms` and `seq_calc` (the savings recursion is already there), and every teenager will need it.
9. **Energy and climate.** The greenhouse effect mentions in `emwaves` and `gases_heat` could become a full chapter on where energy comes from, tying in photons, heat, engines, and economics.

---

## 6. The machine-learning unit (Volume 36)

**Current state:** about 20 ML chapters, most around 500 words, with almost no code and no figures. The framing chapter comes after the methods, and data preparation is split across two tiny chapters. The topics are right; the chapters read like glossary entries.

### Proposed structure

**Volume 36a: Learning from Data**
1. `classification_regression`: what supervised learning is.
2. `train_val_test`.
3. Preparing data: `standardization` + `one-hot` (pointing back to `log_transform` in Vol 11).
4. `least_squares` (with `simple_linear` merged in).
5. `lin_reg_gradient_descent`.
6. `logistic_regr`.
7. `confusion`.
8. `knn_classifier`.
9. `bayes_classifier`, with the stemming material from Vol 29 turned into a **spam filter** project.
10. `bayesian_networks`.

**Volume 36b: Modern Models**
11. `decision_trees_classification`.
12. `bagging_random_forest`.
13. `boosting`.
14. `glm`.
15. `clustering_k-means`.
16. `nn_regression`.
17. `nn_classification`.
18. `deep_learning`.
19. New: AI ethics and bias.

### What every ML chapter needs
- **Code.** Implement each method from scratch in NumPy (most are 20–40 lines), then show the scikit-learn one-liner. That moment, "the library is just doing what I did by hand," is where students fall in love with this material.
- **One dataset threaded through the unit**, so students can compare models on the same problem. The fish data from `bayes_classifier` already exists, and a school-relevant dataset would also work.
- **Figures.** Decision boundaries for k-NN, logistic regression, and trees; a real ROC curve; k-means iterations; a loss curve going down.
- **Exercises that require running code**, not just plugging into formulas.

### Misplaced material
- `stemming_lemmatization` sits in Vol 29 among calculus chapters. It belongs with the spam-filter project in the ML unit.

---

## 7. Exercise and engagement gaps

### Too few exercises for their length
| Chapter | Exercises | Words |
|---|---|---|
| `web_apis` | 1 | 4,047 |
| `kinematics` | 2 | 3,665 |
| `economics` | 2 | 4,770 |
| `boats_sailing` | 3 | 3,370 |
| `subspaces` | 2 | 3,071 |
| `linear_algebra_intro` | 2 | 2,461 |
| `bitmap` | 2 | 3,483 |
| `double_int_regions` | 1 | 1,631 |
| `pop_prop` | 1 | 1,049 |
| `numerical_multi_int` | 1 | 674 |
| `priority_queues` | 1 | 1,156 |
| `maps_location` | 1 | 1,426 |

`kinematics` in particular is a Volume 1 chapter: a new reader needs practice to build confidence.

### Missing exercise types
- **Challenge problems.** Mark one or two per chapter with a star, for students who want to be stretched.
- **"Explore" prompts.** Open-ended questions with no answer key, such as "Change the drag coefficient and see what happens," or "Find a data set about something you care about."

### A capstone project for each volume
Because each volume mixes subjects, a project can tie them together. Examples:
- **Vol 7:** design a catapult (projectiles + momentum).
- **Vol 18:** simulate a lunar mission (orbits + vector simulation + tides).
- **Vol 24:** a subway route planner (graphs + Dijkstra + priority queues).
- **Vol 31:** an engine efficiency calculator.
- **ML unit:** a spam filter, then a model built on the student's own data.

---

## 8. Cross-cutting improvements

1. **A prerequisite checker.** Each chapter's `digital_resources.json` already lists its prerequisites under `requires` (as `covers` ids). Write a script that checks them against the volume order and flags any prerequisite taught later, or any id that nothing covers. Every violation in Section 2 would have been caught automatically. (One example it would flag: `vectors`, in Vol 6, requires `span`, which is taught in Vol 21.) The same data can generate the "Before you start" box.
2. **"Before you start" and "Key ideas" boxes in every chapter**, generated from the prerequisite map and from `summary.md`.
3. **Consistent notation across the statistics chapters.** For example, the proportion is `p` in some chapters and `r` in others. Add a notation table to the appendix.
4. **An appendix volume**: statistical tables, Greek letters, units and prefixes, a formula sheet, a Python cheat sheet, and a glossary generated from the `\newterm` entries.
5. **Running code in one place.** Collect every `minted` listing into runnable files under `digital_resources`, with tests. During this pass I re-ran listings by hand to check their printed output. A test suite would catch drift automatically.
6. **Figure audit.** Some images are unused (the flight images, and `adityaOrbit.png`, `gimbalEngine.png`, and the `.ai` file in `vectors_matrices`). Some need regenerating (`artillery.png` in `drag`) or redrawing (the water phase diagram). Captions should be checked against the images.

---

## 9. Open items left from the editing pass

- The book_02 ordering (Section 2).
- `intro_dataviz` before `intro_python1`; `polynomials_1` before `pylists`.
- `bitmap` (Vol 23) uses hex, which is taught in Vol 26.
- Images: drag's `artillery.png` needs regenerating; the water phase diagram needs redrawing; several images are unused; `tidesSolution.png` is no longer referenced.
- Opinion statements flagged in `economics`, and data values to confirm.
- The orphan chapter `sql_2`.
- Content moved out of `random_variables` (now 582 words) to `int_methods` and `double_int_moments_average`; the move is logged in each chapter's summary. Merge the remainder as described in Section 3.

---

## 10. A possible roadmap

| Phase | Work | Effort |
|---|---|---|
| 1 | Prerequisite checker script; fix the Section 2 ordering problems; place the orphan chapter | Small. Mostly edits to `book_NN.txt`, plus a few rewritten passages |
| 2 | Merges from Section 4; appendix volume | Small to medium |
| 3 | Splits from Section 3; sections for single-section chapters | Medium |
| 4 | Rebuild the ML unit with code, figures, and one shared dataset | Large, and the highest payoff |
| 5 | New chapters, starting with digital logic and AI ethics | Large; can be done one chapter at a time |
| 6 | Capstone projects and challenge/explore problems | Ongoing |
