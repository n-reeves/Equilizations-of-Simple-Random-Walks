# Equilizations-of-Simple-Random-Walks
Script that simulates the long run behavior of simple random walks in 1,2,3 and 8 dimensions.

We can prove using moment generating equations and Stirling's formula for factorial approximation that the number of times an infinite simple random walk will return to the origin in one and two dimensions behaves in a significantly different way than a simple random walk in higher dimensions.

The results of the proof show that the a walk in 1 and 2 dimensions has probability of 1 of intersecting the origin an infinite number of times. Once the dimension increases, the probability that a xsimpel random walk will intersect the origin an infinite number of times is 0. More explicitly, the probability that a simple random walk of dimension 3 or greater will intersect the origin a finite number of times is 1.

The simulation models the average number of equalizations that a simple random walk has made by each step in the dimensions listed above. These averages are computed by simulating 1000 random walks of one million steps. The results are plotted against the number of steps that the walk has made.

For a more indepth description of the proof, referenec the paper "An Introduction to Random Walks" by Derek Johnston
