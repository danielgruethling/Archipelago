from typing import TYPE_CHECKING

from .options import (
    Toggle,
    MagicPuzzleGateBehaviour,
    ShortcutGateBehaviour,
    WindRequirements,
    TrialKeys,
    Goal,
    AbyssTrialRequirement,
    RandomizeLore,
    BossRequirementsDifficulty,
    SkipsInLogic,
    DisableDarkTunnelThunderWall,
    DisableDarkTunnelBridgeCollapse,
    RandomizeBossSouls,
    SkippableBosses, StartingArea,
)
from rule_builder.rules import Has, HasAny, HasAll, HasAllCounts, HasGroup, HasGroupUnique, CanReachRegion, True_
from rule_builder.options import OptionFilter

if TYPE_CHECKING:
    from . import LWNWorld


has_fire_or_thunder = HasAny("Fire", "Thunder")
has_wind_or_skip = Has("Wind") | [OptionFilter(WindRequirements, WindRequirements.option_less_wind_requirements)]
has_wind_or_damage_boost = Has("Wind") | (Has("Fire") & [OptionFilter(WindRequirements, WindRequirements.option_less_wind_requirements)])
has_goal_requirements = ((HasAllCounts({"Arcane": 5, "Fire": 5, "Thunder": 5, "Ice": 5})
                         & [OptionFilter(Goal, Goal.option_magic_master)])
                         | (HasAll("Specter Armor Token", "Tania Token", "Monica Token", "Enraged Armor Token",
                                   "Vanessa Token", "Vanessa V2 Token") & [OptionFilter(Goal, Goal.option_boss_hunt)])
                         | (HasGroupUnique("Lore", 99) & [OptionFilter(Goal, Goal.option_lore_keeper), OptionFilter(RandomizeLore, RandomizeLore.option_vanilla), OptionFilter(StartingArea, StartingArea.option_shrine, operator="ne")])
                         | (HasGroupUnique("Lore", 102) & [OptionFilter(Goal, Goal.option_lore_keeper), OptionFilter(RandomizeLore, RandomizeLore.option_vanilla)])
                         | (HasGroupUnique("Lore", 103) & [OptionFilter(Goal, Goal.option_lore_keeper), OptionFilter(RandomizeLore, RandomizeLore.option_randomized)])
                         | [OptionFilter(Goal, Goal.option_vanilla)])
has_abyss_trial_requirements = ((HasAllCounts({"Arcane": 5, "Fire": 5, "Thunder": 5, "Ice": 5})
                         & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_magic_master)])
                         | (HasAll("Specter Armor Token", "Tania Token", "Monica Token", "Enraged Armor Token",
                                   "Vanessa Token", "Vanessa V2 Token") & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_boss_hunt)])
                         | (HasGroupUnique("Lore", 102) & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_lore_keeper), OptionFilter(RandomizeLore, RandomizeLore.option_vanilla)])
                         | (HasGroupUnique("Lore", 103) & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_lore_keeper), OptionFilter(RandomizeLore, RandomizeLore.option_randomized)])
                         | (Has("Abyss Underground Trial Clear") & Has("Abyss Lava Ruins Trial Clear") & Has("Abyss Dark Tunnel Trial Clear") & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_randomized_item)])
                         | (Has("Abyss Underground Trial Clear") & Has("Abyss Lava Ruins Trial Clear") & Has("Abyss Dark Tunnel Trial Clear") & [OptionFilter(AbyssTrialRequirement, AbyssTrialRequirement.option_vanilla)]))


def has_barrier(barrier: str):
    return (Has(barrier, options=[OptionFilter(MagicPuzzleGateBehaviour, MagicPuzzleGateBehaviour.option_randomized)])
            | [OptionFilter(MagicPuzzleGateBehaviour, MagicPuzzleGateBehaviour.option_always_open)])


def has_gate(gate: str):
    return (Has(gate, options=[OptionFilter(ShortcutGateBehaviour, ShortcutGateBehaviour.option_randomized)])
            | [OptionFilter(ShortcutGateBehaviour, ShortcutGateBehaviour.option_always_open)])


