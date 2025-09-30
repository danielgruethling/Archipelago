from typing import Dict, TYPE_CHECKING
from BaseClasses import Location
from Options import Toggle

if TYPE_CHECKING:
    from . import LWNWorld


class LWNLocation(Location):
    game: str = "Little Witch Nobeta"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
        super(LWNLocation, self).__init__(player, name, code, parent)
        self.event = code is None


base_id = 1

shrine_start_locations: Dict[str, str] = {
    "Shrine - 6. Broken Cross Spear from first ranged Enemy": "Lore",
    "Shrine - 1. Crafted Soul Reader from pot in side alcove": "Lore",
    "Shrine - Chest at first magic switch barrier": "Chest",
    "Shrine - Chest on platform at first magic switch barrier": "Chest",
    "Shrine - First magic switch": "Barrier",
}

shrine_after_first_magic_switch_locations: Dict[str, str] = {
    "Shrine - 3. Copper Coin in Grand Hall statue barrel": "Lore",
    "Shrine - Second magic switch": "Barrier",
}

shrine_cat_room_locations: Dict[str, str] = {
    "Shrine - Meet Cat barrier": "Barrier",
}

shrine_armor_hall_locations: Dict[str, str] = {
    "Shrine - Chest behind gate": "Chest",
    "Shrine - 12. Pointy Witch's Hat in pot at chest behind gate": "Lore",
    "Shrine - 7. Deformed Cavalier Armor from Enemy before Central Hall": "Lore",
    "Shrine - Specter Armor": "Bosses",
    "Shrine - Secret passage magic switch": "Barrier",
}

shrine_underground_shortcut_locations: Dict[str, str] = {
    "Shrine - Underground shortcut gate switch": "Metal Gate",
    "Shrine - 14. Corpse Shroud from pot in Underground shortcut": "Lore",
}

secret_passage_start_locations: Dict[str, str] = {
    "Secret Passage - 35. Dwarven Metalwork in pot after first drop": "Lore",
    "Secret Passage - 36. High Elf's Mana Ring in pot beside destructible wall": "Lore",
    "Secret Passage - 11. Broken Queen Doll from enemy behind destructible wall": "Lore",
    "Secret Passage - Absorption spell chest behind destructible wall": "Chest",
    "Secret Passage - First fire barrier magic switch": "Barrier",
}

secret_passage_after_first_fire_barrier_locations: Dict[str, str] = {
    "Secret Passage - 37. Forest Elf's Vest from enemy before hole in floor": "Lore",
    "Secret Passage - Wind spell chest in alcove during fall": "Chest",
    "Secret Passage - Ice spell chest behind breakable wall after fall": "Chest",
    "Secret Passage - 4. Unknown House Banner from big enemy at spiral stairs": "Lore",
    "Secret Passage - Secret area shortcut gate switch": "Metal Gate",
    "Secret Passage - Fire spell chest at second fire barrier magic switch": "Chest",
    "Secret Passage - Second fire barrier magic switch": "Barrier",
    "Secret Passage - 38. Dark Elf's Ear Sample from pot at magic barrier": "Lore",
}

secret_passage_enraged_armor_locations: Dict[str, str] = {
    "Secret Passage - 19. Knight's Halberd from pot before boss": "Lore",
    "Secret Passage - Enraged Armor": "Bosses",
    "Secret Passage - 56. Knight Kingdom Crown from Enraged Armor": "Lore",
    "Secret Passage - Teleport from Enraged Armor": "Teleport",
    "Secret Passage - Defeat Enraged Armor barrier": "Barrier",
}

secret_passage_boss_shortcut_locations: Dict[str, str] = {
    "Secret Passage - Thunder spell chest after boss": "Chest",
    "Secret Passage - Boss shortcut gate switch": "Metal Gate",
    "Secret Passage - 13. Sleeve Dagger": "Lore",
}

