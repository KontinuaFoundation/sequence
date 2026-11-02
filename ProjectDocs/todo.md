# To-Do List

If you want to volunteer, here are some things we really need done. Before you
start, read [How to Write and Edit the Workbooks](writer.md).

## Writing

You can look through the books and find something missing, interesting and
useful. If you suggest it and volunteer to write it, we will probably OK it. The
[topic list](topic_list.md) and the [outline](outline.md) show what is planned
and what is already written.

That said, here are some topics that definitely need to be tackled:

* How colors separate when they are refracted: dispersion, prisms, rainbows and
  chromatic aberration
* Weather (Why is there wind? What is a high-pressure system? Why does it rain?)

Some chapters need splitting apart, because they cover topics that should come
later. Other chapters need merging, because they repeat each other.

## Problems and solutions

Every chapter needs at least six exercises with answers. As of November 2026,
157 of the 230 chapters have fewer than six.

The exercises and their answers go in the chapter's `student.tex`. The writer's
guide explains [how to write them](writer.md#exercises-and-answers).

Many chapters could also use more [worked problems](writer.md#worked-problems):
69 chapters have none.

Test problems are entered into the Mentoris web application. Besides a problem and
a solution, a test problem also needs a grading rubric. (This is being worked on
for supplemental quizzes.)

## Indexing

Every idea a chapter introduces should be in the index. Some chapters have very
few index entries: `work_kinetic_power`, `inv_trig_functions`, `log_transform`,
`electric_potential`, `limit_laws_ivt`, `circular_motion_2`,
`derivative_applications`, `riemann_python`, `int_methods`,
`integration_by_parts`, `double_int_polar` and `double_int_mass_center` each have
fewer than five.

Go through the chapter's `student.tex` and add an `\index` entry wherever an idea
is introduced. The [Style Guide](style.md#indexing) and the
[writer's guide](writer.md#new-terms-and-the-index) explain how.

## Figures

Every figure, whether a TikZ picture or an image, should be in a `figure`
environment with a caption and a label. See
[Figures and diagrams](writer.md#figures-and-diagrams) in the writer's guide.

## Digital resources

Every chapter has a `digital_resources.json`, but they need work:

* 156 of the 617 objectives have no video.
* 21 chapters do not list any objectives they cover.

`Build/check_ordering.py` currently finds no problems with the order of
prerequisites. Please run it after any change to a `requires` or `covers` list.

See [Digital Resources](digital_resources.md).

## Editing

Everything written so far is first-draft quality. We need editors to read it and
make it better.

## Fund-raising

Thus far, we have done a poor job raising funds. We would like to hire a
full-time writer, but we need a healthy endowment first.

Even if it is just asking your rich friends to write a check, we would appreciate
the help.
