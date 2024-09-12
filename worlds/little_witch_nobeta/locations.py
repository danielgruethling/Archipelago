from typing import Dict, Set, Any, TYPE_CHECKING
from BaseClasses import Location

if TYPE_CHECKING:
    from . import LWNWorld


class LWNLocation(Location):
    game: str = "Little Witch Nobeta"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
        super(LWNLocation, self).__init__(player, name, code, parent)
        self.event = code is None


base_id = 345600000

shrine_start_locations: Set[str] = {
    "Shrine - 6. Broken Cross Spear from first ranged Enemy",
    "Shrine - 1. Crafted Soul Reader from pot in side alcove",
    "Shrine - Chest at first magic switch barrier",
    "Shrine - Chest on platform at first magic switch barrier",
    "Shrine - First magic switch",
}

shrine_after_first_magic_switch_locations: Set[str] = {
    "Shrine - 3. Copper Coin in Grand Hall statue barrel",
    "Shrine - Second magic switch",
}

shrine_armor_hall_locations: Set[str] = {
    "Shrine - Chest behind gate",
    "Shrine - 12. Pointy Witch's Hat in pot at chest behind gate",
    "Shrine - 7. Deformed Cavalier Armor from Enemy before Central Hall",
    "Shrine - Specter Armor",
    "Shrine - Secret passage magic switch",
}

shrine_underground_shortcut_locations: Set[str] = {
    "Shrine - Underground shortcut gate switch",
    "Shrine - 14. Corpse Shroud from pot in Underground shortcut",
}

secret_passage_start_locations: Set[str] = {
    "Secret Passage - 35. Dwarven Metalwork in pot after first drop",
    "Secret Passage - 36. High Elf's Mana Ring in pot beside destructible wall",
    "Secret Passage - 11. Broken Queen Doll from enemy behind destructible wall",
    "Secret Passage - Absorption spell chest behind destructible wall",
    "Secret Passage - First fire barrier magic switch",
}

secret_passage_after_first_fire_barrier_locations: Set[str] = {
    "Secret Passage - 37. Forest Elf's Vest from enemy before hole in floor",
    "Secret Passage - Wind spell chest in alcove during fall",
    "Secret Passage - Ice spell chest behind breakable wall after fall",
    "Secret Passage - 4. Unknown House Banner from big enemy at spiral stairs",
    "Secret Passage - Secret area shortcut gate switch",
    "Secret Passage - Fire spell chest at second fire barrier magic switch",
    "Secret Passage - Second fire barrier magic switch",
    "Secret Passage - 38. Dark Elf's Ear Sample from pot at magic barrier",
}

secret_passage_enraged_armor_locations: Set[str] = {
    "Secret Passage - 19. Knight's Halberd from pot before boss",
    "Secret Passage - Enraged Armor",
    "Secret Passage - 56. Knight Kingdom Crown from Enraged Armor",
    "Secret Passage - Teleport from Enraged Armor",
    "Secret Passage - Defeat Enraged Armor barrier",
}

secret_passage_boss_shortcut_locations: Set[str] = {
    "Secret Passage - Thunder spell chest after boss",
    "Secret Passage - Boss shortcut gate switch",
    "Secret Passage - 13. Sleeve Dagger",
}

secret_passage_dark_tunnel_shortcut_locations: Set[str] = {
    "Secret Passage - Dark Tunnel shortcut gate switch",
}

underground_start_locations: Set[str] = {
    "Underground - 8. Hero's Cross Sword",
    "Underground - 9. Giant Axe",
    "Underground - 10. Shield of the Church",
    "Underground - 97. Faithful Soul Shard",
    "Underground - Wind spell chest",
}

underground_after_wind_locations: Set[str] = {
    "Underground - 18. Soul Doll Remnant from first doll enemy",
    "Underground - Chest in alcove before falling rocks",
    "Underground - Chest across staircase on backtrack path",
    "Underground - 2. Stained Ribbon down on glowing rock",
    "Underground - Arcane chest at bridge jumping puzzle",
    "Underground - Ice spell chest in bottom pit",
    "Underground - 17. Tattered Maid Outfit from maid enemy",
    "Underground - Cat absorption hint & gift",
    "Underground - Magic barrier switches at maid enemy",
}

underground_lava_ruins_shortcut_locations: Set[str] = {
    "Underground - Lava ruins shortcut gate switch",
}

underground_tania_shortcut_locations: Set[str] = {
    "Underground - 15. Headcutter Circular Saw",
    "Underground - Tania shortcut switch on statue side",
}

underground_after_fire_locations: Set[str] = {
    "Underground - 16. Test Subject Manacle from barrel after fire",
    "Underground - Chest after fire",
    "Underground - After fire magic switch",
}

underground_after_fire_magic_switch_barrier_locations: Set[str] = {
    "Underground - Defeat enemies barrier",
}