secret_passage_dark_tunnel_shortcut_locations: Dict[str, str] = {
    "Secret Passage - Dark Tunnel shortcut gate switch": "Metal Gate",
}

underground_start_locations: Dict[str, str] = {
    "Underground - 8. Hero's Cross Sword": "Lore",
    "Underground - 9. Giant Axe": "Lore",
    "Underground - 10. Shield of the Church": "Lore",
    "Underground - 97. Faithful Soul Shard": "Lore",
    "Underground - Wind spell chest": "Chest",
}

underground_after_wind_locations: Dict[str, str] = {
    "Underground - 18. Soul Doll Remnant from first doll enemy": "Lore",
    "Underground - Chest in alcove before falling rocks": "Chest",
    "Underground - Chest across staircase on backtrack path": "Chest",
    "Underground - 2. Stained Ribbon down on glowing rock": "Lore",
    "Underground - Arcane chest at bridge jumping puzzle": "Chest",
    "Underground - Ice spell chest in bottom pit": "Chest",
    "Underground - 17. Tattered Maid Outfit from maid enemy": "Lore",
    "Underground - Cat absorption hint & gift": "Item",
    "Underground - Magic barrier switches at maid enemy": "Barrier",
}

underground_lava_ruins_shortcut_locations: Dict[str, str] = {
    "Underground - Lava ruins shortcut gate switch": "Metal Gate",
}

underground_tania_shortcut_locations: Dict[str, str] = {
    "Underground - 15. Headcutter Circular Saw": "Lore",
    "Underground - Tania shortcut switch on statue side": "Metal Gate",
}

underground_after_fire_locations: Dict[str, str] = {
    "Underground - 16. Test Subject Manacle from barrel after fire": "Lore",
    "Underground - Chest after fire": "Chest",
    "Underground - After fire magic switch": "Barrier",
}

underground_after_fire_magic_switch_barrier_locations: Dict[str, str] = {
    "Underground - Defeat enemies barrier": "Barrier",
}

underground_tania_locations: Dict[str, str] = {
    "Underground - Tania": "Bosses",
    "Underground - Tania shortcut switch on Tania side": "Metal Gate",
    "Underground - 98. Lost Maiden's Soul Shard from Tania": "Lore",
}

lava_ruins_start_locations: Dict[str, str] = {
    "Lava Ruins - 26. Teddy Bear": "Lore",
    "Lava Ruins - 30. Merchant's Ledger from enemy": "Lore",
    "Lava Ruins - Chest on scaffolding": "Chest",
    "Lava Ruins - Chest on left side lava ledge": "Chest",
    "Lava Ruins - 29. Slave Branding Iron in barrel after dropping down": "Lore",
    "Lava Ruins - Absorption spell chest after dropping down": "Chest",
    "Lava Ruins - Chest on right ruins ledge at shotgun enemies magic switch": "Chest",
    "Lava Ruins - Magic platform switch at shotgun enemies": "Barrier",
}

lava_ruins_after_magic_platforms_locations: Dict[str, str] = {
    "Lava Ruins - 27. Fractured Stone Axe from red enemy behind destructible wall": "Lore",
    "Lava Ruins - Wind spell chest behind destructible walls": "Chest",
    "Lava Ruins - 20. Weathered Cloak in corner on ruins top": "Lore",
    "Lava Ruins - 28. Cage on path to starting area shortcut gate": "Lore",
    "Lava Ruins - Fake floor shortcut gate switch": "Metal Gate",
    "Lava Ruins - Fake floor bait item": "Item",
    "Lava Ruins - 23. Cursed Turquoise Necklace from scissor enemy": "Lore",
    "Lava Ruins - Defeat scissor enemy barrier": "Barrier",
}

lava_ruins_after_scissor_enemy_barrier_locations: Dict[str, str] = {
    "Lava Ruins - Lift magic switch at scissor enemy": "Barrier",
    "Lava Ruins - 32. Slave Collar from ranged enemy in corner at spewing lava": "Lore",
    "Lava Ruins - Chest in spewing lava room": "Chest",
    "Lava Ruins - Fire spell chest at double staircase": "Chest",
    "Lava Ruins - 31. Slave Tag from pot atop of double staircase": "Lore",
    "Lava Ruins - Fire magic switch": "Barrier",
}

