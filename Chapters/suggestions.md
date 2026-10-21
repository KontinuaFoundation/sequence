# Suggestions for the Next Pass

These suggestions come from editing and summarizing all 234 chapters in the 36 volumes. Word counts, exercise counts, and code and figure counts come from a script run over every `student.tex`. Prerequisite problems were confirmed by searching the text.

The series deliberately mixes physics, math, computer science, and statistics in every volume. That design is a strength: a curious student never stays in one subject long enough to get bored. The suggestions below keep that mix. They aim to fix the places where the mix breaks down: a chapter uses a tool before the student has it, a topic is taught three times, or a volume is one chapter long.

---

## 1. Top priorities

If you only do a few things, do these, in this order:

1. **Fix the prerequisite violations** (Section 2). A student who meets `sin θ` in Volume 1, or a derivative in Volume 17, decides the book is not for them. These are the cheapest high-value fixes.
2. **Rebuild the machine-learning unit in Volume 36** (Section 6). It has 19 chapters averaging about 480 words each, with no code and no figures. For many students this is the reason they picked up the series, and right now it is the thinnest part of it.
3. **Add a short "Before you start" box and a "Key ideas" box to every chapter.** The `summary.md` files already contain the key ideas, and the prerequisites can come from a dependency file (Section 8).
4. **Add the missing topics a curious teenager will ask about** (Section 5): cryptography, the trigonometry of non-right triangles, relativity, biology, digital logic, and AI ethics.
5. **Split the giant single-section chapters, and merge the duplicated ones** (Sections 3 and 4).

---

## 2. Reordering: prerequisite violations

Each item below is a place where a chapter uses something the student has not seen yet. I confirmed each one in the text.

| Where | Problem | Suggested fix |
|---|---|---|
| `kinematics` (Vol 1) | 7 Python/matplotlib listings; Python is taught in `intro_python1` (Vol 3) | Mark the code "Come back after the Python chapter," or move the plotting examples into `python_libraries` |
| `forces_motion` (Vol 1) | Uses sin/cos 16 times (inclined planes); trig arrives in Vol 6 | Add a short **Right-Triangle Trigonometry** chapter (SOH-CAH-TOA) to Vol 1, or move the inclined-plane section to after Vol 6 |
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
| Vol 27 | 2 | `matplotlib`, `maps_location` |
| Vol 36 | 27 | Larger than any three other volumes combined |

**Suggestions**
- Combine Volumes 25–27 into one "Data and the Web" volume, in this order: `data_representation`, `html`, a new CSS/JavaScript chapter, `web_apis`, `maps_location`. Move `matplotlib` much earlier (see Section 4).
- Move `numerical_multi_int` and `triple_integrals` from Vol 36 into Vol 35, which finishes multivariable integration.
- Split the rest of Vol 36 into two machine-learning volumes (Section 6).

### Orphaned chapters

Two complete chapters are not in any volume:
- **`log_transform`** (2,093 words). It belongs with the data-preparation chapters in the ML unit, or right after `num_methods_2`.
- **`sql_2`** (3,231 words; commented out in `book_14.txt`). Uncomment it or place it right after `sql_1`; multi-table joins are what make databases interesting.

---

## 3. Chapters that are too long and should be split

The book's chapters typically run 1,000–3,000 words. These chapters are well beyond that, often with only one `\section`, so a student has no natural stopping place.