barrier_vanilla = [OptionFilter(MagicPuzzleGateBehaviour, MagicPuzzleGateBehaviour.option_vanilla)]
barrier_randomized = [OptionFilter(ShortcutGateBehaviour, ShortcutGateBehaviour.option_randomized)]
gate_vanilla = [OptionFilter(ShortcutGateBehaviour, ShortcutGateBehaviour.option_vanilla)]
boss_req_easy = True_() & [OptionFilter(BossRequirementsDifficulty, BossRequirementsDifficulty.option_easy)]
boss_req_normal = True_() & [OptionFilter(BossRequirementsDifficulty, BossRequirementsDifficulty.option_normal)]
boss_req_absorption = True_() & [OptionFilter(BossRequirementsDifficulty, BossRequirementsDifficulty.option_absorption_only)]
boss_req_none = True_() & [OptionFilter(BossRequirementsDifficulty, BossRequirementsDifficulty.option_no_requirements)]
boss_souls_vanilla = True_() & [OptionFilter(RandomizeBossSouls, False)]
skip_boss_enabled = True_() & [OptionFilter(SkippableBosses, True)]


def set_region_rules(world: "LWNWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    world.set_rule(multiworld.get_entrance("Shrine - Start -> Shrine - After first magic switch", player),
                   (has_barrier("Shrine First Magic Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Shrine - After first magic switch -> Shrine - Cat Room", player),
                   (has_barrier("Shrine Second Magic Barrier")
                       | (HasAny("Arcane", "Thunder")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Shrine - After first magic switch -> Shrine - Start", player),
                   has_barrier("Shrine First Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Shrine - Cat Room -> Shrine - After first magic switch", player),
                   has_barrier("Shrine Second Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Shrine - Cat Room -> Shrine - Armor Hall", player),
                   (has_barrier("Shrine Meet Cat Magic Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Secret passage - Start", player),
                   (has_barrier("Secret Passage Entrance Magic Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Secret passage - After first fire barrier", player),
                   has_gate("Shrine Secret Area Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Secret Passage - Boss Shortcut", player),
                   has_gate("Shrine Secret Boss Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Shrine - Underground shortcut", player),
                   has_gate("Shrine Underground Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Shrine - Cat Room", player),
                   has_barrier("Shrine Meet Cat Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Shrine - Armor Hall -> Underground - Start", player),
                   (skip_boss_enabled
                       | ((boss_souls_vanilla
                       | Has("Specter Armor Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics"))))))
    world.set_rule(multiworld.get_entrance("Shrine - Underground shortcut -> Shrine - Armor Hall", player),
                   (has_gate("Shrine Underground Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Shrine - Underground shortcut -> Underground - Shrine shortcut", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Secret passage - Start -> Shrine - Armor Hall", player),
                   has_barrier("Secret Passage Entrance Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Secret passage - Start -> Secret passage - After first fire barrier", player),
                   (has_barrier("Secret Passage First Fire Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Secret passage - After first fire barrier -> Secret passage - Start", player),
                   has_barrier("Secret Passage First Fire Barrier"))
    world.set_rule(multiworld.get_entrance("Secret passage - After first fire barrier -> Secret Passage - Dark Tunnel shortcut", player),
                   has_gate("Secret Passage Dark Tunnel Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Secret passage - After first fire barrier -> Shrine - Armor Hall", player),
                   (has_gate("Shrine Secret Area Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Secret passage - After first fire barrier -> Secret Passage - Before Enraged Armor", player),
                   (has_barrier("Secret Passage Second Fire Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Secret Passage - Before Enraged Armor -> Secret passage - After first fire barrier", player),
                   (has_barrier("Secret Passage Second Fire Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Secret Passage - Before Enraged Armor -> Secret Passage - Enraged Armor", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Secret Passage - Enraged Armor -> Secret Passage - Boss Shortcut", player),
                   (has_barrier("Defeat Enraged Armor Barrier")
                       | ((boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption")))
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Secret Passage - Enraged Armor -> Secret Passage - Before Enraged Armor", player),
                   (skip_boss_enabled
                       | ((boss_souls_vanilla
                       | Has("Enraged Armor Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption"))))))
    world.set_rule(multiworld.get_entrance("Secret Passage - Boss Shortcut -> Shrine - Armor Hall", player),
                   (has_gate("Shrine Secret Boss Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Secret Passage - Boss Shortcut -> Secret Passage - Enraged Armor", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Secret Passage - Dark Tunnel shortcut -> Dark Tunnel - After bridge collapse", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Secret Passage - Dark Tunnel shortcut -> Secret passage - After first fire barrier", player),
                   (has_gate("Secret Passage Dark Tunnel Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Underground - Start -> Underground - After wind", player),
                   (Has("Wind")
                       | [OptionFilter(SkipsInLogic, "Underground Wind Skip", "contains")]))
    world.set_rule(multiworld.get_entrance("Underground - Start -> Shrine - Armor Hall", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Underground - After wind -> Underground - Grand Hall", player),
                   (has_barrier("Underground Magic Barrier At Maid Enemy")
                       | (Has("Ice")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Underground - After wind -> Underground - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Underground - Grand Hall -> Underground - After fire", player),
                   Has("Ice"))
    world.set_rule(multiworld.get_entrance("Underground - Grand Hall -> Underground - After wind", player),
                   has_barrier("Underground Magic Barrier At Maid Enemy"))
    world.set_rule(multiworld.get_entrance("Underground - Grand Hall -> Underground - Lava ruins shortcut", player),
                   has_gate("Underground Lava Ruins Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Underground - Grand Hall -> Underground - Shrine shortcut", player),
                   has_gate("Underground Lava Ruins Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Underground - Grand Hall -> Underground - Tania shortcut", player),
                   has_gate("Underground Tania Shortcut Gate On Grand Hall Side"))
    world.set_rule(multiworld.get_entrance("Underground - Lava ruins shortcut -> Underground - Grand Hall", player),
                   (has_gate("Underground Lava Ruins Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Underground - Lava ruins shortcut -> Underground - Shrine shortcut", player),
                   (has_gate("Underground Lava Ruins Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Underground - Lava ruins shortcut -> Lava Ruins - Path to dark tunnel", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Underground - Shrine shortcut -> Underground - Grand Hall", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Underground - Shrine shortcut -> Underground - Lava ruins shortcut", player),
                   has_gate("Underground Lava Ruins Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Underground - Shrine shortcut -> Shrine - Underground shortcut", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Underground - Tania shortcut -> Underground - Grand Hall", player),
                   (has_gate("Underground Tania Shortcut Gate On Grand Hall Side")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Underground - Tania shortcut -> Underground - Tania", player),
                   has_gate("Underground Tania Shortcut Gate On Tania Side"))
    world.set_rule(multiworld.get_entrance("Underground - After fire -> Underground - After fire magic switch barrier", player),
                   (has_barrier("Underground Fire Barrier Magic Barrier")
                       | (Has("Ice")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Underground - After fire -> Underground - Grand Hall", player),
                   Has("Ice"))
    world.set_rule(multiworld.get_entrance("Underground - After fire magic switch barrier -> Underground - Tania", player),
                   (has_barrier("Underground Enemy Magic Barrier")
                       | barrier_vanilla
                       | [OptionFilter(SkipsInLogic, "Underground Barrier Before Tania Skip", "contains")]))
    world.set_rule(multiworld.get_entrance("Underground - After fire magic switch barrier -> Underground - After fire", player),
                   has_barrier("Underground Fire Barrier Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Underground - Tania -> Underground - Tania shortcut", player),
                   (has_gate("Underground Tania Shortcut Gate On Tania Side")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Underground - Tania -> Underground - After fire magic switch barrier", player),
                   (has_barrier("Underground Enemy Magic Barrier")
                       | (barrier_vanilla
                       & HasAny("Arcane", "Thunder", "Fire"))))
    world.set_rule(multiworld.get_entrance("Underground - Tania -> Lava Ruins - Start", player),
                   ((has_barrier("Underground Tania Arena Barrier")
                       | barrier_vanilla)
                       & (skip_boss_enabled
                       | ((boss_souls_vanilla
                       | Has("Tania Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 3)
                       & Has("Mana Absorption")))))))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - After magic platforms", player),
                   (has_barrier("Lava Ruins Magic Platforms")
                       | has_gate("Lava Ruins Fake Floor Shortcut Gate")
                       | barrier_vanilla
                       | ([OptionFilter(SkipsInLogic, "Lava Ruins Platforms Skip", "contains")]
                       & Has("Wind"))))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - Monica warp", player),
                   has_gate("Lava Ruins Monica Warp Gate"))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - Path to dark tunnel", player),
                   (HasAny("Wind", "Fire", "Thunder")
                       & [OptionFilter(SkipsInLogic, "Lava Ruins Monica Skip", "contains")]))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After magic platforms -> Lava Ruins - After scissor enemy barrier", player),
                   (has_barrier("Lava Ruins Scissor Enemy Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After magic platforms -> Lava Ruins - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - After magic platforms -> Lava Ruins - Scissor Enemy Room", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Scissor Enemy Room -> Lava Ruins - After magic platforms", player),
                   (has_barrier("Lava Ruins Scissor Enemy Lift")
                       | (barrier_vanilla
                       & Has("Arcane"))))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Scissor Enemy Room -> Lava Ruins - After scissor enemy barrier", player),
                   (has_barrier("Lava Ruins Scissor Enemy Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Scissor Enemy Room -> Lava Ruins - Lift Magic Switch Room", player),
                   (has_barrier("Lava Ruins Scissor Enemy Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Scissor Enemy Room -> Lava Ruins - Scissor Enemy Battle", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - After Fire Barrier", player),
                   (has_barrier("Lava Ruins Fire Magic Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - After Moving Ring", player),
                   has_gate("Lava Ruins Monica Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - Scissor Enemy Room", player),
                   (has_barrier("Lava Ruins Scissor Enemy Barrier")
                       | (barrier_vanilla
                       & Has("Arcane"))))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - Lift Magic Switch Room", player),
                   Has("Arcane"))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - Scissor Enemy Battle", player),
                   HasAny("Arcane", "Ice", "Thunder"))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Lava Ruins - After scissor enemy barrier", player),
                   has_barrier("Lava Ruins Fire Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Lava Ruins - Lava Ring Activation", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Lava Ruins - After Moving Ring", player),
                   (has_barrier("Lava Ruins Moving Ring")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Moving Ring -> Lava Ruins - After Fire Barrier", player),
                   (has_barrier("Lava Ruins Moving Ring")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Moving Ring -> Lava Ruins - After scissor enemy barrier", player),
                   (has_gate("Lava Ruins Monica Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Moving Ring -> Lava Ruins - Monica", player),
                   has_wind_or_damage_boost)
    world.set_rule(multiworld.get_entrance("Lava Ruins - After Moving Ring -> Lava Ruins - Lava Ring Activation", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Monica -> Lava Ruins - After Fire Barrier", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Monica -> Lava Ruins - Monica warp", player),
                   ((has_barrier("Lava Ruins Monica Arena Barrier")
                       | barrier_vanilla)
                       & (boss_souls_vanilla
                       | Has("Monica Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 4)
                       & Has("Mana Absorption")))))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Monica warp -> Lava Ruins - Path to dark tunnel", player),
                   (has_gate("Lava Ruins Monica Warp Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Monica warp -> Lava Ruins - Start", player),
                   (has_gate("Lava Ruins Monica Warp Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Underground - Lava ruins shortcut", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Lava Ruins - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Dark Tunnel - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Underground - Tania", player),
                   (has_barrier("Underground Tania Arena Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - Start -> Dark Tunnel - After first magic barrier", player),
                   (has_barrier("Dark Tunnel First Magic Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - Start -> Lava Ruins - Path to dark tunnel", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Dark Tunnel - Start -> Dark Tunnel - After first gate", player),
                   (Has("Wind")
                       | [OptionFilter(SkipsInLogic, "Dark Tunnel Hat Skip", "contains")]))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After first magic barrier -> Dark Tunnel - Start", player),
                   has_barrier("Dark Tunnel First Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After first magic barrier -> Dark Tunnel - After first gate", player),
                   (has_gate("Dark Tunnel First Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After first gate -> Dark Tunnel - After first magic barrier", player),
                   has_gate("Dark Tunnel First Gate"))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After first gate -> Dark Tunnel - After light switch barrier", player),
                   (has_barrier("Dark Tunnel Light Switch Barrier")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After first gate -> Dark Tunnel - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After light switch barrier -> Dark Tunnel - Thunder barrier", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After light switch barrier -> Dark Tunnel - Start", player),
                   has_barrier("Dark Tunnel Light Switch Barrier"))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - Thunder barrier -> Dark Tunnel - After light switch barrier", player),
                   ((Has("Thunder")
                       | [OptionFilter(DisableDarkTunnelThunderWall, Toggle.option_true)])))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - Thunder barrier -> Dark Tunnel - After thunder barrier", player),
                   ((has_barrier("Dark Tunnel Thunder Barrier")
                       | barrier_vanilla)
                       & (Has("Thunder")
                       | [OptionFilter(DisableDarkTunnelThunderWall, Toggle.option_true)])))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After thunder barrier -> Dark Tunnel - Thunder barrier", player),
                   (has_barrier("Dark Tunnel Thunder Barrier")
                       & (Has("Thunder")
                       | [OptionFilter(DisableDarkTunnelThunderWall, Toggle.option_true)])))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After thunder barrier -> Dark Tunnel - After floating platforms", player),
                   ((has_barrier("Dark Tunnel Floating Platform One")
                       & has_barrier("Dark Tunnel Floating Platform Two")
                       & has_barrier("Dark Tunnel Floating Platform Three"))
                       | Has("Wind")
                       | (Has("Thunder")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After floating platforms -> Dark Tunnel - After thunder barrier", player),
                   ((has_barrier("Dark Tunnel Floating Platform One")
                       & has_barrier("Dark Tunnel Floating Platform Two")
                       & has_barrier("Dark Tunnel Floating Platform Three"))
                       | Has("Wind")
                       | barrier_vanilla))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After floating platforms -> Dark Tunnel - After bridge collapse", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After bridge collapse -> Spirit Realm - Start", player),
                   (skip_boss_enabled
                       | ((boss_souls_vanilla
                       | Has("Vanessa Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption"))))))
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After bridge collapse -> Secret Passage - Dark Tunnel shortcut", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Dark Tunnel - After bridge collapse -> Dark Tunnel - After floating platforms", player),
                   (True_()
                       & [OptionFilter(DisableDarkTunnelBridgeCollapse, Toggle.option_true)]))
    world.set_rule(multiworld.get_entrance("Spirit Realm - Start -> Spirit Realm - After platforms", player),
                   Has("Wind"))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - Start", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - After second Seal", player),
                   has_gate("Spirit Realm Statue Shortcut Gate"))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - After arcane barrier", player),
                   (has_barrier("Spirit Realm Arcane Barrier")
                       | (Has("Wind")
                       & has_barrier("Spirit Realm Platform Shortcut"))
                       | (Has("Arcane")
                       & barrier_vanilla)
                       | (Has("Wind")
                       & [OptionFilter(SkipsInLogic, "Spirit Realm Arcane Barrier Skip", "contains")])))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After arcane barrier -> Spirit Realm - After platforms", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Spirit Realm - After arcane barrier -> Spirit Realm - Seal", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Spirit Realm - Seal -> Spirit Realm - After first Seal", player),
                   (has_barrier("Spirit Realm First Seal Magic Barrier")
                       | (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption"))
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After first Seal -> Spirit Realm - Seal", player),
                   has_barrier("Spirit Realm First Seal Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After first Seal -> Spirit Realm - After second Seal", player),
                   (has_barrier("Spirit Realm Second Seal Magic Barrier")
                       | (Has("Wind")
                       & [OptionFilter(SkipsInLogic, "Spirit Realm Seal Barrier Skip", "contains")])
                       | (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption"))
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After first Seal", player),
                   has_barrier("Spirit Realm Second Seal Magic Barrier"))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After elevator", player),
                   (has_barrier("Spirit Realm Elevator")
                       | (HasGroup("Attack Magics")
                       & barrier_vanilla)
                       | (Has("Wind")
                       & [OptionFilter(SkipsInLogic, "Spirit Realm Elevator Skip", "contains")])))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After platforms", player),
                   (has_gate("Spirit Realm Statue Shortcut Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After elevator -> Spirit Realm - After teleport", player),
                   (has_barrier("Spirit Realm Teleporter")
                       | (HasAny("Ice", "Thunder")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Spirit Realm - After elevator -> Spirit Realm - After second Seal", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Spirit Realm - After teleport -> Spirit Realm - After elevator", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Spirit Realm - After teleport -> Abyss", player),
                   (skip_boss_enabled
                       | ((boss_souls_vanilla
                       | Has("Vanessa V2 Soul"))
                       & (boss_req_none
                       | (boss_req_absorption
                       & Has("Mana Absorption"))
                       | (boss_req_normal
                       & HasGroup("Attack Magics")
                       & Has("Mana Absorption"))
                       | (boss_req_easy
                       & HasGroup("Attack Magics", 5)
                       & Has("Mana Absorption"))))))
    world.set_rule(multiworld.get_entrance("Abyss -> Abyss - After first teleport", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Abyss - After first teleport -> Abyss - After first gate", player),
                   (has_gate("Abyss First Gate")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Abyss - After first gate -> Abyss - After giant maid barrier", player),
                   (has_barrier("Abyss After Giant Maid Barrier")
                       | (HasGroup("Attack Magics")
                       & barrier_vanilla)
                       | (Has("Wind")
                       & [OptionFilter(SkipsInLogic, "Abyss Giant Maid Skip", "contains")])))
    world.set_rule(multiworld.get_entrance("Abyss - After first gate -> Abyss - Trap gate", player),
                   (has_gate("Abyss Trap Gates")
                       | gate_vanilla))
    world.set_rule(multiworld.get_entrance("Abyss - Trap gate -> Abyss - After first gate", player),
                   has_gate("Abyss Trap Gates"))
    world.set_rule(multiworld.get_entrance("Abyss - After giant maid barrier -> Abyss - Trials Lobby", player),
                   True_())
    world.set_rule(multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Underground Trial", player),
                   Has("Trial Key", count=3, options=[OptionFilter(TrialKeys, Toggle.option_true)], filtered_resolution=True))
    world.set_rule(multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Lava Ruins Trial", player),
                   Has("Trial Key", count=3, options=[OptionFilter(TrialKeys, Toggle.option_true)], filtered_resolution=True))
    world.set_rule(multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Dark Tunnel Trial", player),
                   Has("Trial Key", count=3, options=[OptionFilter(TrialKeys, Toggle.option_true)], filtered_resolution=True))
    world.set_rule(multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Nonota", player),
                   has_abyss_trial_requirements)
    world.set_rule(multiworld.get_entrance("Abyss - Underground Trial -> Abyss - Underground Trial magic switch", player),
                   (has_barrier("Abyss Underground Trial Exit Barrier")
                       | (has_fire_or_thunder
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Abyss - Underground Trial magic switch -> Abyss - Trials Lobby", player),
                   (has_barrier("Abyss Underground Trial Magic Switch")
                       | [OptionFilter(SkipsInLogic, "Abyss Underground Trial Barrier Skip", "contains")]))
    world.set_rule(multiworld.get_entrance("Abyss - Dark Tunnel Trial -> Abyss - Dark Tunnel Trial magic switch", player),
                   (has_barrier("Abyss Dark Tunnel Trial Maid Enemy Barrier")
                       | (Has("Thunder")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Abyss - Dark Tunnel Trial magic switch -> Abyss - Trials Lobby", player),
                   has_barrier("Abyss Dark Tunnel Trial Magic Switch"))
    world.set_rule(multiworld.get_entrance("Abyss - Lava Ruins Trial -> Abyss - Lava Ruins Trial magic switch", player),
                   ((has_barrier("Abyss Lava Ruins Trial Lower Lava")
                       & has_barrier("Abyss Lava Ruins Trial Maid Enemy Barrier"))
                       | (HasGroup("Attack Magics")
                       & barrier_vanilla)))
    world.set_rule(multiworld.get_entrance("Abyss - Lava Ruins Trial magic switch -> Abyss - Trials Lobby", player),
                   has_barrier("Abyss Lava Ruins Trial Magic Switch"))


def set_location_rules(world: "LWNWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Shrine - Second magic switch", player),
                 HasAny("Arcane", "Thunder"))
    world.set_rule(multiworld.get_location("Shrine - Specter Armor", player),
             (boss_souls_vanilla
             | Has("Specter Armor Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics"))
             | (boss_req_easy
             & HasGroup("Attack Magics"))))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Shrine - Secret passage magic switch", player),
                 has_fire_or_thunder)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Secret Passage - First fire barrier magic switch", player),
                 has_fire_or_thunder)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Secret Passage - Second fire barrier magic switch", player),
                 has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Secret Passage - Enraged Armor", player),
             (boss_souls_vanilla
             | Has("Enraged Armor Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 5)
             & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Secret Passage - 56. Knight Kingdom Crown from Enraged Armor", player),
                 (boss_souls_vanilla
                 | Has("Enraged Armor Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Secret Passage - Teleport from Enraged Armor", player),
             (boss_souls_vanilla
             | Has("Enraged Armor Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 5)
             & Has("Mana Absorption"))))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Secret Passage - Defeat Enraged Armor barrier", player),
                 (boss_souls_vanilla
                 | Has("Enraged Armor Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Underground - Arcane chest at bridge jumping puzzle", player),
             has_wind_or_skip)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Underground - Magic barrier switches at maid enemy", player),
                 Has("Ice"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Underground - After fire magic switch", player),
                 Has("Ice"))
    world.set_rule(multiworld.get_location("Underground - Defeat Tania", player),
             (boss_souls_vanilla
             | Has("Tania Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 3)
             & Has("Mana Absorption"))))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Underground - Tania boss arena barrier", player),
                 (boss_souls_vanilla
                 | Has("Tania Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 3)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Underground - 98. Lost Maiden's Soul Shard from Tania", player),
                 (boss_souls_vanilla
                 | Has("Tania Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 3)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Lava Ruins - Chest on scaffolding", player),
             has_wind_or_damage_boost)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Lava Ruins - Defeat scissor enemy barrier", player),
                 True_())
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Lava Ruins - Lift magic switch at scissor enemy", player),
                 True_())
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Lava Ruins - Fire magic switch", player),
                 has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Lava Ruins - Jumping puzzle arcane chest at moving ring gauntlet", player),
             Has("Wind"))
    world.set_rule(multiworld.get_location("Lava Ruins - Monica", player),
             (boss_souls_vanilla
             | Has("Monica Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 4)
             & Has("Mana Absorption"))))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Lava Ruins - Monica boss arena barrier", player),
                 (boss_souls_vanilla
                 | Has("Monica Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 4)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Lava Ruins - 34. Bestian Ear from Monica", player),
                 (boss_souls_vanilla
                 | Has("Monica Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 4)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Lava Ruins - 33. Bestian Palm from Monica", player),
                 (boss_souls_vanilla
                 | Has("Monica Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 4)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Lava Ruins - 99. Child's Soul Shard from Monica", player),
                 (boss_souls_vanilla
                 | Has("Monica Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 4)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 39. Dark Elf's Short Bow from barrel on scaffolding", player),
                 has_wind_or_damage_boost)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 45. Golden Coin from first mimic", player),
                 Has("Fire"))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 48. Chief's Skull from right mimic in mimic room", player),
                 Has("Fire"))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 49. Chief's Skull from straight mimic in mimic room", player),
                 Has("Fire"))
    world.set_rule(multiworld.get_location("Dark Tunnel - Thunder spell chest in mimic room", player),
             has_wind_or_damage_boost)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Dark Tunnel - Thunder barrier magic switches", player),
                 Has("Thunder"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch one", player),
                 Has("Thunder")
                 | CanReachRegion("Dark Tunnel - After floating platforms"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch two", player),
                 Has("Thunder")
                 | CanReachRegion("Dark Tunnel - After floating platforms"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch three", player),
                 Has("Thunder")
                 | CanReachRegion("Dark Tunnel - After floating platforms"))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 71. Apocalypse Knight Record from knight enemy", player),
                 has_wind_or_damage_boost)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 103. Loyal Soul Shard from knight enemy", player),
                 has_wind_or_damage_boost)
    world.set_rule(multiworld.get_location("Dark Tunnel - Chest after knight enemy", player),
             has_wind_or_damage_boost)
    world.set_rule(multiworld.get_location("Dark Tunnel - Vanessa", player),
             (boss_souls_vanilla
             | Has("Vanessa Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 5)
             & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 100. King's Final Honor from Vanessa", player),
                 (boss_souls_vanilla
                 | Has("Vanessa Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 78. Ancient Throne Rune from Vanessa", player),
                 (boss_souls_vanilla
                 | Has("Vanessa Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Dark Tunnel - 77. The Throne from Vanessa", player),
                 (boss_souls_vanilla
                 | Has("Vanessa Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Spirit Realm - Ice spell chest in right side alcove", player),
             Has("Wind"))
    if options.shortcut_gate_behaviour.value == options.shortcut_gate_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Ice spell chest gate switch in right side alcove", player),
                 Has("Wind"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Arcane barrier magic switches", player),
                 Has("Arcane"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Platform shortcut switch", player),
                 HasAll("Fire", "Thunder"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - First Seal magic barrier", player),
                 boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption")))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Second Seal magic barrier", player),
                 boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption")))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Elevator magic switch", player),
                 HasGroup("Attack Magics"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Fire control magic switch", player),
                 (HasAny("Ice", "Thunder")
                 & barrier_vanilla)
                 | (Has("Ice")
                 & barrier_randomized)
                 | has_barrier("Spirit Realm Fire Deactivation"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Magic switch barrier switch", player),
                 (HasAny("Ice", "Thunder")
                 & barrier_vanilla)
                 | (Has("Ice")
                 & barrier_randomized)
                 | has_barrier("Spirit Realm Fire Deactivation"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Spirit Realm - Teleporter magic switch", player),
                 (Has("Thunder")
                 & has_barrier("Spirit Realm Magic Switch Barrier")
                 & ((Has("Ice")
                 & barrier_randomized)
                 | has_barrier("Spirit Realm Fire Deactivation")))
                 | (has_fire_or_thunder
                 & has_barrier("Spirit Realm Fire Deactivation")
                 | (HasAny("Ice", "Thunder")
                 & barrier_vanilla)))
    world.set_rule(multiworld.get_location("Spirit Realm - Vanessa V2", player),
             (boss_souls_vanilla
             | Has("Vanessa V2 Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 5)
             & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Spirit Realm - 101. Proud King's Crafted Soul Shard from Vanessa V2", player),
                 (boss_souls_vanilla
                 | Has("Vanessa V2 Soul"))
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 5)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Spirit Realm - Thunder spell from Vanessa V2", player),
             (boss_souls_vanilla
             | Has("Vanessa V2 Soul"))
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 5)
             & Has("Mana Absorption"))))
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Abyss - 83. Castle Blueprint from crystal on brittle ledge", player),
                 Has("Wind"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Giant maid barrier", player),
                 HasGroup("Attack Magics"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Underground trial activate scissor enemies magic switch", player),
                 has_fire_or_thunder)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Abyss - 91. Gaseous Soul Essence from scissor enemy in underground trial", player),
                 has_fire_or_thunder)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Underground trial scissor enemy barrier", player),
                 has_fire_or_thunder)
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Underground trial magic switch", player),
                 has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Abyss - Underground Trial Complete", player),
             has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Abyss - Thunder spell chest dark tunnel trial", player),
             has_wind_or_skip)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Abyss - 95. Refined Soul Shard from maid enemy in dark tunnel trial", player),
                 Has("Thunder"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Dark tunnel trial maid enemy barrier", player),
                 Has("Thunder"))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Dark Tunnel trial magic switch", player),
                 has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Abyss - Dark Tunnel Trial Complete", player),
             has_fire_or_thunder)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Abyss - 93. Enchanted Soul Shard from maid enemy in lava ruins trial", player),
                 (has_fire_or_thunder
                 | Has("Ice"))
                 & (has_barrier("Abyss Lava Ruins Trial Lower Lava")
                 | barrier_vanilla))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Lava Ruins trial defeat maids enemy barrier", player),
                 (has_fire_or_thunder
                 | Has("Ice"))
                 & (has_barrier("Abyss Lava Ruins Trial Lower Lava")
                 | barrier_vanilla))
    if options.barrier_behaviour.value == options.barrier_behaviour.option_randomized:
        world.set_rule(multiworld.get_location("Abyss - Lava Ruins trial magic switch", player),
                 has_fire_or_thunder)
    world.set_rule(multiworld.get_location("Abyss - Lava Ruins Trial Complete", player),
             has_fire_or_thunder)
    if world.options.randomize_lore.value != world.options.randomize_lore.option_no_lore:
        world.set_rule(multiworld.get_location("Abyss - 102. Lost Maiden's Crafted Soul Shard from Nonota", player),
                 has_goal_requirements
                 & (boss_req_none
                 | (boss_req_absorption
                 & Has("Mana Absorption"))
                 | (boss_req_normal
                 & HasGroup("Attack Magics")
                 & Has("Mana Absorption"))
                 | (boss_req_easy
                 & HasGroup("Attack Magics", 7)
                 & Has("Mana Absorption"))))
    world.set_rule(multiworld.get_location("Abyss - Nonota", player),
             has_goal_requirements
             & (boss_req_none
             | (boss_req_absorption
             & Has("Mana Absorption"))
             | (boss_req_normal
             & HasGroup("Attack Magics")
             & Has("Mana Absorption"))
             | (boss_req_easy
             & HasGroup("Attack Magics", 7)
             & Has("Mana Absorption"))))
