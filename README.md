# voting-valhalla-r6
Program used for calculating Voting Valhalla R6 Results.

Code was done in Python 3.9; Python 3.8 required for geometric mean.

Coma Contestant results were calculated using the meandian.

The main results were calculated using the versus formula with **Ranked Pairs** voting used on the result matrix (done by hand.)

## Server Link
Visit the Voting Valhalla TWOW competition server via this link: https://discord.gg/jbSjZKGeBB

# Main Results
## Versus
Each contestant sent in two responses. Each voter gives out 3-2-1-0 points to these four responses from best to worst.
### Weighting Formula
To calculate the weight of the contestant's responses, all contestants were asked to submit a *Mult* between 0 and 1. This *Mult* would determine the weight of their higher and lower response when averaging. The higher the *Mult*, the more the lower response would count and the less the higher response would count.

Higher Response: 1 - (1 / 3) * (Mult ** 2)
Lower Response: (2 / 3) * Mult

The optimal *Mult* for each matchup is equal to (Lower Response Score / Higher Response Score). Since contestants could only pick one *Mult*, they cannot get it optimally for all matchups.

The final score is done by adding together the two responses' scores after they are weighted.

## Ranked Pairs
In Ranked Pairs Voting, victories are locked in from strongest to weakest. Transitivity is applied; if A > B and B > C, then A > C is also written in. If C > A appears later as a weaker matchup, it is ignored.

# Coma Contestant Results
## Per Voter
Each voter gave a score between 1 and 2 for each response. (For those who know normal TWOW voting: Add 1 to normal TWOW vote scores.) The contestants two responses were then averaged via Meandian.

The +1 is added so that a 0 score does not make the Meandian 0.

## Per Contestant
To get a contestant's final score, all of the Voter's Meandians are averaged using Meandian. After this process is done, subtract 1 from the score to get the final score between 0% and 100%.
