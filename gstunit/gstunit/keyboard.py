from abc import ABC, abstractmethod

class BaseKeyboardMapping(ABC):
    @abstractmethod
    def get_translation(self, character):
        """
        Abstract method to get the translation of a character for
        keyboard input.
        """
        pass

    @abstractmethod
    def get_characters(self):
        """
        Abstract method to get all characters supported by
        the mapping.
        """
        pass


class NdebeKeyboardMapping(BaseKeyboardMapping):
    def __init__(self):
        # Define your mapping dictionary here
        self.mapping = {
            "{numbers}": "\uE101\uE102\uE103",
            "{ent}": "return",
            "{escape}": "esc ⎋",
            "{tab}": "tab ⇥",
            "{backspace}": "⌫",
            "{capslock}": "caps lock ⇪",
            "{shift}": "⇧",
            "{controlleft}": "ctrl ⌃",
            "{controlright}": "ctrl ⌃",
            "{altleft}": "alt ⌥",
            "{altright}": "alt ⌥",
            "{metaleft}": "cmd ⌘",
            "{metaright}": "cmd ⌘",
            "{abc}": "ABC"
        }

    def get_translation(self, character):
        """
        Get the translation of a character for keyboard input.
        """
        return self.mapping.get(character, character)

    def get_characters(self):
        """
        Get all characters supported by the mapping.
        """
        return self.mapping.keys()


class NdebeStandardLayoutMapping(KeyboardMapping):
    def __init__(self):
        # Define your mapping dictionary here
        self.mapping = {
            "`": "\uE101",
            "\uE101": "\uE101",
            "\uE102": "\uE102",
            "\uE103": "\uE103",
            "\uE104": "\uE104",
            "\uE105": "\uE105",
            "\uE106": "\uE106",
            "\uE107": "\uE107",
            "\uE108": "\uE108",
            "\uE109": "\uE109",
            "\uE100": "\uE100",
            "-": "-",
            "=": "=",
            "{bksp}": "{bksp}",
            "{tab}": "{tab}",
            "\uE259": "\uE259",
            "\uE300": "\uE300",
            "\uE253": "\uE253",
            "\uE351": "\uE351",
            "\uE350": "\uE350",
            "\uE301": "\uE301",
            "\uE265": "\uE265",
            "\uE354": "\uE354",
            "\uE262": "\uE262",
            "\uE26B": "\uE26B",
            "[": "[",
            "]": "]",
            "\\": "\\",
            "{lock}": "{lock}",
            "\uE256": "\uE256",
            "\uE302": "\uE302",
            "\uE353": "\uE353",
            "\uE352": "\uE352",
            "\uE303": "\uE303",
            "\uE250": "\uE250",
            "\uE355": "\uE355",
            "\uE304": "\uE304",
            "\uE268": "\uE268",
            ";": ";",
            "'": "'",
            "{enter}": "{enter}",
            "{shift}": "{shift}",
            "\uE356": "\uE356",
            "\uE25C": "\uE25C",
            "\uE305": "\uE305",
            "\uE25F": "\uE25F",
            "\uE254": "\uE254",
            "\uE26C": "\uE26C",
            "\uE26D": "\uE26D",
            ",": ",",
            ".": ".",
            "/": "/",
            "@": "@",
            "·": "·",
            "{space}": "{space}",
            "~": "~",
            "!": "!",
            "#": "#",
            "$": "$",
            "%": "%",
            "^": "^",
            "&": "&",
            "*": "*",
            "(": "(",
            ")": ")",
            "_": "_",
            "+": "+",
            "\uE25B": "\uE25B",
            "\uE10B": "\uE10B",
            "\uE255": "\uE255",
            "\uE10C": "\uE10C",
            "\uE10D": "\uE10D",
            "\uE10E": "\uE10E",
            "\uE267": "\uE267",
            "\uE10F": "\uE10F",
            "\uE264": "\uE264",
            "\uE25A": "\uE25A",
            "{": "{",
            "}": "}",
            "|": "|",
            "\uE10A": "\uE10A",
            "\uE258": "\uE258",
            "\uE110": "\uE110",
            "\uE111": "\uE111",
            "\uE112": "\uE112",
            "\uE113": "\uE113",
            "\uE252": "\uE252",
            "\uE266": "\uE266",
            "\uE263": "\uE263",
            "\uE26A": "\uE26A",
            ":": ":",
            '"': '"',
            "\uE257": "\uE257",
            "\uE25E": "\uE25E",
            "\uE251": "\uE251",
            "\uE261": "\uE261",
            "\uE269": "\uE269",
            "\uE25D": "\uE25D",
            "\uE260": "\uE260",
            "<": "<",
            ">": ">",
            "?": "?",
        }

    def get_translation(self, character):
        """
        Get the translation of a character for keyboard input.
        """
        return self.mapping.get(character, character)

    def get_characters(self):
        """
        Get all characters supported by the mapping.
        """
        return self.mapping.keys()


class NdebeMobileLayoutMapping(KeyboardMapping):
    def __init__(self):
        # Define your mapping dictionary here
        self.mapping = {
            "\uE259": "\uE259",
            "\uE300": "\uE300",
            "\uE253": "\uE253",
            "\uE351": "\uE351",
            "\uE350": "\uE350",
            "\uE301": "\uE301",
            "\uE265": "\uE265",
            "\uE354": "\uE354",
            "\uE262": "\uE262",
            "\uE26B": "\uE26B",
            "\uE256": "\uE256",
            "\uE302": "\uE302",
            "\uE353": "\uE353",
            "\uE352": "\uE352",
            "\uE303": "\uE303",
            "\uE250": "\uE250",
            "\uE355": "\uE355",
            "\uE304": "\uE304",
            "\uE268": "\uE268",
            "{shift}": "{shift}",
            "\uE356": "\uE356",
            "\uE25C": "\uE25C",
            "\uE305": "\uE305",
            "\uE25F": "\uE25F",
            "\uE254": "\uE254",
            "\uE26C": "\uE26C",
            "\uE26D": "\uE26D",
            "{backspace}": "{backspace}",
            "{numbers}": "{numbers}",
            "{space}": "{space}",
            "{ent}": "{ent}",
            "\uE101": "\uE101",
            "\uE102": "\uE102",
            "\uE103": "\uE103",
            "\uE104": "\uE104",
            "\uE105": "\uE105",
            "\uE106": "\uE106",
            "\uE107": "\uE107",
            "\uE108": "\uE108",
            "\uE109": "\uE109",
            "{abc}": "{abc}",
            "\uE100": "\uE100",
            "{bksp}": "{bksp}"
            # Add more mappings as needed
        }

    def get_translation(self, character):
        """
        Get the translation of a character for keyboard input.
        """
        return self.mapping.get(character, character)

    def get_characters(self):
        """
        Get all characters supported by the mapping.
        """
        return self.mapping.keys()
