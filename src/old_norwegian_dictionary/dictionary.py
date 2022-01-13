from . import reader
from typing import NamedTuple, Tuple

DICTIONARY_PATH = 'dictionary.json'

class DictionaryEntry(NamedTuple):
    word: str
    part_of_speech: str
    definition: str


def get_dictionary() -> Tuple[DictionaryEntry, ...]:
    raw_data = reader.read_json(DICTIONARY_PATH)

    return tuple(
        DictionaryEntry(raw_entry["word"], raw_entry['partOfSpeech'], raw_entry["definition"])
        for raw_entry in raw_data
    )
