def get_formatted_name(first, last, middle=""):
    first = first.title()
    last = last.title()
    if (middle):
        middle = middle.title()
        return (first + " " + middle + " " + last)
    return (first + " " +last)

