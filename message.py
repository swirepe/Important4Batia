
from random import choice
from clint.textui import indent, puts


addons = ["I got this for you!",
    "Did you hear about this?",
    "omgbatia",
    "look look",
    "this made me think of batia",
    ";D",
    "BATIA",
    "what does this mean?",
    "-->",
    "batia, look!",
    "look at this, batia!",
    "@snatiabir @snatiabir",
    "#wisdom",
    "heads up",
    "",
    "here!",
    "what is this?",
    "look batia",
    "omgomgomg",
    "is this the real life?",
    "is this just fantasy?",
    "did you hear?",
    "batiabatia",
    "!!",
    "!!!!!!!",
    "so cool!",
    "gucci gucci",
    "why you looking bitter?",
    "why you looking batia?",
    "help",
    "tl;dr ->",
    "0_0",
    "woah check this",
    "duuuuude",
    "batia hey look",
    "hey look at this",
    "look",
    "look look look",
    "ATTN:",
    "i think u need 2 see ths",
    "$$$$",
    "#batia",
    "important!",
    "this reminded me of you",
    "could have said this",
    "what is",
    "lol",
    "u mad, bro?",
    "u r the best!",
    "<3",
    "<3<3<3",
    "WHY",
    "*~^batia^~*",
    "ZERG RUSH",
    "#word",
    "ummmmmm",
    "...",
    "#realchalk",
    "#want",
    "#batianewsnetwork",
    "#CRUNK",
    "#KreayshawnEchoChamber",
    "dude look",
    "look at THAT",
    "so wise!",
    "so brave!",
    "so fresh!",
    "so $$$!",
    "#linguistics",
    "#truelove",
    "look!!",
    "read this plz",
    "ugh",
    "really?",
    "exciting!",
    "exciting news!"]

addons = [u"@snatiabir " + unicode(a) + u" RT @KREAYSHAWN: " for a in addons]


def compose_message(kre_text, tries=100):
    front = choice(addons)
    attempt = 0
    while len(front + kre_text) > 140 and attempt < tries:
        front = choice(addons)
        attempt += 1

    if attempt < tries:
        with indent(3):
            puts(front.encode("utf-8") + kre_text.encode("utf-8"))
        return front + kre_text
    else:
        with indent(3):
            puts(kre_text.encode("utf-8"))
        return kre_text