underground_tania_locations: Set[str] = {
    "Underground - Tania",
    "Underground - Tania shortcut switch on Tania side",
    "Underground - 98. Lost Maiden's Soul Shard from Tania",
}

lava_ruins_start_locations: Set[str] = {
    "Lava Ruins - 26. Teddy Bear",
    "Lava Ruins - 30. Merchant's Ledger from enemy",
    "Lava Ruins - Chest on scaffolding",
    "Lava Ruins - Chest on left side lava ledge",
    "Lava Ruins - 29. Slave Branding Iron in barrel after dropping down",
    "Lava Ruins - Absorption spell chest after dropping down",
    "Lava Ruins - Chest on right ruins ledge at shotgun enemies magic switch",
    "Lava Ruins - Magic platform switch at shotgun enemies",
}

lava_ruins_after_magic_platforms_locations: Set[str] = {
    "Lava Ruins - 27. Fractured Stone Axe from red enemy behind destructible wall",
    "Lava Ruins - Wind spell chest behind destructible walls",
    "Lava Ruins - 20. Weathered Cloak in corner on ruins top",
    "Lava Ruins - 28. Cage on path to starting area shortcut gate",
    "Lava Ruins - Fake floor shortcut gate switch",
    "Lava Ruins - Fake floor bait item",
    "Lava Ruins - 23. Cursed Turquoise Necklace from scissor enemy",
    "Lava Ruins - Defeat scissor enemy barrier",
}

lava_ruins_after_scissor_enemy_barrier_locations: Set[str] = {
    "Lava Ruins - Lift magic switch at scissor enemy",
    "Lava Ruins - 32. Slave Collar from ranged enemy in corner at spewing lava",
    "Lava Ruins - Chest in spewing lava room",
    "Lava Ruins - Fire spell chest at double staircase",
    "Lava Ruins - 31. Slave Tag from pot atop of double staircase",
    "Lava Ruins - Fire magic switch",
}

lava_ruins_after_fire_barrier_locations: Set[str] = {
    "Lava Ruins - 25. Copper Ingot on path through hole in wall",
    "Lava Ruins - 22. Intricate Clock from barrel in lava maze",
    "Lava Ruins - Chest in lava maze",
    "Lava Ruins - Jumping puzzle arcane chest at moving ring gauntlet",
    "Lava Ruins - Monica shortcut switch",
    "Lava Ruins - 21. Silver Coin from barrel at Monica statue",
    "Lava Ruins - 24. Glass Lantern from scissor enemy",
}

lava_ruins_monica_locations: Set[str] = {
    "Lava Ruins - Monica",
    "Lava Ruins - 34. Bestian Ear from Monica",
    "Lava Ruins - 33. Bestian Palm from Monica",
    "Lava Ruins - 99. Child's Soul Shard from Monica",
}

lava_ruins_monica_warp_locations: Set[str] = {
    "Lava Ruins - Monica warp gate switch",
}

lava_ruins_path_to_dark_tunnel_locations: Set[str] = {
    "Lava Ruins - Ice spell chest in corner on path to dark tunnel",
    "Dark Tunnel - 5. Melted Silver Candlestick in front of underground shortcut",
}

dark_tunnel_start_locations: Set[str] = {
    "Dark Tunnel - 39. Dark Elf's Short Bow from barrel on scaffolding",
    "Dark Tunnel - 43. Bloodstained Javelin from barrel at statue",
    "Dark Tunnel - 40. Ogre's Kidney from first shield enemy",
    "Dark Tunnel - 41. Ogre's Eye from first ranged enemy",
    "Dark Tunnel - 44. Nomad's Cookware from barrel at magic barrier switch",
    "Dark Tunnel - First magic barrier switch",
}

dark_tunnel_after_first_magic_barrier_locations: Set[str] = {
    "Dark Tunnel - 42. Ogre's Club from shield enemy at gate switch",
    "Dark Tunnel - First gate switch",
}

dark_tunnel_after_first_gate_locations: Set[str] = {
    "Dark Tunnel - Absorption spell chest hidden behind rubble at staircase",
    "Dark Tunnel - 45. Golden Coin from first mimic",
    "Dark Tunnel - Chest at jump from broken staircase",
    "Dark Tunnel - 46. Tooth Thief's Pouch from barrel at scaffolding",
    "Dark Tunnel - Wind spell chest in dark hole",
    "Dark Tunnel - 50. Crafted Soul Injector from pot at light switch after getting the hat",
    "Dark Tunnel - Light switch after getting the hat",
}

dark_tunnel_after_light_switch_barrier_locations: Set[str] = {
    "Dark Tunnel - 57. Lady's Feather Hat from puppeteer",
    "Dark Tunnel - 47. Blood Orc's Skin Sample from barrel above dark maze",
    "Dark Tunnel - Fire spell chest inside dark maze",
    "Dark Tunnel - 48. Chief's Skull from right mimic in mimic room",
    "Dark Tunnel - 49. Chief's Skull from straight mimic in mimic room",
    "Dark Tunnel - Thunder spell chest in mimic room",
    "Dark Tunnel - 53. Ceremonial Sword from barrel at second statue",
    "Dark Tunnel - Thunder barrier magic switches",
}

