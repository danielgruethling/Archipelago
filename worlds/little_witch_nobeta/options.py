from dataclasses import dataclass

from Options import Choice, Toggle, DefaultOnToggle, Range, PerGameCommonOptions, Visibility, OptionSet

DefaultOffToggle = Toggle


class Goal(Choice):
    """
    The Goal of the game.
    [Vanilla] Reaching and beating Nonota will end the game.
    [Magic Master] All attack magics (arcane, ice, fire and thunder) must be level 5 before Nonota can be reached.
    [Boss Hunt] All boss tokens gained by defeating bosses need to be collected before Nonota can be reached.
    [Lore Keeper] All lore items must be collected before Nonota can be reached.
    """
    display_name = "Goal"
    option_vanilla = 0
    option_magic_master = 1
    option_boss_hunt = 2
    option_lore_keeper = 3

    default = option_vanilla

class AbyssTrialRequirement(Choice):
    """
    Requirement to open the final teleport in Abyss to reach Nonota.
    [Vanilla] The three switches at the end of each trial must be destroyed.
    [Randomized Item] Requires three trial clear items, which are placed in the item pool.
    [Magic Master] All attack magics (arcane, ice, fire and thunder) must be level 5.
    [Boss Hunt] All boss tokens gained by defeating bosses need to be collected.
    [Lore Keeper] All lore items must be collected.
    """
    display_name = "Abyss Trial Requirement"
    option_vanilla = 0
    option_randomized_item = 1
    option_magic_master = 2
    option_boss_hunt = 3
    option_lore_keeper = 4

    default = option_vanilla

class TrialKeys(DefaultOffToggle):
    """
    This setting will add keys to the item pool which are needed to open the teleports to each Abyss trial.
    Opening a trial is done by dropping a key on a trial path.
    Three keys are needed to end the game. Putting more keys in the item pool will speed up progression.
    """
    display_name = "Trial keys"

class TrialKeyAmount(Range):
    """
    Amount of trial keys added to the item pool. Suggested amount is 5.
    """
    display_name = "Trial key amount"
    range_start = 3
    range_end = 7
    default = 5

class Difficulty(Choice):
    """
    The Difficulty of the game.
    [Standard] This is the new default difficulty. Nobeta auto-regenerates life here and the game is easier in general.
    [Advanced] This is the suggested difficulty to use by the developers. If you want
    a challenge like in other soulslike games choose this difficulty.
    """
    visibility = Visibility.none
    display_name = "Difficulty"
    option_standard = 0
    option_advanced = 1

    default = option_standard

class BossRequirementsDifficulty(Choice):
    """
    Logic requirements for being able to beat a boss.
    [Easy] Logic expects player to have multiple magic levels and absorption to beat later bosses.
    [Normal] Logic expects both magic and absorption to beat later bosses.
    [Absorption Only] Logic expects player to have absorption to beat later bosses.
    [No Requirements] There are no logic requirements for any boss. 
    """
    display_name = "Boss Requirements Difficulty"
    option_easy = 0
    option_normal = 1
    option_absorption_only = 2
    option_no_requirements = 3

    default = option_normal

class RandomizeBossSouls(DefaultOffToggle):
    """
    Bosses battles will only trigger once you get the corresponding boss soul items.
    """
    display_name = "Randomize Boss Souls"

class RandomizeBossTokens(DefaultOffToggle):
    """
    Boss tokens will be randomized into the item pool and can be collected from anywhere.
    Only relevant for Boss Hunt goal. Does nothing for other goals.
    """
    display_name = "Randomize Boss Tokens"

class SkippableBosses(DefaultOffToggle):
    """
    Boss battle triggers for Enraged Armor and Tania will be shrunk and visible to allow passing without fighting.
    Specter Armor and both Vanessa fights will have alternate warp points to the next level before their arenas.
    This can allow more flexibility with order of checks or affect progression order when boss souls are enabled.
    """
    display_name = "Skippable Bosses"

class ShortcutGateBehaviour(Choice):
    """
    Shortcut gate behaviour.
    [Vanilla] Shortcuts are closed and will be opened when their lever is pulled.
    [Always open] Shortcut gates will always be open.
    [Randomized] Adds shortcut gate items to the item pool.
    Pulling a lever will then reward a random item and the shortcut will only open when its item is found.
    """
    display_name = "Shortcut lever behaviour"
    option_vanilla = 0
    option_always_open = 1
    option_randomized = 2

    default = option_randomized

class MagicPuzzleGateBehaviour(Choice):
    """
    Magic puzzle gate behaviour.
    [Vanilla] Magic puzzle gates are closed and will be opened when their puzzle is solved (destroy switches).
    [Always open] Magic puzzle gates will always be open.
    [Randomized] Adds puzzle gate items to the item pool.
    Solving a puzzle will then reward a random item and the puzzle gate will only open when its item is found.
    """
    display_name = "Magic puzzle gate behaviour"
    option_vanilla = 0
    option_always_open = 1
    option_randomized = 2

    default = option_randomized
    