lava_ruins_after_fire_barrier_locations: Dict[str, str] = {
    "Lava Ruins - 25. Copper Ingot on path through hole in wall": "Lore",
    "Lava Ruins - 22. Intricate Clock from barrel in lava maze": "Lore",
    "Lava Ruins - Chest in lava maze": "Chest",
    "Lava Ruins - Jumping puzzle arcane chest at moving ring gauntlet": "Chest",
    "Lava Ruins - Monica shortcut switch": "Metal Gate",
    "Lava Ruins - 21. Silver Coin from barrel at Monica statue": "Lore",
    "Lava Ruins - 24. Glass Lantern from scissor enemy": "Lore",
}

lava_ruins_monica_locations: Dict[str, str] = {
    "Lava Ruins - Monica": "Bosses",
    "Lava Ruins - 34. Bestian Ear from Monica": "Lore",
    "Lava Ruins - 33. Bestian Palm from Monica": "Lore",
    "Lava Ruins - 99. Child's Soul Shard from Monica": "Lore",
}

lava_ruins_monica_warp_locations: Dict[str, str] = {
    "Lava Ruins - Monica warp gate switch": "Metal Gate",
}

lava_ruins_path_to_dark_tunnel_locations: Dict[str, str] = {
    "Lava Ruins - Ice spell chest in corner on path to dark tunnel": "Chest",
    "Lava Ruins - 5. Melted Silver Candlestick in front of underground shortcut": "Lore",
}

dark_tunnel_start_locations: Dict[str, str] = {
    "Dark Tunnel - 39. Dark Elf's Short Bow from barrel on scaffolding": "Lore",
    "Dark Tunnel - 43. Bloodstained Javelin from barrel at statue": "Lore",
    "Dark Tunnel - 40. Ogre's Kidney from first shield enemy": "Lore",
    "Dark Tunnel - 41. Ogre's Eye from first ranged enemy": "Lore",
    "Dark Tunnel - 44. Nomad's Cookware from barrel at magic barrier switch": "Lore",
    "Dark Tunnel - First magic barrier switch": "Barrier",
}

dark_tunnel_after_first_magic_barrier_locations: Dict[str, str] = {
    "Dark Tunnel - 42. Ogre's Club from shield enemy at gate switch": "Lore",
    "Dark Tunnel - First gate switch": "Metal Gate",
}

dark_tunnel_after_first_gate_locations: Dict[str, str] = {
    "Dark Tunnel - Absorption spell chest hidden behind rubble at staircase": "Chest",
    "Dark Tunnel - 45. Golden Coin from first mimic": "Lore",
    "Dark Tunnel - Chest at jump from broken staircase": "Chest",
    "Dark Tunnel - 46. Tooth Thief's Pouch from barrel at scaffolding": "Lore",
    "Dark Tunnel - Wind spell chest in dark hole": "Chest",
    "Dark Tunnel - 50. Crafted Soul Injector from pot at light switch after getting the hat": "Lore",
    "Dark Tunnel - Light switch after getting the hat": "Barrier",
}

dark_tunnel_after_light_switch_barrier_locations: Dict[str, str] = {
    "Dark Tunnel - 57. Lady's Feather Hat from puppeteer": "Lore",
    "Dark Tunnel - 47. Blood Orc's Skin Sample from barrel above dark maze": "Lore",
    "Dark Tunnel - Fire spell chest inside dark maze": "Chest",
    "Dark Tunnel - 48. Chief's Skull from right mimic in mimic room": "Lore",
    "Dark Tunnel - 49. Chief's Skull from straight mimic in mimic room": "Lore",
    "Dark Tunnel - Thunder spell chest in mimic room": "Chest",
    "Dark Tunnel - 53. Ceremonial Sword from barrel at second statue": "Lore",
    "Dark Tunnel - Thunder barrier magic switches": "Barrier",
}

