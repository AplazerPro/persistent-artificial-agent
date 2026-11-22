import unittest

from experiment_001.q_learning import QLearningAgent


class TestQLearningAgent(unittest.TestCase):
    def test_terminal_update(self):
        agent = QLearningAgent(learning_rate=0.5, discount_factor=0.9)
        updated = agent.update("s", "WAIT", reward=10, next_state="end",
                               next_actions=[], terminal=True)
        self.assertEqual(updated, 5.0)

    def test_non_terminal_update(self):
        agent = QLearningAgent(learning_rate=1.0, discount_factor=0.5)
        agent.q_values["next"]["EAT"] = 8.0
        updated = agent.update("current", "MOVE", reward=-1,
                               next_state="next", next_actions=["EAT"])
        self.assertEqual(updated, 3.0)

    def test_invalid_learning_rate(self):
        with self.assertRaises(ValueError):
            QLearningAgent(learning_rate=0, discount_factor=0.9)

    def test_empty_action_list(self):
        agent = QLearningAgent(learning_rate=0.1, discount_factor=0.9)
        with self.assertRaises(ValueError):
            agent.greedy_action("s", [])


if __name__ == "__main__":
    unittest.main()