dark_tunnel_after_thunder_barrier_locations: Set[str] = {
    "Dark Tunnel - 51. Hero's Insignia",
    "Dark Tunnel - Chest in alcove",
    "Dark Tunnel - 54. Banner of the Lance Hero from lightning enemy",
    "Dark Tunnel - Floating platform switch one",
    "Dark Tunnel - Floating platform switch two",
    "Dark Tunnel - Floating platform switch three",
}

dark_tunnel_after_floating_platforms_locations: Set[str] = {
    "Dark Tunnel - Chest on left side after floating platforms",
}

dark_tunnel_after_bridge_collapse_locations: Set[str] = {
    "Dark Tunnel - Arcane spell chest on collapsed bridge",
    "Dark Tunnel - 52. Mutated Beast Claw from pot in big hall",
    "Dark Tunnel - 69. Pontiff's Scepter from singular barrel in side room",
    "Dark Tunnel - 71. Apocalypse Knight Record from knight enemy",
    "Dark Tunnel - 103. Loyal Soul Shard from knight enemy",
    "Dark Tunnel - Chest after knight enemy",
    "Dark Tunnel - 65. Declaration of War from barrel at statue",
    "Dark Tunnel - Vanessa",
    "Dark Tunnel - 100. King's Final Honor from Vanessa",
    "Dark Tunnel - 78. Ancient Throne Rune from Vanessa",
    "Dark Tunnel - 77. The Throne from Vanessa",
}

spirit_realm_start_locations: Set[str] = {
    "Spirit Realm - 72. Apocalypse Knight Shield from crystal at statue",
    "Spirit Realm - 73. Apocalypse Knight Axe from enemy in trapped barrel",
    "Spirit Realm - 79. Doctor's Mask hidden on ledge",
    "Spirit Realm - Wind spell chest inside roof hole",
    "Spirit Realm - Wind spell chest gate switch",
    "Spirit Realm - 55. Banner of the Lionhearted from crystal in doorway",
    "Spirit Realm - 75. Apocalypse Knight Bow from bow enemy",
}

spirit_realm_after_platforms_locations: Set[str] = {
    "Spirit Realm - 61. Knight Kingdom Entry Pass from sword enemy",
    "Spirit Realm - 58. Super Cleanser Soap from crystal on path",
    "Spirit Realm - Chest hidden in dropdown alcove",
    "Spirit Realm - 63. Inquisitor's List from crystal at second statue",
    "Spirit Realm - Ice spell chest in right side alcove",
    "Spirit Realm - Ice spell chest gate switch in right side alcove",
    "Spirit Realm - 76. Apocalypse Knight Sword from enemy",
    "Spirit Realm - 74. Apocalypse Knight Staff from enemy",
    "Spirit Realm - Arcane barrier magic switches",
}

spirit_realm_after_arcane_barrier_locations: Set[str] = {
    "Spirit Realm - Thunder spell chest behind breakable wall",
    "Spirit Realm - 86. Missing Person Poster on bridge",
    "Spirit Realm - Platform shortcut switch",
    "Spirit Realm - 59. Exquisite Leather Lamp from crystal before Seal",
}

spirit_realm_seal_locations: Set[str] = {
    "Spirit Realm - 66. Attic Key from crystal at first Seal phase",
    "Spirit Realm - 64. Envoy's Rune from crystal at first Seal phase",
    "Spirit Realm - 60. Premium Grass Ash from crystal at first Seal phase",
    "Spirit Realm - 62. Bone Chess Set from crystal at first Seal phase",
    "Spirit Realm - First Seal magic barrier",
}

spirit_realm_after_first_seal_locations: Set[str] = {
    "Spirit Realm - 90. Enchanted Shackles from second Seal phase",
    "Spirit Realm - Fire spell chest at second Seal phase",
    "Spirit Realm - Second Seal magic barrier",
}

spirit_realm_after_second_seal_locations: Set[str] = {
    "Spirit Realm - 87. Saint's Cane from crystal at third statue",
    "Spirit Realm - Statue shortcut gate switch",
    "Spirit Realm - 67. Halfling's Forelimb from crystal at elevator magic switch",
    "Spirit Realm - Elevator magic switch",
}

spirit_realm_after_elevator_locations: Set[str] = {
    "Spirit Realm - 68. Ratian Claw from crystal after elevator",
    "Spirit Realm - Absorption spell chest behind crystals after elevator",
    "Spirit Realm - Fire control magic switch",
    "Spirit Realm - Magic switch barrier switch",
    "Spirit Realm - Teleporter magic switch",
}

