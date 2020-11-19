from fuzzywuzzy import fuzz
import re
import requests
import sys
from typing import List, Tuple


def fuzzy_match(s: str, options: List[str]) -> List[str]:
    matches = []
    for opt in options:
        score = fuzz.ratio(s, opt)
        matches.append((opt, score))
    return sorted(matches, key=lambda match: match[1], reverse=True)[:3]


def print_fuzzy_matches(fuzzy_matches: List[Tuple[str, int]]) -> None:
    # for fm in [f for f in fuzzy_matches if f[1] >= 80]:
    for fm in fuzzy_matches:
        print(f"    - { fm[0] } ({ fm[1] })")


emoji_re = r':([a-z0-9_]*):'
r = requests.get("https://api.github.com/emojis")
vld_emoji = list(r.json().keys())


# sys.argv[1] is the temp file with the commit message
commit_msg = open(sys.argv[1]).read().strip()


matches = re.findall(emoji_re, commit_msg)
if len(matches) > 0:
    for emoji in matches:
        if emoji not in vld_emoji:
            
            fuzzy_matches = fuzzy_match(emoji, vld_emoji)
            print(f":{ emoji }: is not valid.")
            if len(fuzzy_matches) > 0:
                print_fuzzy_matches(fuzzy_matches)


sys.exit(0)