dark_tunnel_after_thunder_barrier_locations: Dict[str, str] = {
    "Dark Tunnel - 51. Hero's Insignia": "Lore",
    "Dark Tunnel - Chest in alcove": "Chest",
    "Dark Tunnel - 54. Banner of the Lance Hero from lightning enemy": "Lore",
    "Dark Tunnel - Floating platform switch one": "Barrier",
    "Dark Tunnel - Floating platform switch two": "Barrier",
    "Dark Tunnel - Floating platform switch three": "Barrier",
}

dark_tunnel_after_floating_platforms_locations: Dict[str, str] = {
    "Dark Tunnel - Chest on left side after floating platforms": "Chest",
}

dark_tunnel_after_bridge_collapse_locations: Dict[str, str] = {
    "Dark Tunnel - Arcane spell chest on collapsed bridge": "Chest",
    "Dark Tunnel - 52. Mutated Beast Claw from pot in big hall": "Lore",
    "Dark Tunnel - 69. Pontiff's Scepter from singular barrel in side room": "Lore",
    "Dark Tunnel - 71. Apocalypse Knight Record from knight enemy": "Lore",
    "Dark Tunnel - 103. Loyal Soul Shard from knight enemy": "Lore",
    "Dark Tunnel - Chest after knight enemy": "Chest",
    "Dark Tunnel - 65. Declaration of War from barrel at statue": "Lore",
    "Dark Tunnel - Vanessa": "Bosses",
    "Dark Tunnel - 100. King's Final Honor from Vanessa": "Lore",
    "Dark Tunnel - 78. Ancient Throne Rune from Vanessa": "Lore",
    "Dark Tunnel - 77. The Throne from Vanessa": "Lore",
}

spirit_realm_start_locations: Dict[str, str] = {
    "Spirit Realm - 72. Apocalypse Knight Shield from crystal at statue": "Lore",
    "Spirit Realm - 73. Apocalypse Knight Axe from enemy in trapped barrel": "Lore",
    "Spirit Realm - 79. Doctor's Mask hidden on ledge": "Lore",
    "Spirit Realm - Wind spell chest inside roof hole": "Chest",
    "Spirit Realm - Wind spell chest gate switch": "Metal Gate",
    "Spirit Realm - 55. Banner of the Lionhearted from crystal in doorway": "Lore",
    "Spirit Realm - 75. Apocalypse Knight Bow from bow enemy": "Lore",
}

spirit_realm_after_platforms_locations: Dict[str, str] = {
    "Spirit Realm - 61. Knight Kingdom Entry Pass from sword enemy": "Lore",
    "Spirit Realm - 58. Super Cleanser Soap from crystal on path": "Lore",
    "Spirit Realm - Chest hidden in dropdown alcove": "Chest",
    "Spirit Realm - 63. Inquisitor's List from crystal at second statue": "Lore",
    "Spirit Realm - Ice spell chest in right side alcove": "Chest",
    "Spirit Realm - Ice spell chest gate switch in right side alcove": "Metal Gate",
    "Spirit Realm - 76. Apocalypse Knight Sword from enemy": "Lore",
    "Spirit Realm - 74. Apocalypse Knight Staff from enemy": "Lore",
    "Spirit Realm - Arcane barrier magic switches": "Barrier",
}

spirit_realm_after_arcane_barrier_locations: Dict[str, str] = {
    "Spirit Realm - Thunder spell chest behind breakable wall": "Chest",
    "Spirit Realm - 86. Missing Person Poster on bridge": "Lore",
    "Spirit Realm - Platform shortcut switch": "Barrier",
    "Spirit Realm - 59. Exquisite Leather Lamp from crystal before Seal": "Lore",
}

