def capitalize_string(string):
    """
    Возвращает строку с заглавными буквами.
    """
    return string.upper()

def capitalize_first_letters(string):
    """
    Возвращает строку, в которой первые буквы каждого слова заглавные.
    """
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)