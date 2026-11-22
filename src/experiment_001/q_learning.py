"""Small, dependency-free tabular Q-learning implementation.

This module deliberately does not define the environment, reward function,
state representation, or exploration policy. Those belong to separate,
versioned experiment components.
"""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict, Hashable, Iterable


State = Hashable
Action = str


class QLearningAgent:
    """A minimal Q-table with an explicit update rule."""

    def __init__(self, learning_rate: float, discount_factor: float) -> None:
        if not 0.0 < learning_rate <= 1.0:
            raise ValueError("learning_rate must be in (0, 1].")
        if not 0.0 <= discount_factor <= 1.0:
            raise ValueError("discount_factor must be in [0, 1].")

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_values: DefaultDict[State, dict[Action, float]] = defaultdict(dict)
        self.update_count = 0

    def value(self, state: State, action: Action) -> float:
        """Return the current estimate; unseen state-action pairs start at 0."""
        return self.q_values[state].get(action, 0.0)

    def available_values(
        self, state: State, actions: Iterable[Action]
    ) -> dict[Action, float]:
        """Return Q-values for the actions available in this state."""
        return {action: self.value(state, action) for action in actions}

    def greedy_action(self, state: State, actions: Iterable[Action]) -> Action:
        """Choose a highest-valued action; ties are resolved deterministically.

        This is a baseline utility, not a complete exploration policy.
        """
        candidates = list(actions)
        if not candidates:
            raise ValueError("At least one available action is required.")
        values = self.available_values(state, candidates)
        best_value = max(values.values())
        return next(action for action in candidates if values[action] == best_value)

    def update(
        self,
        state: State,
        action: Action,
        reward: float,
        next_state: State,
        next_actions: Iterable[Action],
        terminal: bool = False,
    ) -> float:
        """Apply one Q-learning update and return the updated Q-value."""
        old_value = self.value(state, action)

        if terminal:
            target = reward
        else:
            next_action_list = list(next_actions)
            best_future = (
                max(self.value(next_state, candidate) for candidate in next_action_list)
                if next_action_list
                else 0.0
            )
            target = reward + self.discount_factor * best_future

        updated = old_value + self.learning_rate * (target - old_value)
        self.q_values[state][action] = updated
        self.update_count += 1
        return updated

    def export_table(self) -> list[dict[str, object]]:
        """Return a JSON-serializable representation for checkpointing."""
        rows: list[dict[str, object]] = []
        for state, actions in self.q_values.items():
            for action, value in actions.items():
                rows.append(
                    {"state": repr(state), "action": action, "q_value": value}
                )
        return rows
