"""Compile a list of hints based on the settings."""
import random
from re import U
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Regions import Regions

from randomizer.Lists.Item import NameFromKong
from randomizer.Lists.MapsAndExits import GetMapId
from randomizer.Lists.ShufflableExit import ShufflableExits
from randomizer.Lists.Translations import setLanguage
from randomizer.Lists.WrinklyHints import hints
from randomizer.Spoiler import Spoiler
from randomizer.Patching.UpdateHints import updateRandomHint, ConvertHint
from randomizer.Lists.WrinklyHints import HintLocation, hints
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Transitions import Transitions
from randomizer.Enums.Translations import Translations
from randomizer.Enums.Languages import Languages


class Hint:
    """Hint object for Wrinkly hint text."""

    def __init__(
        self,
        *,
        hint="",
        important=True,
        priority=1,
        kongs=[Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky],
        repeats=1,
        base=False,
        keywords=[],
        permitted_levels=[Levels.JungleJapes, Levels.AngryAztec, Levels.FranticFactory, Levels.GloomyGalleon, Levels.FungiForest, Levels.CrystalCaves, Levels.CreepyCastle],
        subtype="joke",
        joke=False,
        joke_defined=False,
    ):
        """Create wrinkly hint text object."""
        self.kongs = kongs.copy()
        self.hint = hint
        self.important = important
        self.priority = priority
        self.repeats = repeats
        self.base = base
        self.used = False
        self.was_important = important
        self.original_repeats = repeats
        self.original_priority = priority
        self.keywords = keywords.copy()
        self.permitted_levels = permitted_levels.copy()
        self.subtype = subtype
        self.joke = base
        self.base_hint = hint
        if joke_defined:
            self.joke = joke

    def use_hint(self):
        """Set hint as used."""
        if self.repeats == 1:
            self.used = True
            self.repeats = 0
        else:
            self.repeats -= 1
            self.priority += 1

    def downgrade(self):
        """Downgrade hint status."""
        self.important = False


hint_list = [
    Hint(hint=Translations.Wrinkly_DKInDK64, important=False, base=True),
    Hint(hint=Translations.Wrinkly_FungiBK, important=False, base=True),
    Hint(hint=Translations.Wrinkly_TrapBubble, important=False, base=True),
    Hint(hint=Translations.Wrinkly_TinyDixie, important=False, base=True),
    Hint(hint=Translations.Wrinkly_Mornin, important=False, base=True),
    Hint(hint=Translations.Wrinkly_LankyRelatives, important=False, base=True),
    Hint(hint=Translations.Wrinkly_ChunkyJump, important=False, base=True),
    Hint(hint=Translations.Wrinkly_TinySlow, important=False, base=True),
    Hint(hint=Translations.Wrinkly_CandyJapesFungi, important=False, base=True),
    Hint(hint=Translations.Wrinkly_KRoolVictorious, important=False, base=True),
    Hint(hint=Translations.Wrinkly_DK64RandoOrigins, important=False, base=True),
    Hint(hint=Translations.Wrinkly_VanillaIGTMax, important=False, base=True),
    Hint(hint=Translations.Wrinkly_ChunkyKiddy, important=False, base=True),
    Hint(hint=Translations.Wrinkly_FungiMushJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_CavesIglooJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_FactoryFloors, important=False, base=True),
    Hint(hint=Translations.Wrinkly_AztecSandstorm, important=False, base=True),
    Hint(hint=Translations.Wrinkly_IslesNoKey, important=False, base=True),
    Hint(hint=Translations.Wrinkly_RabbitJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_BeetleJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_VultureJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_OwlJoke, important=False, base=True),
    Hint(hint=Translations.Wrinkly_CoinsBuyMoves, important=False, base=True),
    Hint(hint=Translations.Wrinkly_SoundToggle, important=False, base=True),
    Hint(hint=Translations.Wrinkly_CoinHoard, important=False, base=True),
    Hint(hint=Translations.Wrinkly_CapturePad, important=False, base=True),
    Hint(hint=Translations.Wrinkly_NothingToSay, important=False, base=True),
    Hint(hint=Translations.Wrinkly_ForgotHint, important=False, base=True),
    Hint(hint=Translations.Wrinkly_IDontKnow, important=False, base=True),
    Hint(hint=Translations.Wrinkly_Lost, important=False, base=True),
    Hint(hint=Translations.Wrinkly_NeverHeardOfHim, important=False, base=True),
    Hint(hint=Translations.Wrinkly_TranslatorCredit, important=False, base=True),
    Hint(hint=Translations.Wrinkly_NoAccents, important=False, base=True),
    Hint(hint=Translations.Wrinkly_PeakOfRandomizers, important=False, base=True),
    Hint(hint=Translations.Wrinkly_YashichiOven, important=False, base=True),
    Hint(hint=Translations.Wrinkly_WannaBecomeFamous, important=False, base=True),
    Hint(hint=Translations.Wrinkly_SpikeVegeta, important=False, base=True),
]


def pushHintToList(hint: Hint):
    """Push hint to hint list."""
    hint_list.append(hint)


