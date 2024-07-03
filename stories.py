"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "History",
    "A History Tale",
    ["Place", "Noun", "Verb", "Adjective", "Plural_noun"],
    """Once upon a time in a long-ago {Place}, there lived a
       large {Adjective} {Noun}. It loved to {Verb} {Plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["Noun", "Verb"],
    """OMG!! OMG!! I love to {Verb} a {Noun}!"""
)

story3 = Story(
    "Kids",
    "Foods",
    ["Adjective", "Foods1", "Verb", "Saying", "Noun", "Foods2", "Color", "Vehicle", "Animal", "Person"],
    """Today I went to my favorite Taco Stand called the {Adjective} {Animal}. Unlike most food stands, they cook and prepare the food in a {Vehicle} while you {Verb}. The best thing on the menu is the {Color} {Noun}. Instead of ground beef they fill the taco with {Foods1}, cheese, and top it off with a salsa made from {Foods2}. If that doesn't make your mouth water, then it's just like {Person} always says: {Saying}!"""
)

story4 = Story(
    "Kids-Fav",
    "Gingerbread Man",
    ["Place", "Adjective", "Verb_Action", "Food", "Things", "Profession", "Thing", "Color", "Celebrity", "Animal"],
    """There once was a gingerbread man who had two {Things} for eyes and a {Food} for a nose. He always said, '{Verb_Action} as fast as you can, you can't catch me I'm the gingerbread man.' One day he ran past a {Adjective} {Profession}, but they couldn't catch him. He kept running until he passed a {Animal}, but they couldn't catch him either. Suddenly, he came across a river near {Place}. How would he cross? Then he saw a {Color} {Thing} floating by. He jumped on it, but it was actually {Celebrity}--who just so happened to love cookies :)"""
)

story5 = Story(
    "Kids-Love",
    "Butterflies",
    ["Things", "An_Insect", "Verb", "Saying", "Color", "Adjective1", "Food", "Person", "Adjective2", "Place"],
    """Last night I dreamed I was a {Adjective2} butterfly with {Color} splotches that looked like {Things}. I flew to {Place} with my best friend, {Person}, who was a {Adjective1} {An_Insect}. We ate some {Food} when we got there and then decided to {Verb}. The dream ended when I said, '{Saying}.'"""
)

stories = {s.code : s for s in [story1 , story2 , story3 , story4 , story5]}