# Old Norwegian Dictionary

Old Norwegian/Norse Dictionary for Python. The dictionary consists of 40 000+ Old Norse words with Norwegian translations.

Based on "Dictionary of the Old Norwegian Language".

### Install

`pip install old-norwegian-dictionary`

### Usage

The project provides a getter for the whole dataset. You can use it in your script to populate your own database or otherwise use the data.

Should you want to use the data without this Python library, you might want to check [Old Norwegian Dictionary Builder](https://github.com/stscoundrel/old-norwegian-dictionary-builder)


```python

from old_norwegian_dictionary import get_dictionary

# Whole dictionary of +42 000 entries
dictionary = get_dictionary()

# Dictionaries return entries that consist of headword, part of speech and definition.
print(dictionary[25000].word)           # náðuliga
print(dictionary[25000].part_of_speech) # adv
print(dictionary[25000].definition)     # náðuliga, adv.  1)  i Stilhed, ubemærket; hann bauð at hafa [...and more]

```

Individual words are returned in format of:

```python
{
    word: str
    part_of_speech: str
    definition: str
}
```



### About "Dictionary of the Old Norwegian Language"

_"Ordbog over det gamle norske Sprog"_ dictionary was published in late 1800s by Johan Fritzner. Its is the largest Old Norse to Norwegian dictionary, containing over 40 000 word definitions. While the original dictionary is called dictionary of "old norwegian", it is practically a dictionary of western Old Norse. Technically "Old Norwegian" would be a later stage in the language.