def resetHintList():
    """Reset hint list to default state."""
    for hint in hint_list:
        if not hint.base:
            hint_list.remove(hint)
        else:
            hint.used = False
            hint.important = hint.was_important
            hint.repeats = hint.original_repeats
            hint.priority = hint.original_priority
            hint.hint = ConvertHint(hint.base_hint, [])


def compileHints(spoiler: Spoiler):
    """Push hints to hint list based on settings."""
    language_db = {"english": Languages.English, "french_ca": Languages.FrenchCA}
    selected_language = Languages.English
    if spoiler.settings.hint_language in language_db:
        selected_language = language_db[spoiler.settings.hint_language]
    setLanguage(selected_language)
    resetHintList()
    all_levels = [Levels.JungleJapes, Levels.AngryAztec, Levels.FranticFactory, Levels.GloomyGalleon, Levels.FungiForest, Levels.CrystalCaves, Levels.CreepyCastle]
    # K Rool Order
    if spoiler.settings.krool_phase_order_rando and len(spoiler.settings.krool_order) > 1:
        associated_hint = f"{ConvertHint(Translations.Misc_KRoolOrderIs,[])} {NameFromKong(spoiler.settings.krool_order[0])}"
        for x in range(len(spoiler.settings.krool_order)):
            if x != 0:
                associated_hint += f" {ConvertHint(Translations.Generic_Then,[])} {NameFromKong(spoiler.settings.krool_order[x])}"
        hint_list.append(Hint(hint=associated_hint, repeats=2, kongs=spoiler.settings.krool_order.copy(), subtype="k_rool"))
    # K. Rool Moves
    kong_list = [Translations.Generic_DK_Long, Translations.Generic_Diddy, Translations.Generic_Lanky, Translations.Generic_Tiny, Translations.Generic_Chunky]
    kong_cryptic = [
        [
            Translations.Cryptic_DK_Faster,
            Translations.Cryptic_DK_Spurts,
            Translations.Cryptic_DK_Tie,
            Translations.Cryptic_DK_Bongos,
        ],
        [
            Translations.Cryptic_Diddy_Fly,
            Translations.Cryptic_Diddy_DKC,
            Translations.Cryptic_Diddy_Red,
            Translations.Cryptic_Diddy_FreeTiny,
        ],
        [
            Translations.Cryptic_Lanky_Balloon,
            Translations.Cryptic_Lanky_Overalls,
            Translations.Cryptic_Lanky_Beetle,
            Translations.Cryptic_Lanky_Style,
        ],
        [Translations.Cryptic_Tiny_Jazz, Translations.Cryptic_Tiny_Toes, Translations.Cryptic_Tiny_Feather, Translations.Cryptic_Tiny_Shrink],
        [
            Translations.Cryptic_Chunky_HellOfAGuy,
            Translations.Cryptic_Chunky_Boulders,
            Translations.Cryptic_Chunky_ToyMonster,
            Translations.Cryptic_Chunky_DogadonBow,
        ],
    ]
    level_list = [
        Translations.Generic_Japes,
        Translations.Generic_Aztec,
        Translations.Generic_Factory,
        Translations.Generic_Galleon,
        Translations.Generic_Fungi,
        Translations.Generic_Caves,
        Translations.Generic_Castle,
        Translations.Generic_Helm,
    ]
    level_list_isles = [
        Translations.Generic_Japes,
        Translations.Generic_Aztec,
        Translations.Generic_Factory,
        Translations.Generic_Galleon,
        Translations.Generic_Fungi,
        Translations.Generic_Caves,
        Translations.Generic_Castle,
        Translations.Generic_Isles,
    ]
    level_cryptic = [
        [
            Translations.Cryptic_Japes_Storm,
            Translations.Cryptic_Japes_Mountain,
            Translations.Cryptic_Japes_Retailers,
        ],
        [Translations.Cryptic_Aztec_Vases, Translations.Cryptic_Aztec_Cages, Translations.Cryptic_Aztec_Totem],
        [Translations.Cryptic_Factory_ToyProduction, Translations.Cryptic_Factory_BlockTower, Translations.Cryptic_Factory_ArcadeYear, Translations.Cryptic_Factory_ArcadeCost],
        [Translations.Cryptic_Galleon_Water, Translations.Cryptic_Galleon_Seal, Translations.Cryptic_Galleon_GoldTower],
        [Translations.Cryptic_Fungi_Retailers, Translations.Cryptic_Fungi_Night, Translations.Cryptic_Fungi_Owl],
        [
            Translations.Cryptic_Caves_Water,
            Translations.Cryptic_Caves_IceShield,
            Translations.Cryptic_Caves_IceTomato,
        ],
        [Translations.Cryptic_Castle_Battlements, Translations.Cryptic_Castle_IntFeatures, Translations.Cryptic_Castle_ExtFeatures],
        [Translations.Cryptic_Helm_Timer, Translations.Cryptic_Helm_Boss, Translations.Cryptic_Helm_CB],
    ]
    # Make Isles Versions
    level_cryptic_isles = level_cryptic.copy()
    level_cryptic_isles.remove(level_cryptic_isles[-1])
    level_cryptic_isles.append([Translations.Cryptic_Isles_Hub, Translations.Cryptic_Isles_Face, Translations.Cryptic_Isles_Shops])

    if spoiler.settings.shuffle_items == "moves" and spoiler.move_data is not None:
        krool_move_requirements = [0, 2, 1, 1, 4]
        total_moves_for_krool = 0
        for x in spoiler.settings.krool_order:
            total_moves_for_krool += krool_move_requirements[x]
        moves_of_importance = [
            {
                "name": "Monkeyport",
                "name_cryptic": "Their third special move",
                "key": 0x03,
                "kong": 3,
                "move_type": 0,
                "move_index": 3,
                "level": 0,
                "shop": 0,
                "important": True,
            },
            {"name": "Mini Monkey", "name_cryptic": "Their first special move", "key": 0x01, "kong": 3, "move_type": 0, "move_index": 1, "level": 0, "shop": 0, "important": True},
            {
                "name": "Coconut Gun",
                "name_cryptic": "Their gun",
                "key": 0x21,
                "kong": 0,
                "move_type": 2,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": True,
            },
            {"name": "Chimpy Charge", "name_cryptic": "Their first special move", "key": 0x01, "kong": 1, "move_type": 0, "move_index": 1, "level": 0, "shop": 0, "important": True},
            {
                "name": "Gorilla Gone",
                "name_cryptic": "Their third special move",
                "key": 0x03,
                "kong": 4,
                "move_type": 0,
                "move_index": 3,
                "level": 0,
                "shop": 0,
                "important": True,
            },
            {
                "name": "Ponytail Twirl",
                "key": 0x02,
                "kong": 3,
                "move_type": 0,
                "move_index": 2,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Baboon Blast",
                "key": 0x01,
                "kong": 0,
                "move_type": 0,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Strong Kong",
                "key": 0x02,
                "kong": 0,
                "move_type": 0,
                "move_index": 2,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Gorilla Grab",
                "key": 0x03,
                "kong": 0,
                "move_type": 0,
                "move_index": 3,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Rocketbarrel Boost",
                "key": 0x02,
                "kong": 1,
                "move_type": 0,
                "move_index": 2,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Simian Spring",
                "key": 0x03,
                "kong": 1,
                "move_type": 0,
                "move_index": 3,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Orangstand",
                "key": 0x01,
                "kong": 2,
                "move_type": 0,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Baboon Balloon",
                "key": 0x02,
                "kong": 2,
                "move_type": 0,
                "move_index": 2,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Orangstand Sprint",
                "key": 0x03,
                "kong": 2,
                "move_type": 0,
                "move_index": 3,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Hunky Chunky",
                "key": 0x01,
                "kong": 4,
                "move_type": 0,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Primate Punch",
                "key": 0x02,
                "kong": 4,
                "move_type": 0,
                "move_index": 2,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Peanut Popguns",
                "key": 0x21,
                "kong": 1,
                "move_type": 2,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Grape Shooter",
                "key": 0x21,
                "kong": 2,
                "move_type": 2,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Feather Bow",
                "key": 0x21,
                "kong": 3,
                "move_type": 2,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Pineapple Launcher",
                "key": 0x21,
                "kong": 4,
                "level": 0,
                "move_type": 2,
                "move_index": 1,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Bongo Blast",
                "key": 0x41,
                "kong": 0,
                "move_type": 4,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Guitar Gazump",
                "key": 0x41,
                "kong": 1,
                "move_type": 4,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Trombone Tremor",
                "key": 0x41,
                "kong": 2,
                "move_type": 4,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Saxophone Slam",
                "key": 0x41,
                "kong": 3,
                "move_type": 4,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {
                "name": "Triangle Trample",
                "key": 0x41,
                "kong": 4,
                "move_type": 4,
                "move_index": 1,
                "level": 0,
                "shop": 0,
                "important": False,
            },
            {"name": "Slam Upgrade", "key": 0x12, "kong": 0, "move_type": 1, "move_index": 2, "level": 0, "shop": 0, "important": False, "shared": True},
            {"name": "Homing Ammo", "key": 0x22, "kong": 0, "move_type": 2, "move_index": 2, "level": 0, "shop": 0, "important": False, "shared": True},
            {"name": "Sniper Scope", "key": 0x23, "kong": 0, "move_type": 2, "move_index": 3, "level": 0, "shop": 0, "important": False, "shared": True},
            {"name": "Ammo Belt Upgrade", "key": 0x32, "kong": 0, "move_type": 3, "move_index": 2, "level": 0, "shop": 0, "important": False, "shared": True},
            {"name": "Instrument Upgrade", "key": 0x42, "kong": 0, "move_type": 4, "move_index": 2, "level": 0, "shop": 0, "important": False, "shared": True},
        ]
        shop_owners = [Translations.Generic_Cranky, Translations.Generic_Funky, Translations.Generic_Candy]
        for move in moves_of_importance:
            move["key"] = ((move["move_type"] & 7) << 5) + (((move["move_index"] - 1) & 3) << 3) + (move["kong"] & 7)
            move["purchase_kong"] = -1
            move["level"] = -1
            move["shop"] = -1
        shop_contains = {}
        for shop in range(3):
            for kong in range(5):
                for level in range(8):
                    for move in moves_of_importance:
                        if spoiler.move_data[shop][kong][level] == move["key"]:
                            move["level"] = level
                            move["shop"] = shop
                            move["purchase_kong"] = kong
                            if spoiler.settings.wrinkly_hints == "cryptic":
                                shop_level_name = f"{ConvertHint(shop_owners[shop],[])}{ConvertHint(Translations.Generic_PersonalIn,[])}{level}"
                            else:
                                shop_level_name = f"{ConvertHint(level_list_isles[level],[])} {ConvertHint(shop_owners[shop],[])}"
                            is_shared = False
                            if "shared" in move:
                                is_shared = move["shared"]
                            if shop_level_name in shop_contains:
                                if not is_shared:
                                    shop_contains[shop_level_name]["moves"].append(move["name"])
                                    shop_contains[shop_level_name]["kongs"].append(kong)
                            else:
                                kong_lst = [kong]
                                if is_shared:
                                    kong_lst = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
                                shop_contains[shop_level_name] = {"moves": [move["name"]], "kongs": kong_lst.copy()}
        # All moves in a shop
        shop_contain_keys = list(shop_contains.keys())
        random.shuffle(shop_contain_keys)
        priority_barriers = [3, 6, 10]
        shop_priority = 1
        shop_importance = True
        for shop_index, shop in enumerate(shop_contain_keys):
            shop_name = shop
            if ConvertHint(Translations.Generic_PersonalIn, []) in shop_name:
                level_index = int(shop_name.split(ConvertHint(Translations.Generic_PersonalIn, []))[1].strip())
                shop_name = random.choice(level_cryptic_isles[level_index])
            if len(shop_contains[shop]["moves"]) > 2:
                item_names = ", ".join(shop_contains[shop]["moves"][:-1])
                item_names = f"{item_names} {ConvertHint(Translations.Generic_And,[])} {shop_contains[shop]['moves'][-1]}"
            elif len(shop_contains[shop]["moves"]) == 2:
                item_names = f" {ConvertHint(Translations.Generic_And,[])} ".join(shop_contains[shop]["moves"])
            else:
                item_names = shop_contains[shop]["moves"][0]
            hint_list.append(
                Hint(
                    hint=f"{shop_name} {ConvertHint(Translations.Generic_Contains,[])} {item_names}",
                    priority=shop_priority,
                    important=shop_importance,
                    kongs=shop_contains[shop]["kongs"],
                    keywords=shop_contains[shop]["moves"],
                    subtype="shop_dump",
                )
            )
            if shop_importance:
                hint_list.append(
                    Hint(
                        hint=f"{shop_name} {ConvertHint(Translations.Generic_Contains,[])} {item_names}",
                        important=False,
                        kongs=shop_contains[shop]["kongs"],
                        keywords=shop_contains[shop]["moves"],
                        subtype="shop_dump",
                    )
                )
            if shop_priority <= len(priority_barriers):
                if (shop_index + 1) >= priority_barriers[shop_priority - 1]:
                    if shop_priority == len(priority_barriers):
                        shop_importance = False
                    else:
                        shop_priority += 1

        for move in moves_of_importance:
            if move["level"] > -1 and move["shop"] > -1 and move["purchase_kong"] > -1:
                if spoiler.settings.wrinkly_hints == "cryptic":
                    kong_name = random.choice(kong_cryptic[move["purchase_kong"]])
                    level_name = random.choice(level_cryptic[move["level"]])
                else:
                    kong_name = kong_list[move["purchase_kong"]]
                    level_name = level_list[move["level"]]
                move_name = move["name"]

                shop_name = shop_owners[move["shop"]]
                text = f"{move_name} {ConvertHint(Translations.Generic_CanBePurchasedFrom,[])} {ConvertHint(shop_name,[])} {ConvertHint(Translations.Generic_In,[])} {ConvertHint(level_name,[])}."
                hint_list.append(Hint(hint=text, priority=2, kongs=[move["purchase_kong"]], important=move["important"], keywords=[move["name"]], subtype="move_location"))
    if spoiler.settings.kong_rando:
        kong_json = spoiler.shuffled_kong_placement
        placement_levels = [
            {
                "name": "Jungle Japes",
                "level": 0,
            },
            {
                "name": "Llama Temple",
                "level": 1,
            },
            {
                "name": "Tiny Temple",
                "level": 1,
            },
            {
                "name": "Frantic Factory",
                "level": 2,
            },
        ]
        for kong_map in placement_levels:
            kong_index = kong_json[kong_map["name"]]["locked"]["kong"]
            free_kong = kong_json[kong_map["name"]]["puzzle"]["kong"]
            level_index = kong_map["level"]
            if spoiler.settings.wrinkly_hints == "cryptic":
                if not kong_index == Kongs.any:
                    kong_name = random.choice(ConvertHint(kong_cryptic[kong_index], []))
                level_name = random.choice(ConvertHint(level_cryptic[level_index], []))
            else:
                if not kong_index == Kongs.any:
                    kong_name = kong_list[kong_index]
                level_name = level_list[level_index]
            hint_priority = 2
            if kong_index == Kongs.any:
                kong_name = Translations.Generic_AnEmptyCage
                hint_priority = 3
            hint_list.append(
                Hint(
                    hint=f"{ConvertHint(kong_name,[])} {ConvertHint(Translations.Generic_CanBeFoundIn,[])} {ConvertHint(level_name,[])}.",
                    kongs=[free_kong],
                    priority=hint_priority,
                    subtype="kong_location",
                )
            )
    if spoiler.settings.random_patches:
        level_patches = {
            "DK Isles": 0,
            "Jungle Japes": 0,
            "Angry Aztec": 0,
            "Frantic Factory": 0,
            "Gloomy Galleon": 0,
            "Fungi Forest": 0,
            "Crystal Caves": 0,
            "Creepy Castle": 0,
        }
        for patch in spoiler.dirt_patch_placement:
            for level in level_patches:
                if level in patch:
                    level_patches[level] += 1
        level_ordering = list(level_patches.keys())
        random.shuffle(level_ordering)
        for importance in range(2):
            for index in range(4):
                level_name = level_ordering[index + (4 * importance)]
                patch_count = level_patches[level_name]
                if patch_count > 0:
                    patch_mult = Translations.Generic_Patches
                    patch_pre = Translations.Generic_Are
                    if patch_count == 1:
                        patch_mult = Translations.Generic_Patch
                        patch_pre = Translations.Generic_Is
                    patch_text = (
                        f"{ConvertHint(Translations.Generic_There,[])} {ConvertHint(patch_pre,[])} {patch_count} {ConvertHint(patch_mult,[])} {ConvertHint(Translations.Generic_In,[])} {level_name}"
                    )
                    hint_list.append(Hint(hint=patch_text, priority=index + 3, important=False, subtype="level_patch_count"))
        patch_list = spoiler.dirt_patch_placement.copy()
        random.shuffle(patch_list)
        for importance in range(2):
            for index in range(4):
                patch_name = patch_list[index + (importance * 4)]
                patch_text = f"{ConvertHint(Translations.Generic_ThereIsADirtPatchLocatedAt,[])} {patch_name}"
                hint_list.append(Hint(hint=patch_text, priority=index + 4, important=importance == 0, subtype="patch_location"))
    if spoiler.settings.shuffle_loading_zones == "all":
        AddLoadingZoneHints(spoiler)
    if spoiler.settings.coin_door_open == "need_both" or spoiler.settings.coin_door_open == "need_rw":
        hint_list.append(Hint(hint=f"{spoiler.settings.medal_requirement} {ConvertHint(Translations.Generic_MedalsRequiredJetpac,[])}", priority=4, subtype="medal"))
    if spoiler.settings.perma_death:
        hint_list.append(Hint(hint=ConvertHint(Translations.Generic_PermadeathCurse, []), subtype="permadeath"))
    if spoiler.settings.level_randomization != "level_order":
        for x in spoiler.settings.krool_keys_required:
            key_index = x - 4
            if spoiler.settings.wrinkly_hints == "cryptic":
                level_name = random.choice(level_cryptic[key_index])
            else:
                level_name = level_list[key_index]
            hint_list.append(
                Hint(
                    hint=ConvertHint(
                        Translations.Generic_GreatestFoe, [ConvertHint(level_name, [])]
                    ),  # f"{Translations.Generic_YouWillNeedToObtainTheKeyFrom} {level_name} {Translations.Generic_ToFightYourGreatestFoe}",
                    important=False,
                    subtype="key_is_required",
                )
            )
    # Way of the Hoard hints
    shopNames = ["Candy", "Funky", "Cranky"]
    moveSpecificSuffixes = [" Donkey", " Diddy", " Lanky", " Tiny", " Chunky", " Shared"]
    wothLocations = [key for key in spoiler.woth.keys() if any(shopName in key for shopName in shopNames)]
    selectedWothLocations = random.sample(wothLocations, min(5, len(wothLocations)))
    wothPriority = random.randint(1, 4)
    for wothLocation in selectedWothLocations:
        suffix = [specificSuffix for specificSuffix in moveSpecificSuffixes if specificSuffix in wothLocation]
        if len(suffix) > 0:
            wothHint = str(wothLocation).removesuffix(suffix[0])
        hint_list.append(
            Hint(hint=f"{wothHint} {ConvertHint(Translations.Generic_IsTheWayOfTheHoard,[])}", important=random.choice([True, True, False]), priority=wothPriority, subtype="way_of_the_hoard")
        )
        wothPriority += random.randint(1, 2)

    # PADDED HINTS
    cb_list = [
        {"kong": Translations.Generic_DK_Long, "color": Translations.Generic_Yellow},
        {"kong": Translations.Generic_Diddy, "color": Translations.Generic_Red},
        {"kong": Translations.Generic_Lanky, "color": Translations.Generic_Blue},
        {"kong": Translations.Generic_Tiny, "color": Translations.Generic_Purple},
        {"kong": Translations.Generic_Chunky, "color": Translations.Generic_Green},
    ]
    # hint_list.append(Hint(hint=f"Your seed is {spoiler.settings.seed}")
    hint_list.append(
        Hint(
            hint=ConvertHint(Translations.Generic_YouCanFindBananasInButOtherLevels, [ConvertHint(level_list[random.randint(0, 6)], [])]),
            important=False,
            subtype="joke",
            joke=True,
            joke_defined=True,  # f"{Translations.Generic_YouCanFindBananasIn} {level_list[random.randint(0,6)]}{Translations.Generic_ButAlsoOtherLevels}"
        )
    )
    cb_hint = random.choice(cb_list)
    hint_list.append(
        Hint(
            hint=ConvertHint(
                Translations.Generic_KongCanFindBananasInLevel, [ConvertHint(cb_hint["kong"], []), ConvertHint(cb_hint["color"], []), ConvertHint(random.choice(level_list), [])]
            ),  # f"{cb_hint['kong']} {Translations.Generic_CanFind} {cb_hint['color']} {Translations.Generic_BananasIn} {random.choice(level_list)}.",
            important=False,
            subtype="joke",
            joke=True,
            joke_defined=True,
        )
    )
    hint_list.append(Hint(hint=f"{spoiler.settings.krool_key_count} {ConvertHint(Translations.Generic_KeysAreRequiredToFightKRool,[])}", important=False, subtype="key_count_required"))

    if spoiler.settings.shuffle_loading_zones == "levels":

        lobby_entrance_order = {
            Transitions.IslesMainToJapesLobby: Levels.JungleJapes,
            Transitions.IslesMainToAztecLobby: Levels.AngryAztec,
            Transitions.IslesMainToFactoryLobby: Levels.FranticFactory,
            Transitions.IslesMainToGalleonLobby: Levels.GloomyGalleon,
            Transitions.IslesMainToForestLobby: Levels.FungiForest,
            Transitions.IslesMainToCavesLobby: Levels.CrystalCaves,
            Transitions.IslesMainToCastleLobby: Levels.CreepyCastle,
        }
        lobby_exit_order = {
            Transitions.IslesJapesLobbyToMain: Levels.JungleJapes,
            Transitions.IslesAztecLobbyToMain: Levels.AngryAztec,
            Transitions.IslesFactoryLobbyToMain: Levels.FranticFactory,
            Transitions.IslesGalleonLobbyToMain: Levels.GloomyGalleon,
            Transitions.IslesForestLobbyToMain: Levels.FungiForest,
            Transitions.IslesCavesLobbyToMain: Levels.CrystalCaves,
            Transitions.IslesCastleLobbyToMain: Levels.CreepyCastle,
        }
        level_positions = {}
        level_order = {}
        shuffled_level_list = []
        for transition, vanilla_level in lobby_entrance_order.items():
            shuffled_level = lobby_exit_order[spoiler.shuffled_exit_data[transition].reverse]
            level_positions[shuffled_level] = vanilla_level
            level_order[vanilla_level] = shuffled_level
    if spoiler.settings.randomize_blocker_required_amounts is True and spoiler.settings.shuffle_loading_zones == "levels":
        for i in list(level_order.values()):
            shuffled_level_list.append(i.name)
        for x in range(8):
            count = spoiler.settings.EntryGBs[x]
            gb_name = Translations.Generic_GBMult
            if count == 1:
                gb_name = Translations.Generic_GBSingular
            level_name = ConvertHint(level_list[x], [])
            # current_level_position = level_positions.index(level_name)
            gb_importance = False
            permitted_levels = all_levels.copy()
            priority_level = x + 1
            if spoiler.settings.shuffle_loading_zones == "levels":
                if x != 7:
                    current_level_order = level_positions[x]
                    permitted_levels = []
                    for y in range(7):
                        if y < current_level_order:
                            permitted_levels.append(level_order[y])
                    if level_name.replace(" ", "") in shuffled_level_list[4:7]:
                        priority_level = 4
                        gb_importance = True
                if spoiler.settings.maximize_helm_blocker is False and x == 7:
                    priority_level = 1
                    gb_importance = True
            if spoiler.settings.wrinkly_hints == "cryptic":
                level_name = random.choice(level_cryptic[x])

            hint_list.append(
                Hint(
                    hint=ConvertHint(Translations.Generic_BLockerHint, [level_name, count, ConvertHint(gb_name, [])]),  # f"The barrier to {level_name} can be cleared by obtaining {count} {gb_name}.",
                    important=gb_importance,
                    priority=priority_level,
                    permitted_levels=permitted_levels.copy(),
                    subtype="gb_amount",
                )
            )
    for x in range(7):
        count = spoiler.settings.BossBananas[x]
        cb_name = Translations.Generic_CBMult
        if count == 1:
            cb_name = Translations.Generic_CBSingular
        if spoiler.settings.wrinkly_hints == "cryptic":
            level_name = random.choice(level_cryptic[x])
        else:
            level_name = level_list[x]
        permitted_levels = all_levels.copy()
        if spoiler.settings.shuffle_loading_zones == "levels":
            current_level_order = level_positions[x]
            permitted_levels = []
            for y in range(7):
                if y <= current_level_order:
                    permitted_levels.append(level_order[y])
        hint_list.append(
            Hint(
                hint=ConvertHint(
                    Translations.Generic_TNSHint, [ConvertHint(level_name, []), count, ConvertHint(cb_name, [])]
                ),  # f"The barrier to the boss in {level_name} can be cleared by obtaining {count} {cb_name}.",
                important=False,
                permitted_levels=permitted_levels.copy(),
                subtype="cb_amount",
            )
        )
    # Write Hints
    hint_distro = {}
    # 1 Joke Hint
    joke_hints = []
    for hint in hint_list:
        if not hint.important and not hint.used and hint.joke:
            joke_hints.append(hint)
    random_joke_hint = random.choice(joke_hints)
    placed = False
    joke_hint_count = 0
    while not placed:
        placed = updateRandomHint(random_joke_hint.hint, random_joke_hint.kongs.copy(), random_joke_hint.keywords.copy(), random_joke_hint.permitted_levels.copy())
        if placed:
            random_joke_hint.use_hint()
            joke_hint_count += 1
            subtype = random_joke_hint.subtype
            if subtype in hint_distro:
                hint_distro[subtype] += 1
            else:
                hint_distro[subtype] = 1
            break
    # Important
    random.shuffle(hint_list)
    priority_level = 1
    no_important_hints = False
    important_hint_count = 0
    while not no_important_hints:
        found_important = False
        for hint in hint_list:
            if hint.important and hint.priority == priority_level and not hint.used and not hint.joke:
                found_important = True
                placed = updateRandomHint(hint.hint, hint.kongs.copy(), hint.keywords.copy(), hint.permitted_levels.copy())
                if placed:
                    hint.use_hint()
                    important_hint_count += 1
                    subtype = hint.subtype
                    if subtype in hint_distro:
                        hint_distro[subtype] += 1
                    else:
                        hint_distro[subtype] = 1
                else:
                    hint.downgrade()
        if not found_important:
            no_important_hints = True
        priority_level += 1
    # Unimportant
    joke_hints = []
    vacant_slots = 0
    for hint in hint_list:
        if not hint.important and not hint.used and not hint.joke:
            joke_hints.append(hint)
    for hint in hints:
        if hint.hint == "":
            vacant_slots += 1
    random.shuffle(joke_hints)
    unimportant_hint_count = 0
    error_hint_count = 0
    if vacant_slots > 0:
        slot = 0
        tries = 100
        usage_slot = 0
        while slot < vacant_slots:
            placed = False
            if not joke_hints[usage_slot].used:
                placed = updateRandomHint(joke_hints[usage_slot].hint, joke_hints[usage_slot].kongs, joke_hints[usage_slot].keywords.copy(), joke_hints[usage_slot].permitted_levels.copy())
            if placed:
                joke_hints[usage_slot].use_hint()
                unimportant_hint_count += 1
                subtype = joke_hints[usage_slot].subtype
                if subtype in hint_distro:
                    hint_distro[subtype] += 1
                else:
                    hint_distro[subtype] = 1
                slot += 1
            else:
                tries -= 1
            usage_slot += 1
            if usage_slot >= len(joke_hints):
                usage_slot = 0
            if tries == 0:
                for hint in hints:
                    if hint.hint == "":
                        hint.hint = ConvertHint(Translations.Generic_ErrorMsg, [])
                        subtype = "error"
                        if subtype in hint_distro:
                            hint_distro[subtype] += 1
                        else:
                            hint_distro[subtype] = 1
                        error_hint_count += 1
                slot = vacant_slots
    print(
        f"Hint Distribution | Important: {important_hint_count}, Unimportant: {unimportant_hint_count}, Jokes: {joke_hint_count}, Errors: {error_hint_count}, Total Good: {important_hint_count + unimportant_hint_count + joke_hint_count}"
    )
    print(f"Hint JSON: {hint_distro}")
    UpdateSpoilerHintList(spoiler)
    return True


def AddLoadingZoneHints(spoiler: Spoiler):
    """Add hints for loading zone transitions and their destinations."""
    # One hint for each of the critical areas: Japes, Aztec, Factory
    criticalJapesRegions = [
        Regions.JungleJapesMain,
        Regions.JapesBeyondFeatherGate,
        Regions.TinyHive,
        Regions.JapesLankyCave,
        Regions.Mine,
    ]
    criticalAztecRegions = [
        Regions.AngryAztecStart,
        Regions.AngryAztecMain,
    ]
    criticalFactoryRegions = [
        Regions.FranticFactoryStart,
        Regions.ChunkyRoomPlatform,
        Regions.PowerHut,
        Regions.BeyondHatch,
        Regions.InsideCore,
    ]
    japesHintEntrances = [entrance for entrance, back in spoiler.shuffled_exit_data.items() if back.regionId in criticalJapesRegions]
    random.shuffle(japesHintEntrances)
    japesHintPlaced = False
    while len(japesHintEntrances) > 0:
        japesHinted = japesHintEntrances.pop()
        if TryAddingLoadingZoneHint(spoiler, japesHinted, 1, criticalJapesRegions):
            japesHintPlaced = True
            break
    if not japesHintPlaced:
        print("Japes LZR hint unable to be placed!")

    aztecHintEntrances = [entrance for entrance, back in spoiler.shuffled_exit_data.items() if back.regionId in criticalAztecRegions]
    random.shuffle(aztecHintEntrances)
    aztecHintPlaced = False
    while len(aztecHintEntrances) > 0:
        aztecHinted = aztecHintEntrances.pop()
        if TryAddingLoadingZoneHint(spoiler, aztecHinted, 1, criticalAztecRegions):
            aztecHintPlaced = True
            break
    if not aztecHintPlaced:
        print("Aztec LZR hint unable to be placed!")

    factoryHintEntrances = [entrance for entrance, back in spoiler.shuffled_exit_data.items() if back.regionId in criticalFactoryRegions]
    random.shuffle(factoryHintEntrances)
    factoryHintPlaced = False
    while len(factoryHintEntrances) > 0:
        factoryHinted = factoryHintEntrances.pop()
        if TryAddingLoadingZoneHint(spoiler, factoryHinted, 1, criticalFactoryRegions):
            factoryHintPlaced = True
            break
    if not factoryHintPlaced:
        print("Factory LZR hint unable to be placed!")

    # Three hints for any of these useful areas: Banana Fairy, Galleon, Fungi, Caves, Castle, Crypt, Tunnel
    usefulRegions = [
        [Regions.BananaFairyRoom],
        [
            Regions.GloomyGalleonStart,
            Regions.LighthouseArea,
            Regions.Shipyard,
        ],
        [
            Regions.FungiForestStart,
            Regions.GiantMushroomArea,
            Regions.MushroomLowerExterior,
            Regions.MushroomNightExterior,
            Regions.MushroomUpperExterior,
            Regions.MillArea,
        ],
        [
            Regions.CrystalCavesMain,
            Regions.IglooArea,
            Regions.CabinArea,
        ],
        [
            Regions.CreepyCastleMain,
            Regions.CastleWaterfall,
        ],
        [Regions.LowerCave],
        [Regions.UpperCave],
    ]
    hintedUsefulAreas = random.sample(usefulRegions, 3)
    for regions in hintedUsefulAreas:
        usefulHintEntrances = [entrance for entrance, back in spoiler.shuffled_exit_data.items() if back.regionId in regions]
        random.shuffle(usefulHintEntrances)
        usefulHintPlaced = False
        while len(usefulHintEntrances) > 0:
            usefulHinted = usefulHintEntrances.pop()
            if TryAddingLoadingZoneHint(spoiler, usefulHinted, 3, regions):
                usefulHintPlaced = True
                break
        if not usefulHintPlaced:
            print(f"Useful LZR hint to {usefulHinted.name} unable to be placed!")

    # Remaining hints for any shuffled exits in the game
    # Restrict DK isles main areas from being hinted
    uselessDkIslesRegions = [
        Regions.IslesMain,
        Regions.IslesMainUpper,
    ]
    remainingTransitions = [entrance for entrance, back in spoiler.shuffled_exit_data.items() if back.regionId not in uselessDkIslesRegions]
    random.shuffle(remainingTransitions)
    remainingHintCount = 4
    for transition in remainingTransitions:
        if remainingHintCount == 0:
            break
        elif TryAddingLoadingZoneHint(spoiler, transition, 5):
            remainingHintCount -= 1
    if remainingHintCount > 0:
        print("Unable to place remaining LZR hints!")


def TryAddingLoadingZoneHint(spoiler: Spoiler, transition, useful_rating, disallowedRegions: list = None):
    """Try to write a hint for the given transition. If this hint is determined to be bad, it will return false and not place the hint."""
    if disallowedRegions is None:
        disallowedRegions = []
    pathToHint = transition
    # Don't hint entrances from dead-end rooms, follow the reverse pathway back until finding a place with multiple entrances
    if spoiler.settings.decoupled_loading_zones:
        while ShufflableExits[pathToHint].category is None:
            originPaths = [x for x, back in spoiler.shuffled_exit_data.items() if back.reverse == pathToHint]
            # In a few cases, there is no reverse loading zone. In this case we must keep the original path to hint
            if len(originPaths) == 0:
                break
            pathToHint = originPaths[0]
    # With coupled loading zones, never hint from a dead-end room, since it is forced to be coming from the same destination
    elif ShufflableExits[pathToHint].category is None:
        return False
    # Validate the region of the hinted entrance is not in disallowedRegions
    if ShufflableExits[pathToHint].region in disallowedRegions:
        return False
    # Validate the hinted destination is not the same as the hinted origin
    entranceMap = GetMapId(ShufflableExits[pathToHint].region)
    destinationMap = GetMapId(spoiler.shuffled_exit_data[transition].regionId)
    if entranceMap == destinationMap:
        return False
    entranceName = ShufflableExits[pathToHint].name
    destinationName: str = spoiler.shuffled_exit_data[transition].spoilerName
    fromExitName = destinationName.find(" from ")
    if fromExitName != -1:
        # Remove exit name from destination
        destinationName = destinationName[:fromExitName]
    pushHintToList(Hint(hint=ConvertHint(Translations.Generic_LZRHint, [destinationName, entranceName]), priority=useful_rating, subtype="lzr"))
    return True


def UpdateSpoilerHintList(spoiler: Spoiler):
    """Write hints to spoiler object."""
    for hint in hints:
        if hint.kong != Kongs.any:
            spoiler.hint_list[hint.name] = hint.hint
