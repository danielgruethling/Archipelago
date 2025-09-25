from dataclasses import dataclass

from Options import Choice, Toggle, Range, PerGameCommonOptions, Visibility

DefaultOffToggle = Toggle


class Goal(Choice):
    """
    The Goal of the game.
    [Vanilla] Reaching and beating Nonota will end the game.
    [Magic Master] All attack magics (arcane, ice, fire and thunder) must be level 5 before Nonota can be reached.
    [Boss Hunt] All bosses need to be killed before Nonota can be reached.
    """
    display_name = "Goal"
    option_vanilla = 0
    option_magic_master = 1
    option_boss_hunt = 2

    default = option_vanilla


class Difficulty(Choice):
    """
    The Difficulty of the game.
    [Standard] This is the new default difficulty. Nobeta auto-regenerates life here and the game is easier in general.
    [Advanced] This is the suggested difficulty to use by the developers. If you want
    a challenge like in other soulslike games choose this difficulty.
    """
    display_name = "Difficulty"
    option_standard = 0
    option_advanced = 1

    default = option_standard


class RandomizeBossSouls(DefaultOffToggle):
    """
    This option will itemize killed bosses into soul items that are added to the item pool.
    Only relevant for Boss Hunt goal. Does nothing for other goals.
    """
    display_name = "Randomize Boss Souls"


class TrialKeys(DefaultOffToggle):
    """
    This setting will add keys to the item pool which are needed to open the teleports to each trial.
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


class NoArcane(DefaultOffToggle):
    """
    Nobeta will not be able to fire arcane magic. Only melee attack are possible until some form of magic is found.
    Arcane will still show up in the UI, but it will be impossible to fire arcane shots.
    """
    display_name = "Start without magic"


class RandomizeLore(DefaultOffToggle):
    """
    Lore items (green glowing circles) will be randomized into the item pool and give random items instead.
    """
    display_name = "Randomize lore items"


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

    default = option_start_with


class EntranceRandomization(DefaultOffToggle):
    """
    Randomizes the start level and the destinations of doors/post-cutscene level changes.
    """
    display_name = "Entrance randomization"
    visibility = Visibility.none


class ShortcutGateBehaviour(Choice):
    """
    Shortcut gate behaviour.
    [Vanilla] Shortcuts are closed and will be opened when their lever is pulled.
    [Always open] Shortcut gates will always be open.
    [Randomized] Adds shortcut gate items to the item pool.
    Pulling a lever will then reward a random item and the shortcut will only open when its item is found.
    """
    display_name = "Shortcut lever behaviour"
    visibility = Visibility.none
    option_vanilla = 0
    option_always_open = 1
    option_randomized = 2

    default = option_vanilla


class MagicPuzzleGateBehaviour(Choice):
    """
    Magic puzzle gate behaviour.
    [Vanilla] Magic puzzle gates are closed and will be opened when their puzzle is solved(destroy switches).
    [Always open] Magic puzzle gates will always be open.
    [Randomized] Adds puzzle gate items to the item pool.
    Solving a puzzle will then reward a random item and the puzzle gate will only open when its item is found.
    """
    display_name = "Magic puzzle gate behaviour"
    visibility = Visibility.none
    option_vanilla = 0
    option_always_open = 1
    option_randomized = 2

    default = option_vanilla


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
    randomize_boss_souls: RandomizeBossSouls
    trial_keys: TrialKeys
    trial_key_amount: TrialKeyAmount
    no_arcane: NoArcane
    randomize_lore: RandomizeLore
    shortcut_gate_behaviour: ShortcutGateBehaviour
    barrier_behaviour: MagicPuzzleGateBehaviour
    entrance_randomization: EntranceRandomization
    soul_gain_base_value: SoulGainBaseValue
    soul_gain_factor: SoulGainFactor
    death_link: DeathLink
    wind_requirements: WindRequirements