class NoArcane(DefaultOffToggle):
    """
    Nobeta will not be able to fire arcane magic. Only melee attack are possible until some form of magic is found.
    Arcane will still show up in the UI, but it will be impossible to fire arcane shots.
    """
    display_name = "Start without arcane"
    
class StartWithAbsorption(DefaultOffToggle):
    """
    Nobeta will start with absorption. Optionally recommended when starting without arcane.
    """
    display_name = "Start with absorption"

class NoManaRegeneration(DefaultOffToggle):
    """
    Disables mana regeneration, meaning mana must be recovered from dodges, parries, destroyable items, or consumables.
    For players looking for more of a challenge with no effect on logic.
    """
    display_name = "No mana regeneration"

class RandomizeLore(Choice):
    """
    How Lore items (green glowing circles) will be randomized into the item pool.
    [Vanilla] Lore items will all be in their vanilla locations.
    [Randomized] Lore items will be randomized in the item pool, and picking them up will be a check.
    [No Lore] Lore items will be removed from the item pool, but picking them up will be a check.
    If this is selected while lore keeper is set as either the goal or abyss trial requirement, it will default to "Randomized". 
    """
    display_name = "Randomize lore items"
    option_vanilla = 0
    option_randomized = 1
    option_no_lore = 2

    default = option_randomized

class RandomizeBreakableWalls(DefaultOffToggle):
    """
    Breakable walls can only be broken when a corresponding item is given.
    Attempting to break a wall will also grant a check.
    """
    visibility = Visibility.none
    display_name = "Wallsanity"

class RandomizeJugs(DefaultOffToggle):
    """
    Breaking a jug will grant a check.
    """
    visibility = Visibility.none
    display_name = "Jugsanity"
    
class RandomizeBarrels(DefaultOffToggle):
    """
    Breaking a barrel will grant a check.
    """
    visibility = Visibility.none
    display_name = "Barrelsanity"
    
class RandomizeBrokenDolls(DefaultOffToggle):
    """
    Breaking a broken doll will grant a check.
    """
    visibility = Visibility.none
    display_name = "Dollsanity"
    
class RandomizeLightOrb(DefaultOffToggle):
    """
    Access to using light orbs in Dark Tunnel requires an item. Does not add any locations.
    """
    visibility = Visibility.none
    display_name = "Randomize Light Orb"
    
class RandomizeCrystalBalls(DefaultOffToggle):
    """
    Activating crystal balls that dissipate dark fog in Dark Tunnel will grant a check.
    Note that any crystal ball that opens a barrier is not included.
    Disabling dark fog (non-progression) will also be added to the item pool.
    """
    visibility = Visibility.none
    display_name = "Randomize Crystal Balls"
    
class RandomizeCrystals(DefaultOffToggle):
    """
    Breaking a crystal (in Spirit Realm and Abyss) will grant a check.
    """
    visibility = Visibility.none
    display_name = "Crystalsanity"

class WindRequirements(Choice):
    """
    Double Jump logic requirements.
    [Start with] Will put one copy of Wind magic in the starting inventory and thus allow double jump from the start.
    [Start without] Will have all 5 Wind spells in the multiworld.
    [Less wind requirements] Skips some logic requirements of Wind magic in favor of trick jumps and damage boosts.
    """
    display_name = "Wind Requirements"
    option_start_with = 0
    option_start_without = 1
    option_less_wind_requirements = 2

    default = option_start_without

class SkipsInLogic(OptionSet):
    """
    List of in-bound and glitchless skips to be considered in logic.

    Valid values: All, Underground Wind Skip, Underground Barrier Before Tania Skip,
    Lava Ruins Monica Skip, Lava Ruins Platforms Skip, Dark Tunnel Hat Skip,
    Spirit Realm Arcane Barrier Skip, Spirit Realm Seal Barrier Skip, Spirit Realm Elevator Skip,
    Abyss Giant Maid Skip, Abyss Underground Trial Barrier Skip
    """
    display_name = "Skips in logic"
    valid_keys = [
        "All",
        "Underground Wind Skip",
        "Underground Barrier Before Tania Skip",
        "Lava Ruins Monica Skip",
        "Lava Ruins Platforms Skip",
        "Dark Tunnel Hat Skip",
        "Spirit Realm Arcane Barrier Skip",
        "Spirit Realm Seal Barrier Skip",
        "Spirit Realm Elevator Skip",
        "Abyss Giant Maid Skip",
        "Abyss Underground Trial Barrier Skip",
    ]

class EntranceRandomization(DefaultOffToggle):
    """
    Randomizes the start level and the destinations of doors/post-cutscene level changes.
    """
    display_name = "Entrance randomization"
    visibility = Visibility.none


class StartingArea(Choice):
    """
    Sets starting area, default is starting in Shrine
    """
    display_name = "Starting Area"
    visibility = Visibility.none
    option_shrine = 0
    option_underground = 1
    option_lava_ruins = 2
    option_dark_tunnel = 3

    default = option_shrine
    
