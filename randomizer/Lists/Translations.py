"""Stores the translation data for each hint."""

from randomizer.Enums.Languages import Languages
from randomizer.Enums.Translations import Translations
from randomizer.Spoiler import Spoiler

TranslationInfo = {"language_name": Languages.English}


def setLanguage(language_name: Languages):
    """Set Language used by translation element."""
    TranslationInfo["language_name"] = language_name


TranslationDB = {
    Translations.Wrinkly_DKInDK64: {
        Languages.English: ["Did you know - Donkey Kong officially features in Donkey Kong 64."],
        Languages.FrenchCA: ["Saviez-vous que - Donkey Kong joue officiellement un role dans Donkey Kong 64."],
    },
    Translations.Wrinkly_FungiBK: {
        Languages.English: ["Fungi Forest was originally intended to be in the other N64 Rareware title, Banjo Kazooie."],
        Languages.FrenchCA: ["Fungi Forest etait initialement prevu d'etre dans un autre titre de Rareware sur le N64, Banjo-Kazooie."],
    },
    Translations.Wrinkly_TrapBubble: {
        Languages.English: ["Holding up-left when trapped inside of a trap bubble will break you out of it without spinning your stick."],
        Languages.FrenchCA: ["Tenir haut-gauche quand vous etes pris dans une bulle piegee va vous sortir de la sans virer le joystick."],
    },
    Translations.Wrinkly_TinyDixie: {
        Languages.English: ["Tiny Kong is the youngest sister of Dixie Kong."],
        Languages.FrenchCA: ["Tiny Kong est la petite soeur de Dixie Kong."],
    },
    Translations.Wrinkly_Mornin: {
        Languages.English: ["Mornin."],
        Languages.FrenchCA: ["Mornin."],
    },
    Translations.Wrinkly_LankyRelatives: {
        Languages.English: ["Lanky Kong is the only kong with no canonical relation to the main Kong family tree."],
        Languages.FrenchCA: ["Lanky Kong est, canoniquement, le seul kong qui n'a aucune relation avec la branche principale genealogique des Kong."],
    },
    Translations.Wrinkly_ChunkyJump: {
        Languages.English: ["Despite the line in the DK Rap stating otherwise, Chunky is the kong who can jump highest in DK64."],
        Languages.FrenchCA: ["Malgre ce que le DK Rap mentionne, Chunky est le kong qui saute le plus haut dans DK64"],
    },
    Translations.Wrinkly_TinySlow: {
        Languages.English: ["Despite the line in the DK Rap stating otherwise, Tiny is one of the two slowest kongs in DK64."],
        Languages.FrenchCA: ["Malgre ce que le DK Rap mentionne, Tiny est une des deux kong les plus lents."],
    },
    Translations.Wrinkly_CandyJapesFungi: {
        Languages.English: ["Candy Kong does not appear in Jungle Japes or Fungi Forest."],
        Languages.FrenchCA: ["Candy Kong n'apparait pas dans Jungle Japes ou Fungi Forest."],
    },
    Translations.Wrinkly_KRoolVictorious: {
        Languages.English: ["If you fail the twelfth round of K. Rool, the game will dictate that K. Rool is victorious and end the fight."],
        Languages.FrenchCA: ["Si vous echouez la 12e ronde de K.Rool, le jeu va declarer K.Rool comme le vainqueur et terminer le combat."],
    },
    Translations.Wrinkly_DK64RandoOrigins: {
        Languages.English: ["Donkey Kong 64 Randomizer started as a LUA Script in early 2019, evolving into a ROM Hack in 2021."],
        Languages.FrenchCA: ["Donkey Kong 64 Randomizer a commence comme un script LUA au debut de 2019 en evoluant en hack de ROM en 2021."],
    },
    Translations.Wrinkly_VanillaIGTMax: {
        Languages.English: ["The maximum in-game time that the vanilla file screen time can display is 1165 hours and 5 minutes."],
        Languages.FrenchCA: ["Le temps maximum que le jeu original peut afficher a la selection de fichier est de 1165 heures et 5 minutes."],
    },
    Translations.Wrinkly_ChunkyKiddy: {
        Languages.English: ["Chunky Kong is the brother of Kiddy Kong."],
        Languages.FrenchCA: ["Chunky Kong est le frere de Kiddy Kong."],
    },
    Translations.Wrinkly_FungiMushJoke: {
        Languages.English: ["Fungi Forest contains mushrooms."],
        Languages.FrenchCA: ["Fungi Forest contient des champignons."],
    },
    Translations.Wrinkly_CavesIglooJoke: {
        Languages.English: ["Igloos can be found in Crystal Caves."],
        Languages.FrenchCA: ["On peut trouver des igloos dans Crystal Caves."],
    },
    Translations.Wrinkly_FactoryFloors: {
        Languages.English: ["Frantic Factory has multiple floors where things can be found."],
        Languages.FrenchCA: ["Frantic Factory a plusieurs etages ou ce que l'on peut trouver des affaires."],
    },
    Translations.Wrinkly_AztecSandstorm: {
        Languages.English: ["Angry Aztec has so much sand, it's even in the wind."],
        Languages.FrenchCA: ["Angry Aztec a tellement de sable qu'il en a dans le vent."],
    },
    Translations.Wrinkly_IslesNoKey: {
        Languages.English: ["DK Isles does not have a key."],
        Languages.FrenchCA: ["L'ile DK Isles n'a pas de cle."],
    },
    Translations.Wrinkly_RabbitJoke: {
        Languages.English: ["You can find a rabbit in Fungi Forest and in Crystal Caves."],
        Languages.FrenchCA: ["Vous pouvez trouver un lapin dans Fungi Forest et dans Crystal Caves."],
    },
    Translations.Wrinkly_BeetleJoke: {
        Languages.English: ["You can find a beetle in Angry Aztec and in Crystal Caves."],
        Languages.FrenchCA: ["Vous pouvez trouver une coccinelle dans Angry Aztec et dans Crystal Caves."],
    },
    Translations.Wrinkly_VultureJoke: {
        Languages.English: ["You can find a vulture in Angry Aztec."],
        Languages.FrenchCA: ["Vous pouvez trouver un vautour dans Angry Aztec."],
    },
    Translations.Wrinkly_OwlJoke: {
        Languages.English: ["You can find an owl in Fungi Forest."],
        Languages.FrenchCA: ["Vous pouvez trouver un hibou dans Fungi Forest."],
    },
    Translations.Wrinkly_CoinsBuyMoves: {
        Languages.English: ["To buy moves, you will need coins."],
        Languages.FrenchCA: ["Pour acheter les abilites, vous avez besoin de pieces"],
    },
    Translations.Wrinkly_SoundToggle: {
        Languages.English: ["You can change the music and sound effects volume in the sound settings on the main menu."],
        Languages.FrenchCA: ["Vous pouvez changer le volume de la musique et des effets sonores dans le menu Sound Settings dans le menu principal."],
    },
    Translations.Wrinkly_CoinHoard: {
        Languages.English: ["Coin Hoard is a Monkey Smash game mode where players compete to collect the most coins."],
        Languages.FrenchCA: ["Coin Hoard est un mode de Monkey Smash ou les joueurs competitionnent pour ramasser le plus de pieces."],
    },
    Translations.Wrinkly_CapturePad: {
        Languages.English: ["Capture Pad is a Monkey Smash game mode where players attempt to capture pads in different corners of the arena."],
        Languages.FrenchCA: ["Capture Pad est un mode de Monkey Smash ou les joueurs essaient de capturer des capsules dans differents coins de l'arene."],
    },
    Translations.Wrinkly_NothingToSay: {
        Languages.English: ["I have nothing to say to you."],
        Languages.FrenchCA: ["J'ai rien a t'dire."],
    },
    Translations.Wrinkly_ForgotHint: {
        Languages.English: ["I had something to tell you, but I forgot what it is."],
        Languages.FrenchCA: ["J'avais kek'chose a t'dire, mais j'ai oublie c'que c'etait."],
    },
    Translations.Wrinkly_IDontKnow: {
        Languages.English: ["I don't know anything."],
        Languages.FrenchCA: ["J'che rien."],
    },
    Translations.Wrinkly_Lost: {
        Languages.English: ["I'm as lost as you are. Good luck!"],
        Languages.FrenchCA: ["Chu aussi perdu que t'toi. Bonne chance!"],
    },
    Translations.Wrinkly_NeverHeardOfHim: {
        Languages.English: ["Wrinkly? Never heard of him."],
        Languages.FrenchCA: ["Wrinkly? Jamais entendu parler d'lui."],
    },
    Translations.Wrinkly_PeakOfRandomizers: {
        Languages.English: [
            "This is it. The peak of all randomizers. No other randomizer exists besides DK64 Randomizer where you can listen to the dk rap in its natural habitat while freeing Chunky Kong in Jungle Japes."
        ],
        Languages.FrenchCA: [
            "Ca y est. C'est le top du top des randomizers. Aucun autre randomizer autre que DK64 Randomizer ou vous pouvez ecouter le DK Rap dans son habitant naturel tout en liberant Chunky Kong dans Jungle Japes."
        ],
    },
    Translations.Wrinkly_TranslatorCredit: {
        Languages.English: ["Translations done by no-one. This is English."],  # If not english, translation is "Translated into {language} by {author}"
        Languages.FrenchCA: ["Traduit en bon francais quebecois par Lebon14."],
    },
    Translations.Wrinkly_NoAccents: {
        Languages.English: [
            "Accents? There is only 1 accent here - Wrinkly's English."  # If language doesn't contain accents or special characters, translation is "{author} told me to tell you that {pronoun} had to remove the accents for technical reasons."
        ],
        Languages.FrenchCA: ["Lebon14 m'a dit de te dire qu'il a ete oblige d'enelever les accents pour des raisons techniques."],
    },
    Translations.Wrinkly_YashichiOven: {
        Languages.English: ["Why do they call it oven when you of in the cold food of out hot eat the food?"],
        Languages.FrenchCA: ["Pourquoi qui l'appelle un poele quand toi de la bouffe froide de n'a pu de bouffe chaude a manger?"],
    },
    Translations.Wrinkly_WannaBecomeFamous: {
        Languages.English: ["Wanna become famous? Buy followers, coconuts and donks at DK64Randomizer (DK64Randomizer . com)!"],
        Languages.FrenchCA: ["Veux-tu devenir une star? Achete des suiveurs, des noix et des donks a DK64Randomizer (DK64Randomizer . com)!"],
    },
    Translations.Wrinkly_SpikeVegeta: {
        Languages.English: ["What you gonna do, SpikeVegeta?"],
        Languages.FrenchCA: ["Qu'est-ce 'tu va faire, SpikeVegeta?"],
    },
    Translations.Generic_DK_Long: {
        Languages.English: ["Donkey"],
        Languages.FrenchCA: ["Donkey"],
    },
    Translations.Generic_DK_Short: {
        Languages.English: ["DK"],
        Languages.FrenchCA: ["DK"],
    },
    Translations.Generic_Diddy: {
        Languages.English: ["Diddy"],
        Languages.FrenchCA: ["Diddy"],
    },
    Translations.Generic_Lanky: {
        Languages.English: ["Lanky"],
        Languages.FrenchCA: ["Lanky"],
    },
    Translations.Generic_Tiny: {
        Languages.English: ["Tiny"],
        Languages.FrenchCA: ["Tiny"],
    },
    Translations.Generic_Chunky: {
        Languages.English: ["Chunky"],
        Languages.FrenchCA: ["Chunky"],
    },
    Translations.Cryptic_DK_Faster: {
        Languages.English: ["The kong who is bigger, faster and potentially stronger too"],
        Languages.FrenchCA: ["Le kong qui est potentiellement plus gros, plus rapide et plus puissant"],
    },
    Translations.Cryptic_DK_Spurts: {
        Languages.English: ["The kong who fires in spurts"],
        Languages.FrenchCA: ["Le kong qui fait feu en crachats"],
    },
    Translations.Cryptic_DK_Tie: {
        Languages.English: ["The kong with a tie"],
        Languages.FrenchCA: ["Le kong avec une cravate"],
    },
    Translations.Cryptic_DK_Bongos: {
        Languages.English: ["The kong who slaps their instrument to the jungle beat"],
        Languages.FrenchCA: ["Le kong qui tappe son instrument au rhythme de la jungle"],
    },
    Translations.Misc_KRoolOrderIs: {
        Languages.English: ["K. Rool order is"],
        Languages.FrenchCA: ["L'ordre K. Rool est"],
    },
    Translations.Generic_Then: {
        Languages.English: ["then"],
        Languages.FrenchCA: ["ensuite"],
    },
    Translations.Cryptic_Diddy_Fly: {
        Languages.English: ["The kong who can fly real high"],
        Languages.FrenchCA: ["Le kong qui peut voler vraiment haut"],
    },
    Translations.Cryptic_Diddy_DKC: {
        Languages.English: ["The kong who features in the first two Donkey Kong Country games"],
        Languages.FrenchCA: ["Le kong qui a un role dans les 2 premiers Donkey Kong Country"],
    },
    Translations.Cryptic_Diddy_Red: {
        Languages.English: ["The kong who wants to see red"],
        Languages.FrenchCA: ["Le kong qui veut voir rouge"],
    },
    Translations.Cryptic_Diddy_FreeTiny: {
        Languages.English: ["The kong who frees the only female playable kong"],
        Languages.FrenchCA: ["Le kong qui libere le seul kong feminin jouable"],
    },
    Translations.Cryptic_Lanky_Balloon: {
        Languages.English: ["The kong who inflates like a balloon, just like a balloon"],
        Languages.FrenchCA: ["Le kong qui gonfle comme un ballon, comme une balloune"],
    },
    Translations.Cryptic_Lanky_Overalls: {
        Languages.English: ["The kong who waddles in his overalls"],
        Languages.FrenchCA: ["Le kong qui se dandine dans sa salopette"],
    },
    Translations.Cryptic_Lanky_Beetle: {
        Languages.English: ["The kong who has a cold race with an insect"],
        Languages.FrenchCA: ["Le kong qui a une course au froid avec un insecte"],
    },
    Translations.Cryptic_Lanky_Style: {
        Languages.English: ["The kong who lacks style, grace but not a funny face"],
        Languages.FrenchCA: ["Le kong qui manque de style et de grace mais une drole de face"],
    },
    Translations.Cryptic_Tiny_Jazz: {
        Languages.English: ["The kong who likes jazz"],
        Languages.FrenchCA: ["Le kong qui aime le jazz"],
    },
    Translations.Cryptic_Tiny_Toes: {
        Languages.English: ["The kong who shoots K. Rool's tiny toes"],
        Languages.FrenchCA: ["Le kong qui tire les petits orteuils de K. Rool"],
    },
    Translations.Cryptic_Tiny_Feather: {
        Languages.English: ["The kong who has ammo that is light as a feather"],
        Languages.FrenchCA: ["Le kong qui a des munitions aussi leger que des plumes"],
    },
    Translations.Cryptic_Tiny_Shrink: {
        Languages.English: ["The kong who can shrink in size"],
        Languages.FrenchCA: ["Le kong qui peut devenir tout petit"],
    },
    Translations.Cryptic_Chunky_HellOfAGuy: {
        Languages.English: ["The kong who is one hell of a guy"],
        Languages.FrenchCA: ["Le kong qui est toute qu'un gars"],
    },
    Translations.Cryptic_Chunky_Boulders: {
        Languages.English: ["The kong who can pick up boulders"],
        Languages.FrenchCA: ["Le kong qui peut soulever des roches"],
    },
    Translations.Cryptic_Chunky_ToyMonster: {
        Languages.English: ["The kong who fights a blocky boss"],
        Languages.FrenchCA: ["Le kong qui se bat contre des blocs numerotes"],
    },
    Translations.Cryptic_Chunky_DogadonBow: {
        Languages.English: ["The kong who bows down to a dragonfly"],
        Languages.FrenchCA: ["Le kong qui s'ajenoue a une libellule"],
    },
    Translations.Generic_Japes: {
        Languages.English: ["Jungle Japes"],
        Languages.FrenchCA: ["Jungle Japes"],
    },
    Translations.Generic_Aztec: {
        Languages.English: ["Angry Aztec"],
        Languages.FrenchCA: ["Angry Aztec"],
    },
    Translations.Generic_Factory: {
        Languages.English: ["Frantic Factory"],
        Languages.FrenchCA: ["Frantic Factory"],
    },
    Translations.Generic_Galleon: {
        Languages.English: ["Gloomy Galleon"],
        Languages.FrenchCA: ["Gloomy Galleon"],
    },
    Translations.Generic_Fungi: {
        Languages.English: ["Fungi Forest"],
        Languages.FrenchCA: ["Fungi Forest"],
    },
    Translations.Generic_Caves: {
        Languages.English: ["Crystal Caves"],
        Languages.FrenchCA: ["Crystal Caves"],
    },
    Translations.Generic_Castle: {
        Languages.English: ["Creepy Castle"],
        Languages.FrenchCA: ["Creepy Castle"],
    },
    Translations.Generic_Helm: {
        Languages.English: ["Hideout Helm"],
        Languages.FrenchCA: ["Hideout Helm"],
    },
    Translations.Generic_Isles: {
        Languages.English: ["DK Isles"],
        Languages.FrenchCA: ["DK Isles"],
    },
    Translations.Cryptic_Japes_Storm: {
        Languages.English: ["The level with a localized storm"],
        Languages.FrenchCA: ["Le niveau avec un orage localise"],
    },
    Translations.Cryptic_Japes_Mountain: {
        Languages.English: ["The level with a dirt mountain"],
        Languages.FrenchCA: ["Le niveau avec une montagne de terre"],
    },
    Translations.Cryptic_Japes_Retailers: {
        Languages.English: ["The level which has two retailers and no race"],
        Languages.FrenchCA: ["Le niveau qui a deux detaillants mais pas de course"],
    },
    Translations.Cryptic_Aztec_Vases: {
        Languages.English: ["The level with four vases"],
        Languages.FrenchCA: ["Le niveau aux quatre vases"],
    },
    Translations.Cryptic_Aztec_Cages: {
        Languages.English: ["The level with two kongs cages"],
        Languages.FrenchCA: ["Le niveau avec deux cages Kong"],
    },
    Translations.Cryptic_Aztec_Totem: {
        Languages.English: ["The level with a spinning totem"],
        Languages.FrenchCA: ["Le niveau avec un totem qui tourne"],
    },
    Translations.Cryptic_Factory_ToyProduction: {
        Languages.English: ["The level with a toy production facility"],
        Languages.FrenchCA: ["Le niveau avec une usine de production de jouets"],
    },
    Translations.Cryptic_Factory_BlockTower: {
        Languages.English: ["The level with a tower of blocks"],
        Languages.FrenchCA: ["Le niveau avec une tour de blocs"],
    },
    Translations.Cryptic_Factory_ArcadeYear: {
        Languages.English: ["The level with a game from 1981"],
        Languages.FrenchCA: ["Le niveau avec un jeu de 1981"],
    },
    Translations.Cryptic_Factory_ArcadeCost: {
        Languages.English: ["The level where you need two quarters to play"],
        Languages.FrenchCA: ["Le niveau ou vous avez besoin de deux pieces pour jouer"],
    },
    Translations.Cryptic_Galleon_Water: {
        Languages.English: ["The level with the most water"],
        Languages.FrenchCA: ["Le niveau avec le plus d'eau"],
    },
    Translations.Cryptic_Galleon_Seal: {
        Languages.English: ["The level where you free a water dweller"],
        Languages.FrenchCA: ["Le niveau ou vous devez liberer une creature sousmarine"],
    },
    Translations.Cryptic_Galleon_GoldTower: {
        Languages.English: ["The level with stacks of gold"],
        Languages.FrenchCA: ["Le niveau avec une montagne d'or"],
    },
    Translations.Cryptic_Fungi_Retailers: {
        Languages.English: ["The level with only two retailers and two races"],
        Languages.FrenchCA: ["Le niveau avec deux detaillants et deux courses"],
    },
    Translations.Cryptic_Fungi_Night: {
        Languages.English: ["The level where night can be acquired at will"],
        Languages.FrenchCA: ["Le niveau ou la nuit peut etre acquise a volonte"],
    },
    Translations.Cryptic_Fungi_Owl: {
        Languages.English: ["The level with a nocturnal tree dweller"],
        Languages.FrenchCA: ["Le niveau avec une creature d'un arbre nocturne"],
    },
    Translations.Cryptic_Caves_Water: {
        Languages.English: ["The level with two inches of water"],
        Languages.FrenchCA: ["Le niveau avec deux pouces d'eau"],
    },
    Translations.Cryptic_Caves_IceShield: {
        Languages.English: ["The level with two ice shields"],
        Languages.FrenchCA: ["Le niveau avec deux boucliers de glace"],
    },
    Translations.Cryptic_Caves_IceTomato: {
        Languages.English: ["The level with an Ice Tomato"],
        Languages.FrenchCA: ["Le niveau avec une Tomate de Glace"],
    },
    Translations.Cryptic_Castle_Battlements: {
        Languages.English: ["The level with battlements"],
        Languages.FrenchCA: ["Le niveau a creneaux"],
    },
    Translations.Cryptic_Castle_IntFeatures: {
        Languages.English: ["The level with a dungeon, ballroom and a library"],
        Languages.FrenchCA: ["Le niveau avec un dongeon, une salle de bal et une bibliotheque"],
    },
    Translations.Cryptic_Castle_ExtFeatures: {
        Languages.English: ["The level with drawbridge and a moat"],
        Languages.FrenchCA: ["Le niveau avec un pont-levis et des douves"],
    },
    Translations.Cryptic_Helm_Timer: {
        Languages.English: ["The timed level"],
        Languages.FrenchCA: ["Le niveau chronometre"],
    },
    Translations.Cryptic_Helm_Boss: {
        Languages.English: ["The level with no boss"],
        Languages.FrenchCA: ["Le niveua sans boss"],
    },
    Translations.Cryptic_Helm_CB: {
        Languages.English: ["The level with no small bananas"],
        Languages.FrenchCA: ["Le niveau sans petites bananes"],
    },
    Translations.Cryptic_Isles_Hub: {
        Languages.English: ["The hub world"],
        Languages.FrenchCA: ["Le monde central"],
    },
    Translations.Cryptic_Isles_Face: {
        Languages.English: ["The world with DK's ugly mug on it"],
        Languages.FrenchCA: ["Le monde avec la face laite de DK dessus"],
    },
    Translations.Cryptic_Isles_Shops: {
        Languages.English: ["The world with only a Cranky's Lab and Snide's HQ in it"],
        Languages.FrenchCA: ["Le monde avec seulement le lab de Cranky et l'HQ de Snide dedans"],
    },
    Translations.Generic_Cranky: {
        Languages.English: ["Cranky"],
        Languages.FrenchCA: ["Cranky"],
    },
    Translations.Generic_Candy: {
        Languages.English: ["Candy"],
        Languages.FrenchCA: ["Candy"],
    },
    Translations.Generic_Funky: {
        Languages.English: ["Funky"],
        Languages.FrenchCA: ["Funky"],
    },
    Translations.Generic_PersonalIn: {
        Languages.English: ["'s in "],
        Languages.FrenchCA: [" est en "],
    },
    Translations.Generic_And: {
        Languages.English: ["and"],
        Languages.FrenchCA: ["et"],
    },
    Translations.Generic_Contains: {
        Languages.English: ["contains"],
        Languages.FrenchCA: ["contient"],
    },
    Translations.Generic_CanBePurchasedFrom: {
        Languages.English: ["Can be purchased from"],
        Languages.FrenchCA: ["Peuvent etre achetes chez"],
    },
    Translations.Generic_In: {
        Languages.English: ["In"],
        Languages.FrenchCA: ["dans"],
    },
    Translations.Generic_CanBeFoundIn: {
        Languages.English: ["Can be found in"],
        Languages.FrenchCA: ["peut etre trouve dans"],
    },
    Translations.Generic_Patch: {
        Languages.English: ["Patch"],
        Languages.FrenchCA: ["patch"],
    },
    Translations.Generic_Patches: {
        Languages.English: ["Patches"],
        Languages.FrenchCA: ["patchs"],
    },
    Translations.Generic_Is: {
        Languages.English: ["Is"],
        Languages.FrenchCA: ["a"],
    },
    Translations.Generic_Are: {
        Languages.English: ["Are"],
        Languages.FrenchCA: ["a"],
    },
    Translations.Generic_There: {
        Languages.English: ["There"],
        Languages.FrenchCA: ["Il y"],
    },
    Translations.Generic_ThereIsADirtPatchLocatedAt: {
        Languages.English: ["There is a dirt patch located at"],
        Languages.FrenchCA: ["Il y a une patch de terre situe dans"],
    },
    Translations.Generic_PermadeathCurse: {
        Languages.English: ["The curse can only be removed upon disabling K. Rools machine."],
        Languages.FrenchCA: ["La malediction peut seulement etre levee en desactivant la machine de K. Rool."],
    },
    Translations.Generic_MedalsRequiredJetpac: {
        Languages.English: ["medals are required to access Jetpac."],
        Languages.FrenchCA: ["medailles sont requises pour jouer a Jetpac."],
    },
    Translations.Generic_GreatestFoe: {
        Languages.English: ["You will need to obtain the key from ", "~", " to fight your greatest foe."],
        Languages.FrenchCA: ["Vous devez obtenir une cle de ", "~", " pour pouvoir affronter votre plus grand adversaire."],
    },
    Translations.Generic_IsTheWayOfTheHoard: {
        Languages.English: ["is on the Way of the Hoard."],
        Languages.FrenchCA: ["est sur le chemin de la Reserve de Bananes."],
    },
    Translations.Generic_YouCanFindBananasInButOtherLevels: {
        Languages.English: ["You can find bananas in ", "~", ", but also in other levels"],
        Languages.FrenchCA: ["Vous pouvez trouver des bananes dans ", "~", ", mais aussi dans d'autres niveaux."],
    },
    Translations.Generic_Yellow: {
        Languages.English: ["Yellow"],
        Languages.FrenchCA: ["Jaune"],
    },
    Translations.Generic_Red: {
        Languages.English: ["Red"],
        Languages.FrenchCA: ["Rouge"],
    },
    Translations.Generic_Blue: {
        Languages.English: ["Blue"],
        Languages.FrenchCA: ["Bleu"],
    },
    Translations.Generic_Purple: {
        Languages.English: ["Purple"],
        Languages.FrenchCA: ["Violet"],
    },
    Translations.Generic_Green: {
        Languages.English: ["Green"],
        Languages.FrenchCA: ["Vert"],
    },
    Translations.Generic_KongCanFindBananasInLevel: {
        Languages.English: ["~", " can find ", "~", " bananas in ", "~"],
        Languages.FrenchCA: ["~", " peut trouver des bananes ", "~", " dans ", "~"],
    },
    Translations.Generic_KeysAreRequiredToFightKRool: {
        Languages.English: ["Keys are required to reach K. Rool."],
        Languages.FrenchCA: ["cles sont requises pour atteindre K. Rool."],
    },
    Translations.Generic_GBSingular: {
        Languages.English: ["Golden Banana"],
        Languages.FrenchCA: ["banane doree"],
    },
    Translations.Generic_GBMult: {
        Languages.English: ["Golden Bananas"],
        Languages.FrenchCA: ["bananes dorees"],
    },
    Translations.Generic_BLockerHint: {
        Languages.English: ["The barrier to ", "~", " can be cleared by obtaining ", "~", " ", "~", "."],
        Languages.FrenchCA: ["La barriere vers ", "~", " peut etre leve en obtenant ", "~", " ", "~", "."],
    },
    Translations.Generic_CBSingular: {
        Languages.English: ["Small Banana"],
        Languages.FrenchCA: ["petite banane"],
    },
    Translations.Generic_CBMult: {
        Languages.English: ["Small Bananas"],
        Languages.FrenchCA: ["petites bananes"],
    },
    Translations.Generic_TNSHint: {
        Languages.English: ["The barrier to the boss in ", "~", " can be cleared by obtaining ", "~", " ", "~", "."],
        Languages.FrenchCA: ["La barriere vers le boss dans ", "~", " peut etre leve en obtenant ", "~", " ", "~", "."],
    },
    Translations.Generic_ErrorMsg: {
        Languages.English: [
            "I have so little to tell you that this hint got placed here. If you see this, please report with your spoiler log in the bug reports channel in the DK64 Randomizer discord."
        ],  # If not english, state that the server language is English
        Languages.FrenchCA: [
            "J'ai tellement rien a te dire que cette indice a ete placee ici. Si vous voyez ceci, reportez cette erreur, avec votre spoiler log, dans les canaux de signalement de bugs dans le DK64 Randomizer discord. Notez que vous aller a avoir a parler en anglais."
        ],
    },
    Translations.Generic_LZRHint: {
        Languages.English: ["If you're looking for ", "~", ", follow the path from ", "~", "."],
        Languages.FrenchCA: ["Si vous cherchez ", "~", ", suivez le chemin depuis ", "~", "."],
    },
    Translations.Generic_AnEmptyCage: {
        Languages.English: ["An Empty Cage"],
        Languages.FrenchCA: ["Une cage vide"],
    },
}
