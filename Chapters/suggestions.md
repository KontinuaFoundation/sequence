# Suggestions for the Next Pass

These suggestions come from editing and summarizing all 234 chapters in the 36 volumes. Word counts, exercise counts, and code and figure counts come from a script run over every `student.tex`. Prerequisite problems were confirmed by searching the text.

The series deliberately mixes physics, math, computer science, and statistics in every volume. That design is a strength: a curious student never stays in one subject long enough to get bored. The suggestions below keep that mix. They aim to fix the places where the mix breaks down: a chapter uses a tool before the student has it, a topic is taught three times, or a volume is one chapter long.

---

## 1. Top priorities

If you only do a few things, do these, in this order:

1. **Add a short "Before you start" box and a "Key ideas" box to every chapter.** The `summary.md` files already contain the key ideas, and the prerequisites can come from a dependency file (Section 8).
2. **Add the missing topics a curious teenager will ask about** (Section 5): AI ethics.
3. **Merge the duplicated material** (Section 4).

---

## 4. Superfluous or duplicated material: merge candidates

| Topic | Taught in | Suggestion |
|---|---|---|
| **Mean, variance, standard deviation** | `data_tools` (Vol 3) and `num_methods` (Vol 9) | `data_tools` now points ahead to `num_methods`. Removing its statistics section was considered and not done: the spreadsheet work and the bell-curve 68–95% rule depend on it, and `num_methods` comes six volumes later. Decide whether this early introduction should stay. |
| **Python classes** | `intro_python2` (Vol 4) and `classes` (Vol 14) | Keep the Polynomial class from `classes` as a section of `polynomials_1`. Drop the re-teaching. |
| **Python lists** | `intro_python1` (Vol 3) and `pylists` (Vol 14) | Same treatment: keep the coefficient-list material inside `polynomials_1`. |
| **Recursion** | `intro_python2`, `proofs` (induction), `sorting`, `recursion` (Vol 22) | Move `recursion` right after `intro_python2` and trim the recursion section in `intro_python2`, or cross-reference them. |
| **AC circuits** | `ac` (Vol 11) and the AC/impedance half of `pendulums` (Vol 16) | Move impedance into `ac`. Keep a short "springs and circuits obey the same equation" box in `pendulums`. |
| **Sequences** | `sequences` (Vol 8) and the review opening of `seq_calc` (Vol 29) | Trim `seq_calc`'s re-introduction to a one-paragraph recap. |
| **Greek alphabet** | `greek` (Vol 1, a reference table) | Move it to an appendix volume along with `stat_tables`, the unit tables from `units_conversions`, and a formula sheet. |
| **Experimental design** | `experiments` + `experimental_designs` (Vol 17) | Fine as two chapters, and both now have sections. Remove the vocabulary overlap. |

**Possibly superfluous for the target reader:**
- `positive-semidefinite` (Vol 21): Goemans–Williamson Max Cut with cvxpy is graduate-level. It is a fun "here be dragons" chapter. Keep it only if it is clearly labeled as optional enrichment.
- Parts of `linked_list_c` that cover allocator padding and alignment.
- The B-tree, trie, and suffix-tree survey in `trees`.

Mark these as optional rather than cutting them.

---

## 5. What is missing

These are ranked by how much a curious high school student would care, and by how well each topic reuses tools the series already teaches.

### Thinking and society
1. **AI ethics and algorithmic bias.** The ML unit never discusses fairness, privacy, or what happens when a model is wrong about a person. `biases1` covers human cognitive bias; a companion chapter on machine bias belongs at the end of the ML unit.
2. **Personal finance.** Loans, credit-card interest, and saving. It reuses `exponentials_logarithms` and `seq_calc` (the savings recursion is already there), and every teenager will need it.
3. **Energy and climate.** The greenhouse effect mentions in `emwaves` and `gases_heat` could become a full chapter on where energy comes from, tying in photons, heat, engines, and economics.

---

## 7. Exercise and engagement gaps

### Too few exercises for their length
| Chapter | Exercises | Words |
|---|---|---|
| `kinematics` | 2 | 3,665 |
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
- **Vol 16:** simulate a lunar mission (orbits + vector simulation + tides).
- **Vol 22:** a subway route planner (graphs + Dijkstra + priority queues).
- **Vol 28:** an engine efficiency calculator.
- **ML unit:** a model built on the student's own data.

---

## 8. Cross-cutting improvements

1. **"Before you start" and "Key ideas" boxes in every chapter**, generated from the prerequisite map and from `summary.md`.
2. **Consistent notation across the statistics chapters.** For example, the proportion is `p` in some chapters and `r` in others. Add a notation table to the appendix.
3. **An appendix volume**: statistical tables, Greek letters, units and prefixes, a formula sheet, a Python cheat sheet, and a glossary generated from the `\newterm` entries.
4. **Running code in one place.** Collect every `minted` listing into runnable files under `digital_resources`, with tests. During this pass I re-ran listings by hand to check their printed output. A test suite would catch drift automatically.
5. **Figure audit.** Some images are unused (the flight images, and `adityaOrbit.png`, `gimbalEngine.png`, and the `.ai` file in `vectors_matrices`). Some need regenerating (`artillery.png` in `drag`) or redrawing (the water phase diagram). Captions should be checked against the images.

---

## 9. Open items left from the editing pass

- Images: drag's `artillery.png` needs regenerating; the water phase diagram needs redrawing; several images are unused; `tidesSolution.png` is no longer referenced.

---

## 10. A possible roadmap

| Phase | Work | Effort |
|---|---|---|
| 1 | Merges from Section 4; appendix volume | Small to medium |
| 2 | New chapters, starting with AI ethics | Large; can be done one chapter at a time |
| 3 | Capstone projects and challenge/explore problems | Ongoing |
