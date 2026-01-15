from collections import deque

# Capacities of the jugs
CAPACITY_A = 4
CAPACITY_B = 3

def water_jug_bfs():
    """
    Solves the Water Jug Problem using Breadth First Search (BFS)
    and returns the sequence of states leading to the goal.
    """

    initial_state = (0, 0)
    goal_amount = 2

    queue = deque()
    queue.append((initial_state, [initial_state]))

    visited = set()
    visited.add(initial_state)

    while queue:
        (a, b), path = queue.popleft()

        # Goal check
        if a == goal_amount:
            return path

        # All possible next states
        next_states = [
            (CAPACITY_A, b),                  # Fill Jug A
            (a, CAPACITY_B),                  # Fill Jug B
            (0, b),                           # Empty Jug A
            (a, 0),                           # Empty Jug B
            (a - min(a, CAPACITY_B - b),      # Pour A -> B
             b + min(a, CAPACITY_B - b)),
            (a + min(b, CAPACITY_A - a),      # Pour B -> A
             b - min(b, CAPACITY_A - a))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None


if __name__ == "__main__":
    solution = water_jug_bfs()

    print("Sequence of steps to reach the goal:\n")
    for step in solution:
        print(step)
