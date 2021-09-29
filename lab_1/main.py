"""
Lab 1
Language detection
"""


def tokenize(text: str) -> list or None:
    """
    Splits a text into tokens, converts the tokens into lowercase,
    removes punctuation and other symbols from words
    :param text: a text
    :return: a list of lower-cased tokens without punctuation
    """
    if not isinstance(text, str):
        return None
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', '}',
               ']', ';', '<', ',', '>', '.', '?', '|', '\\', ':', ';', '"', "'",
               '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if isinstance(text, str):
        for s in symbols:
            text = text.replace(s, '')
        text = text.lower()
        text = text.split()
        return text



def remove_stop_words(tokens: list, stop_words: list) -> list or None:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    """
    if not isinstance(tokens, list) or not isinstance(stop_words, list):
        return None
    checking_tokens = []
    for token in tokens:
        if token not in stop_words:
            checking_tokens.append(token)
    return checking_tokens



def calculate_frequencies(tokens: list) -> dict or None:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens
    :return: a dictionary with frequencies
    """

    if not isinstance(tokens, list):
        return None
    freq_dict = {}
    for token in tokens:
        if isinstance(token, str):
            if token in freq_dict:
                freq_dict[token] += 1
            else:
                freq_dict[token] = 1
        else:
            return None
    return freq_dict


def get_top_n_words(freq_dict: dict, top_n: int) -> list or None:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words
    :return: a list of the most common words
    """

    if not isinstance(freq_dict, dict) or not isinstance(top_n, int):
        return None
    top_n_words = []
    freq_dict_keys = [key for key in freq_dict]
    top_n_words = sorted(freq_dict, key=freq_dict.get, reverse=True)[:top_n]
    return top_n_words






def create_language_profile(language: str, text: str, stop_words: list) -> dict or None:
    """
    Creates a language profile
    :param language: a language
    :param text: a text
    :param stop_words: a list of stop words
    :return: a dictionary with three keys – name, freq, n_words
    """

    if not isinstance(language, str) or not isinstance(text, str) \
            or not isinstance(stop_words, list):
        return None
    frequencies = calculate_frequencies(remove_stop_words(tokenize(text), stop_words))
    return {'name': language, 'freq': frequencies, 'n_words': len(frequencies)}



def compare_profiles(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> float or None:
    """
    Compares profiles and calculates the distance using top n words
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: the distance
    """
    if not isinstance(unknown_profile, dict) or not isinstance(profile_to_compare, dict) or \
            not isinstance(top_n, int):
        return None
    top_unknown_profile = get_top_n_words(unknown_profile['freq'], top_n)
    top_profile_to_compare = get_top_n_words(profile_to_compare['freq'], top_n)
    common_words = []
    for profile_word in top_profile_to_compare:
        if profile_word in top_unknown_profile:
            common_words.append(profile_word)
    distance = round(len(common_words) / len(top_unknown_profile), 2)
    return distance


def detect_language(unknown_profile: dict, profile_1: dict, profile_2: dict, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile
    :param unknown_profile: a dictionary
    :param profile_1: a dictionary
    :param profile_2: a dictionary
    :param top_n: a number of the most common words
    :return: a language
    """
    if not isinstance(unknown_profile, dict) or not isinstance(profile_1, dict) or not isinstance(
            profile_2, dict) or not isinstance(top_n, int):
        return None
    compare_1 = compare_profiles(unknown_profile, profile_1, top_n)
    compare_2 = compare_profiles(unknown_profile, profile_2, top_n)
    language = ""
    if compare_1 > compare_2:
        language += profile_1['name']
    elif compare_2 > compare_1:
        language += profile_2['name']
    else:
        language += sorted([profile_1['name'], profile_2['name']])[0]
    return language


def compare_profiles_advanced(unknown_profile: dict, profile_to_compare: dict, top_n: int) -> list or None:
    """
    Compares profiles and calculates some advanced parameters
    :param unknown_profile: a dictionary
    :param profile_to_compare: a dictionary
    :param top_n: a number of the most common words
    :return: a dictionary with 7 keys – name, score, common, sorted_common, max_length_word,
    min_length_word, average_token_length
    """
    pass


def detect_language_advanced(unknown_profile: dict, profiles: list, languages: list, top_n: int) -> str or None:
    """
    Detects the language of an unknown profile within the list of possible languages
    :param unknown_profile: a dictionary
    :param profiles: a list of dictionaries
    :param languages: a list of possible languages
    :param top_n: a number of the most common words
    :return: a language
    """
    pass


def load_profile(path_to_file: str) -> dict or None:
    """
    Loads a language profile
    :param path_to_file: a path
    :return: a dictionary with three keys – name, freq, n_words
    """
    pass


def save_profile(profile: dict) -> int:
    """
    Saves a language profile
    :param profile: a dictionary
    :return: 0 if everything is ok, 1 if not
    """
    pass
