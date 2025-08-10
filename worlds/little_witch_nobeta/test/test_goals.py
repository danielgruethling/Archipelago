from .bases import LWNTestBase


class TestVanillaGoal(LWNTestBase):
    options = { "goal": "vanilla" }

    def test_vanilla_goal(self) -> None:
        self.collect_all_but(["Thunder"])
        self.assertFalse(self.can_reach_location("Abyss - Nonota"))
        self.collect_by_name(["Thunder"])
        self.assertTrue(self.can_reach_location("Abyss - Nonota"))


class TestBossHuntGoal(LWNTestBase):
    options = {"goal": "boss_hunt"}

    def test_boss_hunt_goal(self) -> None:
        self.collect_all_but(["Specter Armor Soul", "Tania Soul", "Monica Soul", "Enraged Armor Soul", "Vanessa Soul", "Vanessa V2 Soul"])
        self.assertFalse(self.can_reach_location("Abyss - Nonota"))
        self.collect_by_name(["Specter Armor Soul", "Tania Soul", "Monica Soul", "Enraged Armor Soul", "Vanessa Soul", "Vanessa V2 Soul"])
        self.assertTrue(self.can_reach_location("Abyss - Nonota"))


class TestMagicMasterGoal(LWNTestBase):
    options = {"goal": "magic_master"}

    def test_magic_master_goal(self) -> None:
        self.collect_all_but(["Arcane", "Ice", "Fire", "Thunder"])