spirit_realm_seal_locations: Dict[str, str] = {
    "Spirit Realm - 66. Attic Key from crystal at first Seal phase": "Lore",
    "Spirit Realm - 64. Envoy's Rune from crystal at first Seal phase": "Lore",
    "Spirit Realm - 60. Premium Grass Ash from crystal at first Seal phase": "Lore",
    "Spirit Realm - 62. Bone Chess Set from crystal at first Seal phase": "Lore",
    "Spirit Realm - First Seal magic barrier": "Barrier",
}

spirit_realm_after_first_seal_locations: Dict[str, str] = {
    "Spirit Realm - 90. Enchanted Shackles from second Seal phase": "Lore",
    "Spirit Realm - Fire spell chest at second Seal phase": "Chest",
    "Spirit Realm - Second Seal magic barrier": "Barrier",
}

spirit_realm_after_second_seal_locations: Dict[str, str] = {
    "Spirit Realm - 87. Saint's Cane from crystal at third statue": "Lore",
    "Spirit Realm - Statue shortcut gate switch": "Metal Gate",
    "Spirit Realm - 67. Halfling's Forelimb from crystal at elevator magic switch": "Lore",
    "Spirit Realm - Elevator magic switch": "Barrier",
}

spirit_realm_after_elevator_locations: Dict[str, str] = {
    "Spirit Realm - 68. Ratian Claw from crystal after elevator": "Lore",
    "Spirit Realm - Absorption spell chest behind crystals after elevator": "Chest",
    "Spirit Realm - Fire control magic switch": "Barrier",
    "Spirit Realm - Magic switch barrier switch": "Barrier",
    "Spirit Realm - Teleporter magic switch": "Barrier",
}

spirit_realm_after_teleport_locations: Dict[str, str] = {
    "Spirit Realm - 70. Abandoned Rag Doll from crystal on spiral stairs": "Lore",
    "Spirit Realm - Chest before boss behind breakable wall": "Chest",
    "Spirit Realm - 89. Bloodstained Key at statue before boss": "Lore",
    "Spirit Realm - Vanessa V2": "Bosses",
    "Spirit Realm - 101. Proud King's Crafted Soul Shard from Vanessa V2": "Lore",
    "Spirit Realm - Thunder spell from Vanessa V2": "Item",
}

abyss_locations: Dict[str, str] = {
    "Abyss - 80. Ceremonial Incense at first statue": "Lore",
}

abyss_after_first_teleport_locations: Dict[str, str] = {
    "Abyss - First gate switch": "Metal Gate",
}

abyss_after_first_gate_locations: Dict[str, str] = {
    "Abyss - 81. Moonlight Blade from trapped barrel": "Lore",
    "Abyss - 83. Castle Blueprint from crystal on brittle ledge": "Lore",
    "Abyss - Arcane spell chest on pillar": "Chest",
    "Abyss - 84. Witch Worshipper Puppet from pot right of pillars": "Lore",
    "Abyss - Giant maid barrier": "Barrier",
    "Abyss - Left gate trigger": "Metal Gate",
}

abyss_left_gate_at_trap_locations: Dict[str, str] = {
    "Abyss - 82. Prostitute's Chiffon from crystal in left trap gate": "Lore",
    "Abyss - Chest in left trap gate": "Chest",
}

abyss_after_giant_maid_barrier_locations: Dict[str, str] = {
    "Abyss - 85. Polymorphism Scroll from crystal behind gate": "Lore",
}

abyss_trials_lobby_locations: Dict[str, str] = {
    "Abyss - 88. Hero Summon Rune in front of statue": "Lore",
}

abyss_underground_trial_locations: Dict[str, str] = {
    "Abyss - Fire Spell chest underground trial": "Chest",
    "Abyss - Underground trial unlock enemies magic switch": "Barrier",
    "Abyss - 91. Gaseous Soul Essence from scissor enemy in underground trial": "Lore",
    "Abyss - Underground trial scissor enemy magic gate": "Barrier",
}

