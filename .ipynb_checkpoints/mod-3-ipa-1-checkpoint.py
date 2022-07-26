def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if ord(letter) == 32: 
        print(" ")
    elif (ord(letter) + shift) >= 91:
        return chr((ord(letter) + shift - 90) + 64)
    elif ord(letter) >=65:
        return chr(ord(letter) + shift)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    caesar = ""
    for i in message: 
        if i.isupper():
            i_upper = ord(i) - ord("A")
            i_new = chr((i_upper + shift) % 26 + ord("A"))
            caesar += i_new
        elif i.islower(): 
            i_lower = ord(i) - ord("a") 
            i_new = chr((i_lower + shift) % 26 + ord("a"))
            caesar += i_new
        elif i.isdigit():
            i_new = (int(i) + shift) % 10
            caesar += str(i_new)
        else:
            caesar += i
    return caesar

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if ord(letter) == 32:
        print(" ")
    for i in range(65, 91):
        if ((ord(letter) - ord("A")) + ord(letter_shift)) >= 91: 
            return chr((ord(letter) + ord(letter_shift)) - 91)
        elif ord(letter) >= 65:
            return chr(((ord(letter) - ord("A")) + ord(letter_shift)))