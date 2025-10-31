
# -------------------minimax-----------------------


import math


def minimax(level, position, isMax, outcomes, maxDepth):

    # Base case: if we reached the leaf node (bottom of the tree)
    if level == maxDepth:
        return outcomes[position]

    if isMax:  # MAX player's turn → pick the bigger value
        return max(
            minimax(level+1, position*2, False, outcomes, maxDepth),
            minimax(level+1, position*2+1, False, outcomes, maxDepth)
        )
    else:      # MIN player's turn → pick the smaller value
        return min(
            minimax(level+1, position*2, True, outcomes, maxDepth),
            minimax(level+1, position*2+1, True, outcomes, maxDepth)
        )


# Leaf scores (outcomes of the game)
outcomes = [3, 5, 2, 9, 12, 5, 23, 23]

# Depth of tree = log2(number of outcomes) → must be an integer
maxDepth = int(math.log(len(outcomes), 2))

print("The best value for MAX is:", minimax(0, 0, True, outcomes, maxDepth))



# --------------------alphabetaPruning---------------------------

import math


def alphabeta(level, position, isMax, outcomes, maxDepth, alpha, beta):
    # Base case: leaf node
    if level == maxDepth:
        return outcomes[position]

    if isMax:  # MAX player's turn
        best = -math.inf

        # Left child
        val = alphabeta(level+1, position*2, False,
                        outcomes, maxDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)
        if beta <= alpha:   # Prune
            return best

        # Right child
        val = alphabeta(level+1, position*2+1, False,
                        outcomes, maxDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)
        return best

    else:  # MIN player's turn
        best = math.inf

        # Left child
        val = alphabeta(level+1, position*2, True,
                        outcomes, maxDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)
        if beta <= alpha:   # Prune
            return best

        # Right child
        val = alphabeta(level+1, position*2+1, True,
                        outcomes, maxDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)
        return best


# Leaf scores (outcomes of the game)
outcomes = [3, 5, 2, 9, 12, 5, 23, 23]

# Depth of tree
maxDepth = int(math.log(len(outcomes), 2))

print("The best value for MAX is:", alphabeta(
    0, 0, True, outcomes, maxDepth, -math.inf, math.inf))
