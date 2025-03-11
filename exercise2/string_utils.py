# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    return s[::-1]
    pass


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0  # Initialisation du compteur

    for char in s:  # Parcourt chaque caractère de la chaîne
        if char in vowels:  # Vérifie si c'est une voyelle
            count += 1  # Incrémente le compteur

    return count  # Retourne le nombre de voyelles
    pass


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    # Mettre tout en minuscules pour ignorer la casse
    chaine_minuscule = s.lower()

    # Supprimer tous les espaces pour ne garder que les lettres
    chaine_sans_espaces = "".join(chaine_minuscule.split())

    # Vérifier si la chaîne obtenue est identique à son inverse
    chaine_inverse = chaine_sans_espaces[::-1]

    # Comparer les deux chaînes et retourner le résultat
    return chaine_sans_espaces == chaine_inverse
    pass


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    return s.title()
<<<<<<< Updated upstream
    pass
=======
    pass
>>>>>>> Stashed changes