spirit_realm_after_teleport_locations: Set[str] = {
    "Spirit Realm - 70. Abandoned Rag Doll from crystal on spiral stairs",
    "Spirit Realm - Chest before boss behind breakable wall",
    "Spirit Realm - 89. Bloodstained Key at statue before boss",
    "Spirit Realm - Vanessa V2",
    "Spirit Realm - 101. Proud King's Crafted Soul Shard from Vanessa V2",
    "Spirit Realm - Thunder spell from Vanessa V2",
}

abyss_locations: Set[str] = {
    "Abyss - 80. Ceremonial Incense at first statue",
}

abyss_after_first_teleport_locations: Set[str] = {
    "Abyss - First gate switch",
}

abyss_after_first_gate_locations: Set[str] = {
    "Abyss - 81. Moonlight Blade from trapped barrel",
    "Abyss - 83. Castle Blueprint from crystal on brittle ledge",
    "Abyss - Arcane spell chest on pillar",
    "Abyss - 84. Witch Worshipper Puppet from pot right of pillars",
    "Abyss - Giant maid barrier",
}

abyss_left_gate_at_trap_locations: Set[str] = {
    "Abyss - 82. Prostitute's Chiffon from crystal in left trap gate",
    "Abyss - Chest in left trap gate",
}

abyss_after_giant_maid_barrier_locations: Set[str] = {
    "Abyss - 85. Polymorphism Scroll from crystal behind gate",
}

abyss_trials_lobby_locations: Set[str] = {
    "Abyss - 88. Hero Summon Rune in front of statue",
}

abyss_underground_trial_locations: Set[str] = {
    "Abyss - Fire Spell chest underground trial",
    "Abyss - Underground trial unlock enemies magic switch",
    "Abyss - 91. Gaseous Soul Essence from scissor enemy in underground trial",
    "Abyss - Underground trial scissor enemy magic gate",
}

abyss_underground_trial_magic_switch_locations: Set[str] = {
    "Abyss - Underground trial magic switch",
    "Abyss - 92. Semi-gaseous Soul Essence in front of underground trial magic switch",
}

abyss_dark_tunnel_trial_locations: Set[str] = {
    "Abyss - Thunder spell chest dark tunnel trial",
    "Abyss - 95. Refined Soul Shard from maid enemy in dark tunnel trial",
    "Abyss - Dark tunnel trial maid enemy barrier",
}

abyss_dark_tunnel_trial_magic_switch_locations: Set[str] = {
    "Abyss - Dark Tunnel trial magic switch",
    "Abyss - 96. Knight's Soul Shard in front of dark tunnel trial magic switch",
}

abyss_lava_ruins_trial_locations: Set[str] = {
    "Abyss - Ice spell chest lava ruins trial",
    "Abyss - 93. Enchanted Soul Shard from maid enemy in lava ruins trial",
    "Abyss - Lava Ruins trial defeat maids enemy barrier",
}

abyss_lava_ruins_trial_magic_switch_locations: Set[str] = {
    "Abyss - Lava Ruins trial magic switch",
    "Abyss - 94. Knight's Soul Shard in front of lava ruins trial magic switch",
}

abyss_nonota_locations: Set[str] = {
    "Abyss - 102. Lost Maiden's Crafted Soul Shard from Nonota",
    "Abyss - Nonota",
}

