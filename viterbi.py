
from utils import matrix

def viterbi(observations, model):
    states = model.states()
    d = matrix(len(states), len(observations), val = 0)

    # Step 1: Initialization
    for i, state in enumerate(states):
        d[i][0] = model.start(state) * model.emit(state, observations[0])

    # Step 2: Recursion
    for t in range(1, len(observations)):
        for j, curr_state in enumerate(states):
            for i, prev_state in enumerate(states):
                val = d[i][t - 1] * model.transition(prev_state, curr_state) * model.emit(curr_state, observations[t])
                if val > d[j][t]:
                    d[j][t] = val

    # Step 3: Traceback
    qs = []
    for t in reversed(range(len(observations))):
        best_state = None
        best_state_val = 0
        for i, state in enumerate(states):
            transition_prob = 1
            if t < len(observations) - 1:
                transition_prob = model.transition(state, qs[0])
            if d[i][t] * transition_prob > best_state_val:
                best_state_val = d[i][t] * transition_prob
                best_state = state
        qs.insert(0, best_state)

    return qs