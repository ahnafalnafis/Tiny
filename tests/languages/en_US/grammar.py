import random

# Loading uppercase letters, lowercase letters, vowels, consonants, pronouns, etc. /env/basics/english.py
from env.basics.english import *


class UnknownWordError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidTenseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TenseConversionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class word(str):
    def __init__(self, word: str):
        self.word = word
        self.transformed = self.word.lower()

    def isnoun(self) -> bool:
        pass

    def ispronoun(self) -> bool:
        if self.transformed in PRONOUNS:
            return True
        else:
            return False

    def isverb(self) -> bool:
        if self.transformed in VERBS:
            return True
        else:
            return False

    def plural_form(self) -> str:
        if self.transformed[-1] in ['s', 'sh', 'ch', 'x', 'z'] or self.transformed[-2:] in ['s', 'sh', 'ch', 'x', 'z']:
            self.transformed += 'es'

        elif self.transformed[-2] in VOWELS:
            self.transformed += 's'

        elif self.transformed[-1] == 'y':
            self.transformed = self.transformed.replace('y', 'ies')

        else:
            self.transformed = self.transformed + 's'

        return self.transformed.title() if self.word[0] in UPPERCASE else self.transformed


class verb(word):
    def right_form(self, tense='present') -> str:
        if tense == 'present':
            if self.transformed in VERBS:
                for verb in VERBS:
                    if verb in self.transformed:
                        if self.transformed.replace(verb, '') in ['s', 'es']:
                            return 'VERB IS ALREADY IN SINGULAR FORM'

                if self.transformed.endswith('s'):
                    form = self.transformed + 'es'
                else:
                    form = self.transformed + 's'

            else:
                raise UnknownWordError(f"Invalid word: '{self.transformed}'")
            return form.title() if self.word[0].isupper() else form

        elif tense == 'past':
            pass
        elif tense == 'perfect':
            pass
        elif tense == 'continuous':
            pass

    def past_form(self, all=True) -> str:
        form = VERBS[self.transformed]['past']
        if isinstance(form, list):
            if all:
                new = ""
                count = 0
                for i in form:
                    if count == len(form) - 1:
                        new += i
                    else:
                        new += i + ' '
                    count += 1
                return new.replace(' ', '/').title() if self.word[0].isupper() else new
            else:
                return random.choice(form).title() if self.word[0].isupper() else random.choice(form)

        else:
            return form.title() if self.word[0].isupper() else form

    def past_participle_form(self, all='random') -> str:
        form = VERBS[self.transformed]['past participle']
        if isinstance(form, list):
            if all:
                new = ""
                count = 0
                for i in form:
                    if count == len(form) - 1:
                        new += i
                    else:
                        new += i + ' '
                    count += 1
                return new.replace(' ', '/').title() if self.word[0].isupper() else new
            else:
                return random.choice(form).title() if self.word[0].isupper() else random.choice(form)
        else:
            return form.title() if self.word[0].isupper() else form

    def base_form(self) -> str:
        for base in VERBS:
            for form in VERBS[base]:
                if isinstance(VERBS[base][form], list):
                    if self.transformed in VERBS[base][form]:
                        return form.title() if self.word[0].isupper() else base
                else:
                    if self.transformed == VERBS[base][form]:
                        return form.title() if self.word[0].isupper() else base