lwn_locations: Dict[str, Any] = {
    **dict.fromkeys(shrine_start_locations, None),
    **dict.fromkeys(shrine_after_first_magic_switch_locations, None),
    **dict.fromkeys(shrine_armor_hall_locations, None),
    **dict.fromkeys(shrine_underground_shortcut_locations, None),
    **dict.fromkeys(secret_passage_start_locations, None),
    **dict.fromkeys(secret_passage_after_first_fire_barrier_locations, None),
    **dict.fromkeys(secret_passage_enraged_armor_locations, None),
    **dict.fromkeys(secret_passage_boss_shortcut_locations, None),
    **dict.fromkeys(secret_passage_dark_tunnel_shortcut_locations, None),
    **dict.fromkeys(underground_start_locations, None),
    **dict.fromkeys(underground_after_wind_locations, None),
    **dict.fromkeys(underground_lava_ruins_shortcut_locations, None),
    **dict.fromkeys(underground_tania_shortcut_locations, None),
    **dict.fromkeys(underground_after_fire_locations, None),
    **dict.fromkeys(underground_after_fire_magic_switch_barrier_locations, None),
    **dict.fromkeys(underground_tania_locations, None),
    **dict.fromkeys(lava_ruins_start_locations, None),
    **dict.fromkeys(lava_ruins_after_magic_platforms_locations, None),
    **dict.fromkeys(lava_ruins_after_scissor_enemy_barrier_locations, None),
    **dict.fromkeys(lava_ruins_after_fire_barrier_locations, None),
    **dict.fromkeys(lava_ruins_monica_locations, None),
    **dict.fromkeys(lava_ruins_monica_warp_locations, None),
    **dict.fromkeys(lava_ruins_path_to_dark_tunnel_locations, None),
    **dict.fromkeys(dark_tunnel_start_locations, None),
    **dict.fromkeys(dark_tunnel_after_first_magic_barrier_locations, None),
    **dict.fromkeys(dark_tunnel_after_first_gate_locations, None),
    **dict.fromkeys(dark_tunnel_after_light_switch_barrier_locations, None),
    **dict.fromkeys(dark_tunnel_after_thunder_barrier_locations, None),
    **dict.fromkeys(dark_tunnel_after_floating_platforms_locations, None),
    **dict.fromkeys(dark_tunnel_after_bridge_collapse_locations, None),
    **dict.fromkeys(spirit_realm_start_locations, None),
    **dict.fromkeys(spirit_realm_after_platforms_locations, None),
    **dict.fromkeys(spirit_realm_after_arcane_barrier_locations, None),
    **dict.fromkeys(spirit_realm_seal_locations, None),
    **dict.fromkeys(spirit_realm_after_first_seal_locations, None),
    **dict.fromkeys(spirit_realm_after_second_seal_locations, None),
    **dict.fromkeys(spirit_realm_after_elevator_locations, None),
    **dict.fromkeys(spirit_realm_after_teleport_locations, None),
    **dict.fromkeys(abyss_locations, None),
    **dict.fromkeys(abyss_after_first_teleport_locations, None),
    **dict.fromkeys(abyss_after_first_gate_locations, None),
    **dict.fromkeys(abyss_left_gate_at_trap_locations, None),
    **dict.fromkeys(abyss_after_giant_maid_barrier_locations, None),
    **dict.fromkeys(abyss_trials_lobby_locations, None),
    **dict.fromkeys(abyss_underground_trial_locations, None),
    **dict.fromkeys(abyss_underground_trial_magic_switch_locations, None),
    **dict.fromkeys(abyss_dark_tunnel_trial_locations, None),
    **dict.fromkeys(abyss_dark_tunnel_trial_magic_switch_locations, None),
    **dict.fromkeys(abyss_lava_ruins_trial_locations, None),
    **dict.fromkeys(abyss_lava_ruins_trial_magic_switch_locations, None),
    **dict.fromkeys(abyss_nonota_locations, None),
}

location_name_to_id: Dict[str, int] = {name: base_id + index for index, name in enumerate(lwn_locations)}

