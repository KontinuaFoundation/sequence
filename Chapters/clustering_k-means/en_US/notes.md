# Clustering with k-Means — Notes

## Summary
Defines unsupervised learning and k-means: centroids that minimize total squared distance, the alternating assign and update steps, a worked example on the points 1, 2, 6, 8 with k = 2 (clusters {1, 2} and {6, 8}), and the elbow method for choosing k. It has two exercises (one iteration from centroids 2 and 7 gives the same clusters and centroids 1.5 and 7, and why to run k-means several times).

## Changes in this pass
- Added a high school link: splitting a class into project groups by interest.

## Checked and correct
- Worked example: from centroids 1 and 6, the assignments are {1, 2} and {6, 8}, and the centroids move to 1.5 and 7.
- Exercise km1: from centroids 2 and 7, the assignments are {1, 2} and {6, 8}; the new centroids are 1.5 and 7.

## Open items
- The algorithm section does not state the objective as a formula. Writing J = Σ‖x − c_{assign(x)}‖² would connect the text to the elbow plot.
- The worked example stops after one update. A line showing the second assignment would make the convergence check concrete.
