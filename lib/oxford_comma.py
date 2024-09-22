def oxford_comma(items):
    if len(items) == 1:
        return items[0]  # Return the only element if the list has one element
    elif len(items) == 2:
        return " and ".join(items)  # Join two elements with 'and' without a comma
    else:
        return ", ".join(items[:-1]) + f", and {items[-1]}"  # Oxford comma for lists with 3+ items