location_name_groups = {
    "Bosses": {
        "Dark Tunnel - Vanessa",
        "Lava Ruins - Monica",
        "Secret Passage - Enraged Armor",
        "Shrine - Specter Armor",
        "Spirit Realm - Vanessa V2",
        "Underground - Tania",
    },
    "Lore": {
        "Abyss - 102. Lost Maiden's Crafted Soul Shard from Nonota",
        "Abyss - 80. Ceremonial Incense at first statue",
        "Abyss - 81. Moonlight Blade from trapped barrel",
        "Abyss - 82. Prostitute's Chiffon from crystal in left trap gate",
        "Abyss - 83. Castle Blueprint from crystal on brittle ledge",
        "Abyss - 84. Witch Worshipper Puppet from pot right of pillars",
        "Abyss - 85. Polymorphism Scroll from crystal behind gate",
        "Abyss - 88. Hero Summon Rune in front of statue",
        "Abyss - 91. Gaseous Soul Essence from scissor enemy in underground trial",
        "Abyss - 92. Semi-gaseous Soul Essence in front of underground trial magic switch",
        "Abyss - 93. Enchanted Soul Shard from maid enemy in lava ruins trial",
        "Abyss - 94. Knight's Soul Shard in front of lava ruins trial magic switch",
        "Abyss - 95. Refined Soul Shard from maid enemy in dark tunnel trial",
        "Abyss - 96. Knight's Soul Shard in front of dark tunnel trial magic switch",
        "Dark Tunnel - 100. King's Final Honor from Vanessa",
        "Dark Tunnel - 103. Loyal Soul Shard from knight enemy",
        "Dark Tunnel - 39. Dark Elf's Short Bow from barrel on scaffolding",
        "Dark Tunnel - 40. Ogre's Kidney from first shield enemy",
        "Dark Tunnel - 41. Ogre's Eye from first ranged enemy",
        "Dark Tunnel - 42. Ogre's Club from shield enemy at gate switch",
        "Dark Tunnel - 43. Bloodstained Javelin from barrel at statue",
        "Dark Tunnel - 44. Nomad's Cookware from barrel at magic barrier switch",
        "Dark Tunnel - 45. Golden Coin from first mimic",
        "Dark Tunnel - 46. Tooth Thief's Pouch from barrel at scaffolding",
        "Dark Tunnel - 47. Blood Orc's Skin Sample from barrel above dark maze",
        "Dark Tunnel - 48. Chief's Skull from right mimic in mimic room",
        "Dark Tunnel - 49. Chief's Skull from straight mimic in mimic room",
        "Dark Tunnel - 5. Melted Silver Candlestick in front of underground shortcut",
        "Dark Tunnel - 50. Crafted Soul Injector from pot at light switch after getting the hat",
        "Dark Tunnel - 51. Hero's Insignia",
        "Dark Tunnel - 52. Mutated Beast Claw from pot in big hall",
        "Dark Tunnel - 53. Ceremonial Sword from barrel at second statue",
        "Dark Tunnel - 54. Banner of the Lance Hero from lightning enemy",
        "Dark Tunnel - 57. Lady's Feather Hat from puppeteer",
        "Dark Tunnel - 65. Declaration of War from barrel at statue",
        "Dark Tunnel - 69. Pontiff's Scepter from singular barrel in side room",
        "Dark Tunnel - 71. Apocalypse Knight Record from knight enemy",
        "Dark Tunnel - 77. The Throne from Vanessa",
        "Dark Tunnel - 78. Ancient Throne Rune from Vanessa",
        "Lava Ruins - 20. Weathered Cloak in corner on ruins top",
        "Lava Ruins - 21. Silver Coin from barrel at Monica statue",
        "Lava Ruins - 22. Intricate Clock from barrel in lava maze",
        "Lava Ruins - 23. Cursed Turquoise Necklace from scissor enemy",
        "Lava Ruins - 24. Glass Lantern from scissor enemy",
        "Lava Ruins - 25. Copper Ingot on path through hole in wall",
        "Lava Ruins - 26. Teddy Bear",
        "Lava Ruins - 27. Fractured Stone Axe from red enemy behind destructible wall",
        "Lava Ruins - 28. Cage on path to starting area shortcut gate",
        "Lava Ruins - 29. Slave Branding Iron in barrel after dropping down",
        "Lava Ruins - 30. Merchant's Ledger from enemy",
        "Lava Ruins - 31. Slave Tag from pot atop of double staircase",
        "Lava Ruins - 32. Slave Collar from ranged enemy in corner at spewing lava",
        "Lava Ruins - 33. Bestian Palm from Monica",
        "Lava Ruins - 34. Bestian Ear from Monica",
        "Lava Ruins - 99. Child's Soul Shard from Monica",
        "Secret Passage - 11. Broken Queen Doll from enemy behind destructible wall",
        "Secret Passage - 13. Sleeve Dagger",
        "Secret Passage - 19. Knight's Halberd from pot before boss",
        "Secret Passage - 35. Dwarven Metalwork in pot after first drop",
        "Secret Passage - 36. High Elf's Mana Ring in pot beside destructible wall",
        "Secret Passage - 37. Forest Elf's Vest from enemy before hole in floor",
        "Secret Passage - 38. Dark Elf's Ear Sample from pot at magic barrier",
        "Secret Passage - 4. Unknown House Banner from big enemy at spiral stairs",
        "Secret Passage - 56. Knight Kingdom Crown from Enraged Armor",
        "Shrine - 1. Crafted Soul Reader from pot in side alcove",
        "Shrine - 12. Pointy Witch's Hat in pot at chest behind gate",
        "Shrine - 14. Corpse Shroud from pot in Underground shortcut",
        "Shrine - 3. Copper Coin in Grand Hall statue barrel",
        "Shrine - 6. Broken Cross Spear from first ranged Enemy",
        "Shrine - 7. Deformed Cavalier Armor from Enemy before Central Hall",
        "Spirit Realm - 101. Proud King's Crafted Soul Shard from Vanessa V2",
        "Spirit Realm - 55. Banner of the Lionhearted from crystal in doorway",
        "Spirit Realm - 58. Super Cleanser Soap from crystal on path",
        "Spirit Realm - 59. Exquisite Leather Lamp from crystal before Seal",
        "Spirit Realm - 60. Premium Grass Ash from crystal at first Seal phase",
        "Spirit Realm - 61. Knight Kingdom Entry Pass from sword enemy",
        "Spirit Realm - 62. Bone Chess Set from crystal at first Seal phase",
        "Spirit Realm - 63. Inquisitor's List from crystal at second statue",
        "Spirit Realm - 64. Envoy's Rune from crystal at first Seal phase",
        "Spirit Realm - 66. Attic Key from crystal at first Seal phase",
        "Spirit Realm - 67. Halfling's Forelimb from crystal at elevator magic switch",
        "Spirit Realm - 68. Ratian Claw from crystal after elevator",
        "Spirit Realm - 70. Abandoned Rag Doll from crystal on spiral stairs",
        "Spirit Realm - 72. Apocalypse Knight Shield from crystal at statue",
        "Spirit Realm - 73. Apocalypse Knight Axe from enemy in trapped barrel",
        "Spirit Realm - 74. Apocalypse Knight Staff from enemy",
        "Spirit Realm - 75. Apocalypse Knight Bow from bow enemy",
        "Spirit Realm - 76. Apocalypse Knight Sword from enemy",
        "Spirit Realm - 79. Doctor's Mask hidden on ledge",
        "Spirit Realm - 86. Missing Person Poster on bridge",
        "Spirit Realm - 87. Saint's Cane from crystal at third statue",
        "Spirit Realm - 89. Bloodstained Key at statue before boss",
        "Spirit Realm - 90. Enchanted Shackles from second Seal phase",
        "Underground - 10. Shield of the Church",
        "Underground - 15. Headcutter Circular Saw",
        "Underground - 16. Test Subject Manacle from barrel after fire",
        "Underground - 17. Tattered Maid Outfit from maid enemy",
        "Underground - 18. Soul Doll Remnant from first doll enemy",
        "Underground - 2. Stained Ribbon down on glowing rock",
        "Underground - 8. Hero's Cross Sword",
        "Underground - 9. Giant Axe",
        "Underground - 97. Faithful Soul Shard",
        "Underground - 98. Lost Maiden's Soul Shard from Tania",
    },
    "Item": {
        "Lava Ruins - Fake floor bait item",
        "Spirit Realm - Thunder spell from Vanessa V2",
        "Underground - Cat absorption hint & gift",
    },
    "Chest": {
        "Abyss - Arcane spell chest on pillar",
        "Abyss - Chest in left trap gate",
        "Abyss - Fire Spell chest underground trial",
        "Abyss - Ice spell chest lava ruins trial",
        "Abyss - Thunder spell chest dark tunnel trial",
        "Dark Tunnel - Absorption spell chest hidden behind rubble at staircase",
        "Dark Tunnel - Arcane spell chest on collapsed bridge",
        "Dark Tunnel - Chest after knight enemy",
        "Dark Tunnel - Chest at jump from broken staircase",
        "Dark Tunnel - Chest in alcove",
        "Dark Tunnel - Chest on left side after floating platforms",
        "Dark Tunnel - Fire spell chest inside dark maze",
        "Dark Tunnel - Thunder spell chest in mimic room",
        "Dark Tunnel - Wind spell chest in dark hole",
        "Lava Ruins - Absorption spell chest after dropping down",
        "Lava Ruins - Chest in lava maze",
        "Lava Ruins - Chest in spewing lava room",
        "Lava Ruins - Chest on left side lava ledge",
        "Lava Ruins - Chest on right ruins ledge at shotgun enemies magic switch",
        "Lava Ruins - Chest on scaffolding",
        "Lava Ruins - Fire spell chest at double staircase",
        "Lava Ruins - Ice spell chest in corner on path to dark tunnel",
        "Lava Ruins - Jumping puzzle arcane chest at moving ring gauntlet",
        "Lava Ruins - Wind spell chest behind destructible walls",
        "Secret Passage - Absorption spell chest behind destructible wall",
        "Secret Passage - Fire spell chest at second fire barrier magic switch",
        "Secret Passage - Ice spell chest behind breakable wall after fall",
        "Secret Passage - Thunder spell chest after boss",
        "Secret Passage - Wind spell chest in alcove during fall",
        "Shrine - Chest at first magic switch barrier",
        "Shrine - Chest behind gate",
        "Shrine - Chest on platform at first magic switch barrier",
        "Spirit Realm - Absorption spell chest behind crystals after elevator",
        "Spirit Realm - Chest before boss behind breakable wall",
        "Spirit Realm - Chest hidden in dropdown alcove",
        "Spirit Realm - Fire spell chest at second Seal phase",
        "Spirit Realm - Ice spell chest in right side alcove",
        "Spirit Realm - Thunder spell chest behind breakable wall",
        "Spirit Realm - Wind spell chest inside roof hole",
        "Underground - Arcane chest at bridge jumping puzzle",
        "Underground - Chest across staircase on backtrack path",
        "Underground - Chest after fire",
        "Underground - Chest in alcove before falling rocks",
        "Underground - Ice spell chest in bottom pit",
        "Underground - Wind spell chest",
    },
    "Metal Gate": {
        "Abyss - First gate switch",
        "Dark Tunnel - First gate switch",
        "Lava Ruins - Fake floor shortcut gate switch",
        "Lava Ruins - Monica shortcut switch",
        "Lava Ruins - Monica warp gate switch",
        "Secret Passage - Boss shortcut gate switch",
        "Secret Passage - Dark Tunnel shortcut gate switch",
        "Secret Passage - Secret area shortcut gate switch",
        "Shrine - Underground shortcut gate switch",
        "Spirit Realm - Ice spell chest gate switch in right side alcove",
        "Spirit Realm - Statue shortcut gate switch",
        "Spirit Realm - Wind spell chest gate switch",
        "Underground - Lava ruins shortcut gate switch",
        "Underground - Tania shortcut switch on Tania side",
        "Underground - Tania shortcut switch on statue side",
    },
    "Barrier": {
        "Abyss - Dark Tunnel trial magic switch",
        "Abyss - Dark tunnel trial maid enemy barrier",
        "Abyss - Giant maid barrier",
        "Abyss - Lava Ruins trial defeat maids enemy barrier",
        "Abyss - Lava Ruins trial magic switch",
        "Abyss - Underground trial magic switch",
        "Abyss - Underground trial scissor enemy magic gate",
        "Abyss - Underground trial unlock enemies magic switch",
        "Dark Tunnel - First magic barrier switch",
        "Dark Tunnel - Floating platform switch one",
        "Dark Tunnel - Floating platform switch three",
        "Dark Tunnel - Floating platform switch two",
        "Dark Tunnel - Light switch after getting the hat",
        "Dark Tunnel - Thunder barrier magic switches",
        "Lava Ruins - Defeat scissor enemy barrier",
        "Lava Ruins - Fire magic switch",
        "Lava Ruins - Lift magic switch at scissor enemy",
        "Lava Ruins - Magic platform switch at shotgun enemies",
        "Secret Passage - Defeat Enraged Armor barrier",
        "Secret Passage - First fire barrier magic switch",
        "Secret Passage - Second fire barrier magic switch",
        "Shrine - First magic switch",
        "Shrine - Second magic switch",
        "Shrine - Secret passage magic switch",
        "Spirit Realm - Arcane barrier magic switches",
        "Spirit Realm - Elevator magic switch",
        "Spirit Realm - Fire control magic switch",
        "Spirit Realm - First Seal magic barrier",
        "Spirit Realm - Magic switch barrier switch",
        "Spirit Realm - Platform shortcut switch",
        "Spirit Realm - Second Seal magic barrier",
        "Spirit Realm - Teleporter magic switch",
        "Underground - After fire magic switch",
        "Underground - Defeat enemies barrier",
        "Underground - Magic barrier switches at maid enemy",
    },
    "Teleport": {
        "Secret Passage - Teleport from Enraged Armor",
    },
    "Event": {
        "Abyss - Nonota",
    },
}


