V = ['a', 'e', 'ẹ', 'i', 'o', 'ọ', 'u']
Vn = ['an', 'ẹn', 'in', 'ọn', 'un']
N = ['m', 'n']
C = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 's', 't', 'w', 'y']
D = ['gb']


def syllabicator(word):

    syllable = ''
    while len(word) >= 1:
        if len(word) > 3:
            if word[-4:-2] in D and word[-2:] in Vn:  # DVn
                syllable = word[-4:] + ' ' + syllable
                word = word[0:4]
            else:
                if word[-3:-1] in D and word[-1] in V:  # DV Structure
                    syllable = word + ' ' + syllable
                    word = word[0:-3]

                elif word[-3] in C and word[-2:] in Vn:  # CVn Structure
                    syllable = word[-3:] + ' ' + syllable
                    word = word[0:-3]
                else:
                    if word[-2] in C and word[-1] in V:  # CV Structure
                        syllable = word[-2:] + ' ' + syllable
                        word = word[0:-2]
                    elif word in Vn:  # Vn Structure
                        syllable = word[-2:] + ' ' + syllable
                        word = word[0:-2]
                    else:
                        if word[-1] in V:  # V Structure
                            syllable = word[-1:] + ' ' + syllable
                            word = word[0:-1]
                        elif word[-1] in N:
                            syllable = word[-1:] + ' ' + syllable
                            word = word[0:-1]
                        else:
                            raise ValueError('An error occurred with last char')

        elif len(word) == 3:
            if word[-3:-1] in D and word[-1] in V:  # DV Structure
                syllable = word[-3:] + ' ' + syllable
                word = word[0:-3]

            elif word[-3] in C and word[-2:] in Vn:  # CVn Structure
                syllable = word[-3:] + ' ' + syllable
                word = word[0:-3]
            else:
                if word[-2] in C and word[-1] in V:  # CV Structure
                    syllable = word[-2:] + ' ' + syllable
                    word = word[0:-2]
                elif word in Vn:  # Vn Structure
                    syllable = word[-2:] + ' ' + syllable
                    word = word[0:-2]
                else:
                    if word[-1] in V:  # V Structure
                        syllable = word[-1:] + ' ' + syllable
                        word = word[0:-1]
                    elif word[-1] in N:
                        syllable = word + ' ' + syllable
                        word = word[0:-1]
                    else:
                        raise ValueError('An error occurred with last char')

        elif len(word) == 2:
            if word[-2] in C and word[-1] in V:  # CV Structure
                syllable = word[-2:] + ' ' + syllable
                word = word[0:-2]
            elif word in Vn:  # Vn Structure
                syllable = word[-2:] + ' ' + syllable
                word = word[0:-2]
            else:
                if word[-1] in V:  # V Structure
                    syllable = word[-1:] + ' ' + syllable
                    word = word[0:-1]
                elif word[-1] in N:
                    syllable = word[-1:] + ' ' + syllable
                    word = word[0:-1]
                else:
                    raise ValueError('An error occurred with last char')

        else:
            if word[-1] in V:  # V Structure
                syllable = word[-1:] + ' ' + syllable
                word = word[0:-1]
            elif word[-1] in N:
                syllable = word[-1:] + ' ' + syllable
                word = word[0:-1]
            else:
                raise ValueError('An error occurred with last char')

    return syllable






print(syllabicator('la'))
print(syllabicator('gba'))
print(syllabicator('fun'))
print(syllabicator('gbafun'))

print(syllabicator('tẹtan'))
print(syllabicator('sunkanmi'))
print(syllabicator('kalokalo'))

