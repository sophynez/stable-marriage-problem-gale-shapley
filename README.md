# Stable marriage problem

The Gale-Shapley algorithm is a well-known algorithm used to solve the stable marriage problem, which is a matching problem between two sets of elements (traditionally, men and women). The problem consists of finding a stable pairing of elements, such that no element prefers an element they are not paired with over the one they are paired with.

The algorithm works as follows:

  1. Each man proposes to the woman he prefers the most and has not yet proposed to.

  2. Each woman, upon receiving a proposal, accepts the proposal from the man she prefers the most among all the men who have proposed to her.

  3. If a woman accepts a proposal, the man who made the proposal is matched with that woman and removes all other women from his list.

   The process repeats until all men are matched with a woman, or it becomes impossible for any man to propose to a woman who has not yet received a proposal.

The Gale-Shapley algorithm is guaranteed to find a stable pairing. 