class DisableDarkTunnelThunderWall(DefaultOffToggle):
    """
    Disable thunder wall in Dark Tunnel, which removes the thunder requirement for passing through the stage.
    """
    display_name = "Disable Dark Tunnel thunder wall"

class DisableDarkTunnelBridgeCollapse(DefaultOnToggle):
    """
    Disables the Dark Tunnel bridge collapse cutscene and allows two-way movement through the bridge in logic.
    This can help create more interesting worlds when gate or entrance randomization is enabled.
    """
    display_name = "Disable Dark Tunnel bridge collapse"

class DisableUnimportantCutscenes(DefaultOffToggle):
    """
    Disables any story cutscenes that do not move or warp the player. Does not affect logic.
    """
    display_name = "Disable unimportant cutscenes"

class SoulGainBaseValue(Range):
    """
    Whenever the randomizer would add souls to your inventory it will at least add this amount.
    """
    display_name = "Soul gain base value"
    range_start = 1
    range_end = 1000
    default = 250

class SoulGainFactor(Range):
    """
    Whenever the randomizer would add souls to your inventory it will multiply the soul gain base value with
    a factor randomly chosen between 1 and the configured soul gain factor.
    """
    display_name = "Soul gain factor"
    range_start = 1
    range_end = 100
    default = 2

class FillerCrystalWeight(Range):
    """
    Weight of a filler being a crystal item, where (weight / total weight of all filler) is the likelihood.
    Can be any type (HP, Magic, Defense, Arcane, Holy) and any size.
    """
    display_name = "Filler Crystal Weight"
    range_start = 0
    range_end = 100
    default = 0

class FillerSoulsWeight(Range):
    """
    Weight of a filler being souls, where (weight / total weight of all filler) is the likelihood.
    Can be any type (Soul Essense, HP Souls, MP Souls) and a random amount.
    """
    display_name = "Filler Crystal Weight"
    range_start = 0
    range_end = 100
    default = 0

class TrapFillPercentage(Range):
    """
    Replaces a percentage of filler items with traps.
    """
    display_name = "Trap fill percentage"
    range_start = 0
    range_end = 100
    default = 0

class ManaDrainTrapWeight(Range):
    """
    Weight of a trap being a Mana Drain Trap, where (weight / total weight of all traps) is the likelihood.
    A mana drain trap instantly depletes all of Nobeta's mana.
    """
    display_name = "Mana Drain trap weight"
    range_start = 0
    range_end = 100
    default = 0
    
class BonkTrapWeight(Range):
    """
    Weight of a trap being a Bonk Trap, where (weight / total weight of all traps) is the likelihood.
    A bonk trap launches Nobeta in a random direction.
    """
    display_name = "Bonk trap weight"
    range_start = 0
    range_end = 100
    default = 0

class DeathLink(DefaultOffToggle):
    """
    On death a trigger to kill all other deathlink players will be sent. When another deathlink
    player dies you die as well.
    """
    display_name = "Deathlink"
    

@dataclass
class LWNOptions(PerGameCommonOptions):
    goal: Goal
    difficulty: Difficulty
    boss_requirements_difficulty: BossRequirementsDifficulty
    randomize_boss_souls: RandomizeBossSouls
    randomize_boss_tokens: RandomizeBossTokens
    skippable_bosses: SkippableBosses
    trial_keys: TrialKeys
    trial_key_amount: TrialKeyAmount
    abyss_trial_requirement: AbyssTrialRequirement
    no_arcane: NoArcane
    start_with_absorption: StartWithAbsorption
    no_mana_regeneration: NoManaRegeneration
    randomize_lore: RandomizeLore
    randomize_breakable_walls: RandomizeBreakableWalls
    randomize_jugs: RandomizeJugs
    randomize_barrels: RandomizeBarrels
    randomize_broken_dolls: RandomizeBrokenDolls
    randomize_light_orb: RandomizeLightOrb
    randomize_crystal_balls: RandomizeCrystalBalls
    randomize_crystals: RandomizeCrystals
    wind_requirements: WindRequirements
    skips_in_logic: SkipsInLogic
    entrance_randomization: EntranceRandomization
    starting_area: StartingArea
    shortcut_gate_behaviour: ShortcutGateBehaviour
    barrier_behaviour: MagicPuzzleGateBehaviour
    disable_dark_tunnel_thunder_wall: DisableDarkTunnelThunderWall
    disable_dark_tunnel_bridge_collapse: DisableDarkTunnelBridgeCollapse
    disable_unimportant_cutscenes: DisableUnimportantCutscenes
    soul_gain_base_value: SoulGainBaseValue
    soul_gain_factor: SoulGainFactor
    filler_crystal_weight: FillerCrystalWeight
    filler_souls_weight: FillerSoulsWeight
    trap_fill_percentage: TrapFillPercentage
    mana_drain_trap_weight: ManaDrainTrapWeight
    bonk_trap_weight: BonkTrapWeight
    death_link: DeathLink
