
UPPERCASE = ["A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
VOWELS = ["a", "e", "i", "o", "u"]
CONSONANT = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
             "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "z"]
PRONOUNS = {
    "i": {
        "person": "1st",
        "number": "singular",
        "be verb": "am",
        "type": "person.1st.singular",
        "objective": "me",
        "possessive": "my"
    },
    "we": {
        "person": "1st",
        "number": "plural",
        "be verb": "are",
        "type": "person.1st.plural",
        "objective": "us",
        "possessive": "our"
    },
    "you": {
        "person": "2nd",
        "number": "both",
        "be verb": "are",
        "type": "person.2nd.plural",
        "objective": "you",
        "possessive": "your"
    },
    "he": {
        "person": "3rd",
        "number": "singular",
        "be verb": "is",
        "type": "person.3rd.singular",
        "objective": "him",
        "possessive": "his"
    },
    "she": {
        "person": "3rd",
        "number": "singular",
        "be verb": "is",
        "type": "person.3rd.singular",
        "objective": "her",
        "possessive": "her"
    },
    "it": {
        "person": "3rd",
        "number": "singular",
        "be verb": "is",
        "type": "person.3rd.singular"
    },
    "they": {
        "person": "3rd",
        "number": "plural",
        "be verb": "are",
        "type": "person.3rd.plural",
        "objective": "them",
        "possessive": "their"
    }
}

VERBS = {
    "abide": {
        "past": "abode",
                "past participle": "abode"
    },
    "arise": {
        "past": "arose",
                "past participle": "arisen"
    },
    "awake": {
        "past": "awoke",
                "past participle": "awaken"
    },
    "be": {
        "past": [
            "was",
            "were"
        ],
        "past participle": "been"
    },
    "bear": {
        "past": "bore",
                "past participle": [
                    "borne",
                    "born"
                ]
    },
    "beat": {
        "past": "beat",
                "past participle": "beaten"
    },
    "become": {
        "past": "became",
                "past participle": "become"
    },
    "beget": {
        "past": [
            "begat",
            "begot"
        ],
        "past participle": "begotten"
    },
    "begin": {
        "past": "began",
                "past participle": "begun"
    },
    "bend": {
        "past": "bent",
                "past participle": "bent"
    },
    "bet": {
        "past": "bet",
                "past participle": "bet"
    },
    "bid": {
        "past": "bid"
    },
    "wake": {
        "past": "woke",
                "past participle": "waken"
    }
}
