def kebab_case(string):
    return "-".join(word.lower() for word in string.split())