| Chapter | Words | Sections | Proposed split |
|---|---|---|---|
| `forces_motion` (Vol 1) | 7,091 | 5 | **Newton's Laws** (the three laws, net force, normal force, free-body diagrams) / **Friction, Inclines, and Pulleys**. Move universal gravitation to `mass_weight_gravity` or `orbits`. |
| `gases_heat` (Vol 31) | 6,456 | 4 | **Temperature and the Gas Laws** / **Heat, Work, and the Laws of Thermodynamics**. Add entropy and the second law, which are currently missing. |
| `matter_energy` (Vol 2) | 6,330 | 2 | **Atoms and Chemical Bonds** / move the energy and E = mc² material into `energy_conservation` and a new nuclear-physics chapter. |
| `continuous_distributions` (Vol 30) | 5,633 | 6 | **CDFs, PDFs, and the Uniform Distribution** / **The Normal Distribution**. Move the multivariate normal next to `bayes_classifier` and `numerical_multi_int`, which reuse the snail data. |
| `data_tools` (Vol 3) | 5,227 | 3 | Keep it as **Spreadsheets**. Its mean/variance/standard-deviation material duplicates `num_methods` (Section 4). |
| `num_methods` (Vol 11) | 5,179 | 6 | **Center** / **Spread and Shape**. |
| `charge` (Vol 12) | 5,108 | 7 | **Electric Charge and Coulomb's Law** / **Electric Fields and Gauss's Law**. |
| `rotational_motion` (Vol 17) | 4,961 | **1** | **Torque and Equilibrium** / **Moment of Inertia and Angular Momentum**. It currently opens by reviewing rotational kinematics from `circular_motion`. |
| `circular_motion` (Vol 17) | 4,834 | **1** | **Uniform Circular Motion and Centripetal Force** / **Rotational Kinematics**. At minimum, add section headings. |
| `economics` (Vol 10) | 4,770 | 15 | **Markets: Trade, Supply, and Demand** / **Money, Investment, and Government**. It has only 2 exercises in 4,770 words; supply-and-demand equilibrium is algebra, so add numeric problems. |
| `data_representation` (Vol 26) | 4,740 | 5 | **Text and Integers** (ASCII/UTF-8, binary, hex, two's complement), which could move earlier as noted above / **Floating Point**. |
| `flight` (Vol 8) | 4,721 | 3 | **Airplanes** / **Quadcopters and Rockets**. It has 71 images, some of them unused. |
| `discrete_probability_counting` (Vol 28) | 4,463 | 3 | **Probability Rules** / **Counting**. Then merge the tiny `random_variables` (582 words) with the probability half and add the binomial and geometric distributions (Section 5). |
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
| **matplotlib** | `python_libraries` (Vol 4), `matplotlib` (Vol 27), plus ad hoc use in 10+ chapters | Merge them into one early plotting chapter in Vol 3 or 4. Later chapters already depend on it. |
| **Python classes** | `intro_python2` (Vol 4) and `classes` (Vol 16) | Keep the Polynomial class from `classes` as a section of `polynomials_1`. Drop the re-teaching. |
| **Python lists** | `intro_python1` (Vol 3) and `pylists` (Vol 16) | Same treatment: keep the coefficient-list material inside `polynomials_1`. |
| **Recursion** | `intro_python2`, `proofs` (induction), `sorting`, `recursion` (Vol 24) | Move `recursion` right after `intro_python2` and trim the recursion section in `intro_python2`, or cross-reference them. |
| **Span** | `linear_combo` (Vol 21) and `span` (Vol 22) | Merge into one chapter. |
| **AC circuits** | `ac` (Vol 12) and the AC/impedance half of `pendulums` (Vol 17) | Move impedance into `ac`. Keep a short "springs and circuits obey the same equation" box in `pendulums`. |
| **Sequences** | `sequences` (Vol 9) and the review opening of `seq_calc` (Vol 33) | Trim `seq_calc`'s re-introduction to a one-paragraph recap. |
| **Simple machines** | `simple_machines` and `machines_work` (both Vol 2) | Merge into one chapter on simple machines and mechanical advantage. |
| **Logistic regression** | `simple_logistic` + `multiv_logistic` (about 450 words each) | Merge. |
| **GLMs** | `glm` + `link_functions` (about 450 words each, overlapping) | Merge. |
| **Classifier evaluation** | `confusion` + `precision_recall_auc_roc` | Merge into "Evaluating Classifiers." |
| **Data preparation** | `standardization` (500 words) + `one-hot` (400) + orphan `log_transform` | Merge into "Preparing Data for Models." |
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

### Mathematics
1. **Number theory and cryptography.** Primes, divisibility, the Euclidean algorithm, modular arithmetic, and RSA. Only `sets` mentions primes, and no chapter covers encryption. This may be the single best hook for teenagers ("how does your phone keep secrets?"), and it ties to `proofs`, `data_representation`, and `hash_tables`.
2. **Right-triangle trigonometry, and the Law of Sines and Law of Cosines.** Neither law appears anywhere. They are needed for physics (forces, vectors) and for AP Precalculus.
3. **Euler's formula and the complex exponential**, e^{iθ} = cos θ + i sin θ. It falls naturally out of `taylor_series` and connects to `complex_numbers` and `ac`. It is the most famous equation in math, and it is missing.
4. **Fourier series and signals.** Breaking sound into sine waves ties together `sound`, `trig_functions`, `series`, `py_images` (JPEG), and `ac`. It also gives students a project they can hear.
5. **Lagrange multipliers.** These are needed for constrained optimization. `gradients_optimization` sets them up but stops short.
6. **Monte Carlo simulation**, as a chapter: estimating π, simulating Monty Hall and the birthday problem in Python. This would bridge `paradoxes` (Vol 10) and probability (Vol 28) without needing counting first.

### Statistics and probability
7. **Binomial and geometric distributions** as a proper chapter. The binomial appears only incidentally (in `pop_prop` and `glm`), and the geometric distribution does not appear at all. Both are on the AP Statistics exam.
8. **The Central Limit Theorem and sampling distributions**, with a simulation. The CLT currently gets a mention in `continuous_distributions`.
9. **Two-proportion inference.** Only means have two-sample procedures. AP Statistics requires both.
10. **Simulation-based inference** (bootstrap and permutation tests). It builds intuition before formulas and fits the Python thread. The bootstrap currently appears only inside `bagging_random_forest`.

### Physics
11. **Special relativity.** Time dilation needs only the Pythagorean theorem and algebra, and few topics excite curious students more.
12. **Nuclear physics and radioactivity.** Half-life appears inside other chapters. A real chapter would cover decay, fission and fusion (E = mc² is already in `matter_energy`), and a link to `exponentials_logarithms`.
13. **Waves, part two: the Doppler effect, interference, and diffraction** (including the double slit). Neither the Doppler effect nor wave interference has its own coverage; interference appears only in `paradoxes`.
14. **Fluids: Bernoulli's principle.** `flight` explains lift without Bernoulli, and `buoyancy` stops at statics.
15. **Entropy and the second law of thermodynamics.** No chapter states the second law, even though `engine` discusses efficiency. A Carnot efficiency section would complete the story.

### Chemistry
16. **Acids, bases, and pH.** pH is a perfect logarithm application, and the series has no chemistry beyond moles and bonding.
17. **Reaction rates and equilibrium** (Le Chatelier's principle). This would reuse `diff_eqs` and exponentials.

### Biology (currently almost absent)
18. **Epidemics: the SIR model.** It uses `diff_eqs`, `euler_method`, and Python, and every student lived through COVID.
19. **Genetics and probability.** Punnett squares, Hardy–Weinberg, and DNA as a 4-letter code (a link to `data_representation`).
20. **Neurons as circuits.** This connects `dc1` and `charge` to `nn_regression`, where artificial neurons came from.

### Computer science
21. **Digital logic: from transistors to adders.** Logic gates appear nowhere, yet the pieces are all present: `sets` (logic tables), `diodes` (transistors are mentioned), and `data_representation` (binary). A chapter that builds an adder from NAND gates answers "how does a computer actually compute?"
22. **CSS and JavaScript.** There is an `html` chapter and a Node server, but nothing to make a page look good or respond to clicks. Students want to build something they can show friends.
23. **How the internet works.** Packets, IP addresses, routing as shortest paths (`shortest_path`), and DNS. A natural partner to `web_apis`.
24. **Dynamic programming.** It is mentioned once, in `intro_markov`. Memoization is already in `recursion`, so a chapter on DP (making change, edit distance for spell-check) would be a small step.
25. **Multi-table databases.** Already written as the orphan `sql_2`.

### Thinking and society
26. **AI ethics and algorithmic bias.** The ML unit never discusses fairness, privacy, or what happens when a model is wrong about a person. `biases1` covers human cognitive bias; a companion chapter on machine bias belongs at the end of the ML unit.
27. **Personal finance.** Loans, credit-card interest, and saving. It reuses `exponentials_logarithms` and `seq_calc` (the savings recursion is already there), and every teenager will need it.
28. **Energy and climate.** The greenhouse effect mentions in `emwaves` and `gases_heat` could become a full chapter on where energy comes from, tying in photons, heat, engines, and economics.

---

## 6. The machine-learning unit (Volume 36)

**Current state:** 19 ML chapters averaging about 480 words each, with 0 code listings and 0 figures. The framing chapter comes after the methods, three topics are each split across two tiny chapters, and the neural-network chapters originally came after deep learning (now fixed). The topics are right; the chapters read like glossary entries.

### Proposed structure

**Volume 36a: Learning from Data**
1. `classification_regression`: what supervised learning is.
2. `train_val_test`.
3. Preparing data: `standardization` + `one-hot` + `log_transform`.
4. `least_squares` (with `simple_linear` merged in).
5. `lin_reg_gradient_descent`.
6. Logistic regression (`simple_logistic` + `multiv_logistic`).
7. Evaluating classifiers (`confusion` + `precision_recall_auc_roc`).
8. `knn_classifier`.
9. `bayes_classifier`, with the stemming material from Vol 29 turned into a **spam filter** project.
10. `bayesian_networks`.

**Volume 36b: Modern Models**
11. `decision_trees_classification`.
12. `bagging_random_forest`.
13. `boosting`.
14. GLMs (`glm` + `link_functions`).
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

1. **A prerequisite map.** Create a machine-readable file listing each chapter's prerequisites, plus a script that checks it against the volume order. Every violation in Section 2 would have been caught automatically. The same file can generate the "Before you start" box.
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
- The orphan chapters `log_transform` and `sql_2`.
- Content moved out of `random_variables` (now 582 words) to `int_methods` and `double_int_moments_average`; the move is logged in each chapter's summary. Merge the remainder as described in Section 3.

---

## 10. A possible roadmap

| Phase | Work | Effort |
|---|---|---|
| 1 | Prerequisite map and checker script; fix the Section 2 ordering problems; place the orphan chapters | Small. Mostly edits to `book_NN.txt`, plus a few rewritten passages |
| 2 | Merges from Section 4; appendix volume | Small to medium |
| 3 | Splits from Section 3; sections for single-section chapters | Medium |
| 4 | Rebuild the ML unit with code, figures, and one shared dataset | Large, and the highest payoff |
| 5 | New chapters, starting with cryptography, right-triangle trig and the laws of sines/cosines, digital logic, SIR epidemics, relativity, the binomial distribution and CLT, and AI ethics | Large; can be done one chapter at a time |
| 6 | Capstone projects and challenge/explore problems | Ongoing |
