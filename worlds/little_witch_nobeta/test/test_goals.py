from .bases import LWNTestBase


class TestVanillaGoal(LWNTestBase):
    options = { "goal": "vanilla" }

    def test_vanilla_goal(self) -> None:
        self.assertAccessDependency(["Abyss - Nonota"],
                                    [["Thunder", "Ice", "Arcane", "Fire"]], True)


class TestBossHuntGoal(LWNTestBase):
    options = {
        "goal": "boss_hunt",
        "randomize_boss_souls": "true"
    }

    def test_boss_hunt_goal(self) -> None:
        self.collect_all_but(["Specter Armor Soul", "Tania Soul", "Monica Soul", "Enraged Armor Soul",
                              "Vanessa Soul", "Vanessa V2 Soul", "Victory"])
        self.assertBeatable(False)
        self.collect_by_name(["Specter Armor Soul", "Tania Soul", "Monica Soul", "Enraged Armor Soul",
                              "Vanessa Soul", "Vanessa V2 Soul"])
        self.assertBeatable(True)


class TestMagicMasterGoal(LWNTestBase):
    options = {
        "goal": "magic_master",
        "no_arcane": "false"
    }

    def test_magic_master_goal(self) -> None:
        self.collect_all_but(["Arcane", "Ice", "Fire", "Thunder", "Victory"])
        self.assertBeatable(False)
        self.collect_by_name(["Arcane", "Ice", "Fire", "Thunder"])
        self.assertBeatable(True)