def append_locations(world: "LWNWorld"):
    for location_name in shrine_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Shrine - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in shrine_after_first_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Shrine - After first magic switch", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in shrine_armor_hall_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Shrine - Armor Hall", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in shrine_underground_shortcut_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Shrine - Underground shortcut", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in secret_passage_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Secret passage - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in secret_passage_after_first_fire_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Secret passage - After first fire barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in secret_passage_enraged_armor_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Secret Passage - Enraged Armor", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in secret_passage_boss_shortcut_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Secret Passage - Boss Shortcut", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in secret_passage_dark_tunnel_shortcut_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Secret Passage - Dark Tunnel shortcut", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_after_wind_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - After wind", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_lava_ruins_shortcut_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - Lava ruins shortcut", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_tania_shortcut_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - Tania shortcut", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_after_fire_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - After fire", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_after_fire_magic_switch_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - After fire magic switch barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in underground_tania_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Underground - Tania", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_after_magic_platforms_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - After magic platforms", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_after_scissor_enemy_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - After scissor enemy barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_after_fire_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - After Fire Barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_monica_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - Monica", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_monica_warp_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - Monica warp", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in lava_ruins_path_to_dark_tunnel_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Lava Ruins - Path to dark tunnel", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_first_magic_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After first magic barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_first_gate_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After first gate", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_light_switch_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After light switch barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_thunder_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After thunder barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_floating_platforms_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After floating platforms", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in dark_tunnel_after_bridge_collapse_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After bridge collapse", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_start_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - Start", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_platforms_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After platforms", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_arcane_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After arcane barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_seal_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - Seal", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_first_seal_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After first Seal", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_second_seal_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After second Seal", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_elevator_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After elevator", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in spirit_realm_after_teleport_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Spirit Realm - After teleport", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_after_first_teleport_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - After first teleport", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_after_first_gate_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - After first gate", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_left_gate_at_trap_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Left gate at trap", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_after_giant_maid_barrier_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - After giant maid barrier", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_trials_lobby_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Trials Lobby", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_underground_trial_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Underground Trial", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_underground_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Underground Trial magic switch", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_dark_tunnel_trial_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Dark Tunnel Trial", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_dark_tunnel_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Dark Tunnel Trial magic switch", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_lava_ruins_trial_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Lava Ruins Trial", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_lava_ruins_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Lava Ruins Trial magic switch", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))

    for location_name in abyss_nonota_locations:
        location_id = location_name_to_id[location_name]
        region = world.multiworld.get_region("Abyss - Nonota", world.player)
        region.locations.append(LWNLocation(world.player, location_name, location_id, region))