abyss_underground_trial_magic_switch_locations: Dict[str, str] = {
    "Abyss - Underground trial magic switch": "Barrier",
    "Abyss - 92. Semi-gaseous Soul Essence in front of underground trial magic switch": "Lore",
}

abyss_dark_tunnel_trial_locations: Dict[str, str] = {
    "Abyss - Thunder spell chest dark tunnel trial": "Chest",
    "Abyss - 95. Refined Soul Shard from maid enemy in dark tunnel trial": "Lore",
    "Abyss - Dark tunnel trial maid enemy barrier": "Barrier",
}

abyss_dark_tunnel_trial_magic_switch_locations: Dict[str, str] = {
    "Abyss - Dark Tunnel trial magic switch": "Barrier",
    "Abyss - 96. Knight's Soul Shard in front of dark tunnel trial magic switch": "Lore",
}

abyss_lava_ruins_trial_locations: Dict[str, str] = {
    "Abyss - Ice spell chest lava ruins trial": "Chest",
    "Abyss - 93. Enchanted Soul Shard from maid enemy in lava ruins trial": "Lore",
    "Abyss - Lava Ruins trial defeat maids enemy barrier": "Barrier",
}

abyss_lava_ruins_trial_magic_switch_locations: Dict[str, str] = {
    "Abyss - Lava Ruins trial magic switch": "Barrier",
    "Abyss - 94. Knight's Soul Shard in front of lava ruins trial magic switch": "Lore",
}

abyss_nonota_locations: Dict[str, str] = {
    "Abyss - 102. Lost Maiden's Crafted Soul Shard from Nonota": "Lore",
    "Abyss - Nonota": "Event",
}

lwn_locations: Dict[str, str] = {
    **shrine_start_locations,
    **shrine_after_first_magic_switch_locations,
    **shrine_cat_room_locations,
    **shrine_armor_hall_locations,
    **shrine_underground_shortcut_locations,
    **secret_passage_start_locations,
    **secret_passage_after_first_fire_barrier_locations,
    **secret_passage_enraged_armor_locations,
    **secret_passage_boss_shortcut_locations,
    **secret_passage_dark_tunnel_shortcut_locations,
    **underground_start_locations,
    **underground_after_wind_locations,
    **underground_lava_ruins_shortcut_locations,
    **underground_tania_shortcut_locations,
    **underground_after_fire_locations,
    **underground_after_fire_magic_switch_barrier_locations,
    **underground_tania_locations,
    **lava_ruins_start_locations,
    **lava_ruins_after_magic_platforms_locations,
    **lava_ruins_after_scissor_enemy_barrier_locations,
    **lava_ruins_after_fire_barrier_locations,
    **lava_ruins_monica_locations,
    **lava_ruins_monica_warp_locations,
    **lava_ruins_path_to_dark_tunnel_locations,
    **dark_tunnel_start_locations,
    **dark_tunnel_after_first_magic_barrier_locations,
    **dark_tunnel_after_first_gate_locations,
    **dark_tunnel_after_light_switch_barrier_locations,
    **dark_tunnel_after_thunder_barrier_locations,
    **dark_tunnel_after_floating_platforms_locations,
    **dark_tunnel_after_bridge_collapse_locations,
    **spirit_realm_start_locations,
    **spirit_realm_after_platforms_locations,
    **spirit_realm_after_arcane_barrier_locations,
    **spirit_realm_seal_locations,
    **spirit_realm_after_first_seal_locations,
    **spirit_realm_after_second_seal_locations,
    **spirit_realm_after_elevator_locations,
    **spirit_realm_after_teleport_locations,
    **abyss_locations,
    **abyss_after_first_teleport_locations,
    **abyss_after_first_gate_locations,
    **abyss_left_gate_at_trap_locations,
    **abyss_after_giant_maid_barrier_locations,
    **abyss_trials_lobby_locations,
    **abyss_underground_trial_locations,
    **abyss_underground_trial_magic_switch_locations,
    **abyss_dark_tunnel_trial_locations,
    **abyss_dark_tunnel_trial_magic_switch_locations,
    **abyss_lava_ruins_trial_locations,
    **abyss_lava_ruins_trial_magic_switch_locations,
    **abyss_nonota_locations,
}

