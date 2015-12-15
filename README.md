# 1D Random Walk

## Simulation Set-up

There are `N` particles that can move in one dimension. During one time step a particle can move one particle width to the left with probability `pLeft`, or to the right with probability `pRight`.

- The probabilities sum to 1 and the difference between `pRight` and `pLeft` is referred to as the drift velocity.
- Particles move in discrete units of distance equal to one particle width.
- Particles may not occupy the same position at the same time.
- Particles are initialized one particle-width apart from one another.

The simulation tracks the center of mass (COM) of the `N` particles and records the time where the COM has traveled a threshold distance `L`.

## Code

There are two implementations, one in `fortran` and the other in `python`. Both seem to produce similar results.
