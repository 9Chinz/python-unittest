def reverse_word(in_wrd: str) -> str:
    return ' '.join([wrd[::-1] for wrd in in_wrd.split(' ')])