location_name_to_id: Dict[str, int] = {name: base_id + index for index, name in enumerate(sorted(lwn_locations))}

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
        "Abyss - Left gate trigger",
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
        "Shrine - Meet Cat barrier",
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


def add_location_to_region(location_name, location_id, group_name, region, world):
    if (group_name == "Metal Gate"
            and world.options.shortcut_gate_behaviour.value == world.options.shortcut_gate_behaviour.option_vanilla):
        return
    elif (group_name == "Barrier"
          and world.options.barrier_behaviour.value == world.options.barrier_behaviour.option_vanilla):
        return
    elif (group_name == "Lore"
          and world.options.randomize_lore.value == Toggle.option_false):
        return
    region.locations.append(LWNLocation(world.player, location_name, location_id, region))


def append_locations(world: "LWNWorld"):
    for location_name in shrine_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = shrine_start_locations[location_name]
        region = world.multiworld.get_region("Shrine - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in shrine_after_first_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        group_name = shrine_after_first_magic_switch_locations[location_name]
        region = world.multiworld.get_region("Shrine - After first magic switch", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in shrine_cat_room_locations:
        location_id = location_name_to_id[location_name]
        group_name = shrine_cat_room_locations[location_name]
        region = world.multiworld.get_region("Shrine - Cat Room", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in shrine_armor_hall_locations:
        location_id = location_name_to_id[location_name]
        group_name = shrine_armor_hall_locations[location_name]
        region = world.multiworld.get_region("Shrine - Armor Hall", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in shrine_underground_shortcut_locations:
        location_id = location_name_to_id[location_name]
        group_name = shrine_underground_shortcut_locations[location_name]
        region = world.multiworld.get_region("Shrine - Underground shortcut", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in secret_passage_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = secret_passage_start_locations[location_name]
        region = world.multiworld.get_region("Secret passage - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in secret_passage_after_first_fire_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = secret_passage_after_first_fire_barrier_locations[location_name]
        region = world.multiworld.get_region("Secret passage - After first fire barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in secret_passage_enraged_armor_locations:
        location_id = location_name_to_id[location_name]
        group_name = secret_passage_enraged_armor_locations[location_name]
        region = world.multiworld.get_region("Secret Passage - Enraged Armor", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in secret_passage_boss_shortcut_locations:
        location_id = location_name_to_id[location_name]
        group_name = secret_passage_boss_shortcut_locations[location_name]
        region = world.multiworld.get_region("Secret Passage - Boss Shortcut", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in secret_passage_dark_tunnel_shortcut_locations:
        location_id = location_name_to_id[location_name]
        group_name = secret_passage_dark_tunnel_shortcut_locations[location_name]
        region = world.multiworld.get_region("Secret Passage - Dark Tunnel shortcut", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_start_locations[location_name]
        region = world.multiworld.get_region("Underground - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_after_wind_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_after_wind_locations[location_name]
        region = world.multiworld.get_region("Underground - After wind", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_lava_ruins_shortcut_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_lava_ruins_shortcut_locations[location_name]
        region = world.multiworld.get_region("Underground - Lava ruins shortcut", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_tania_shortcut_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_tania_shortcut_locations[location_name]
        region = world.multiworld.get_region("Underground - Tania shortcut", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_after_fire_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_after_fire_locations[location_name]
        region = world.multiworld.get_region("Underground - After fire", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_after_fire_magic_switch_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_after_fire_magic_switch_barrier_locations[location_name]
        region = world.multiworld.get_region("Underground - After fire magic switch barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in underground_tania_locations:
        location_id = location_name_to_id[location_name]
        group_name = underground_tania_locations[location_name]
        region = world.multiworld.get_region("Underground - Tania", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_start_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_after_magic_platforms_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_after_magic_platforms_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - After magic platforms", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_after_scissor_enemy_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_after_scissor_enemy_barrier_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - After scissor enemy barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_after_fire_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_after_fire_barrier_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - After Fire Barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_monica_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_monica_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - Monica", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_monica_warp_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_monica_warp_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - Monica warp", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in lava_ruins_path_to_dark_tunnel_locations:
        location_id = location_name_to_id[location_name]
        group_name = lava_ruins_path_to_dark_tunnel_locations[location_name]
        region = world.multiworld.get_region("Lava Ruins - Path to dark tunnel", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_start_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_first_magic_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_first_magic_barrier_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After first magic barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_first_gate_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_first_gate_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After first gate", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_light_switch_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_light_switch_barrier_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After light switch barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_thunder_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_thunder_barrier_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After thunder barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_floating_platforms_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_floating_platforms_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After floating platforms", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in dark_tunnel_after_bridge_collapse_locations:
        location_id = location_name_to_id[location_name]
        group_name = dark_tunnel_after_bridge_collapse_locations[location_name]
        region = world.multiworld.get_region("Dark Tunnel - After bridge collapse", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_start_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_start_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - Start", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_platforms_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_platforms_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After platforms", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_arcane_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_arcane_barrier_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After arcane barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_seal_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_seal_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - Seal", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_first_seal_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_first_seal_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After first Seal", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_second_seal_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_second_seal_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After second Seal", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_elevator_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_elevator_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After elevator", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in spirit_realm_after_teleport_locations:
        location_id = location_name_to_id[location_name]
        group_name = spirit_realm_after_teleport_locations[location_name]
        region = world.multiworld.get_region("Spirit Realm - After teleport", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_locations[location_name]
        region = world.multiworld.get_region("Abyss", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_after_first_teleport_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_after_first_teleport_locations[location_name]
        region = world.multiworld.get_region("Abyss - After first teleport", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_after_first_gate_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_after_first_gate_locations[location_name]
        region = world.multiworld.get_region("Abyss - After first gate", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_left_gate_at_trap_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_left_gate_at_trap_locations[location_name]
        region = world.multiworld.get_region("Abyss - Left gate at trap", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_after_giant_maid_barrier_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_after_giant_maid_barrier_locations[location_name]
        region = world.multiworld.get_region("Abyss - After giant maid barrier", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_trials_lobby_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_trials_lobby_locations[location_name]
        region = world.multiworld.get_region("Abyss - Trials Lobby", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_underground_trial_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_underground_trial_locations[location_name]
        region = world.multiworld.get_region("Abyss - Underground Trial", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_underground_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_underground_trial_magic_switch_locations[location_name]
        region = world.multiworld.get_region("Abyss - Underground Trial magic switch", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_dark_tunnel_trial_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_dark_tunnel_trial_locations[location_name]
        region = world.multiworld.get_region("Abyss - Dark Tunnel Trial", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_dark_tunnel_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_dark_tunnel_trial_magic_switch_locations[location_name]
        region = world.multiworld.get_region("Abyss - Dark Tunnel Trial magic switch", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_lava_ruins_trial_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_lava_ruins_trial_locations[location_name]
        region = world.multiworld.get_region("Abyss - Lava Ruins Trial", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_lava_ruins_trial_magic_switch_locations:
        location_id = location_name_to_id[location_name]
        group_name = abyss_lava_ruins_trial_magic_switch_locations[location_name]
        region = world.multiworld.get_region("Abyss - Lava Ruins Trial magic switch", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)

    for location_name in abyss_nonota_locations:
        if location_name != "Abyss - Nonota":
            location_id = location_name_to_id[location_name]
        else:
            location_id = None
        group_name = abyss_nonota_locations[location_name]
        region = world.multiworld.get_region("Abyss - Nonota", world.player)
        add_location_to_region(location_name, location_id, group_name, region, world)
