from src import old_norwegian_dictionary


def test_dictionary_has_correct_length() -> None:
    result = old_norwegian_dictionary.get_dictionary()
    assert len(result) == 42021


def test_dictionary_entries_are_not_empty() -> None:
    result = old_norwegian_dictionary.get_dictionary()

    for entry in result:
        assert entry.word
        assert entry.part_of_speech
        assert entry.definition


def test_dictionary_has_expected_content() -> None:
    result = old_norwegian_dictionary.get_dictionary()

    assert result[0].word == '-æri'
    assert result[0].part_of_speech == 'uten ordklasse'
    assert result[0].definition == '-æri (af ár dvs. Aar) i hallæri.'

    assert result[10000].word == 'fri'
    assert result[10000].part_of_speech == 'm'
    assert result[10000].definition == 'fri, m. = friðill. Hým. 9.'

    assert result[25000].word == 'náðuliga'
    assert result[25000].part_of_speech == 'adv'
    assert result[25000].definition == 'náðuliga, adv.  1)  i Stilhed, ubemærket; hann bauð at hafa Hánef þar á launþar til, er skip kemr n. at, svá athonum mætti útan koma Vem. 591; B.biskup biðr nú því öruggari til guðsaf öllu hjarta, sem hann má þat náð-uligar ok leyniligar gera fyrir mönn-um Mar. 116911 fg; biðjandi því meðmeira athuga, sem hann mátti leyni-ligar ok auðveldligar (&vl náðuligar)Mar. 83710. 34.  2)  naadigen; biðjom vér,at þér takir þessum várum erendumbetr ok náðuligar, en vér erum verðirDN. VII, 19013.'

    assert result[42000].word == 'þyrnir'
    assert result[42000].part_of_speech == 'm'
    assert result[42000].definition == 'þyrnir, m. Tjørn, Tornebusk. Stj. 39611;Hom. 10218; Post. 75034; Klm. 54615;Mar. 3378. 10351.'
