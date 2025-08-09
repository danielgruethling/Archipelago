from . import LWNTestBase

class TestGoals(LWNTestBase):
    options = { "goal": "vanilla" }

    def test_vanilla_goal(self) -> None:
        self.collect_all_but(["Lightning"])
        self.assertFalse(self.can_reach_location("Abyss - Nonota"))
        self.collect_by_name(["Lightning"])
        self.assertTrue(self.can_reach_location("Abyss - Nonota"))