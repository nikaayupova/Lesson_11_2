def foo(word):
    """

    :param word:
    :return:
    """
    return word.upper()


def foo_2(word):
    """

    :param word:
    :return:
    """
    words_list = word.split()
    result = []
    for word in words_list:
        result.append(word.capitalize())
    return ' '.join(result)
