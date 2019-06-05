import random

def make_transition_dict(transitions):
    to_next = {}
    for start, end, prob in transitions:
        if start not in to_next:
            to_next[start] = [[], []]
        to_next[start][0].append(prob)
        to_next[start][1].append(end)
    return to_next

def markov_runout(transitions, start, num_steps):
    to_next = make_transition_dict(transitions)

    freq = {state : 0 for state in to_next}
    curr_state = start
    for _ in range(num_steps):
        freq[curr_state] += 1
        i = 0
        value = random.random()
        while value >= to_next[curr_state][0][i]:
            value -= to_next[curr_state][0][i]
            i += 1
        curr_state = to_next[curr_state][1][i]

    return freq

transitions = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
start = 'a'
num_steps = 5000
print(markov_runout(transitions, start, num_steps))