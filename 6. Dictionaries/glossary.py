glossary = {
    'variable': 'Variables are containers for storing data values.',
    'numbers': 'There are three numeric types in Python: int, float, complex.',
    'lists': 'Lists are used to store multiple items in a single variable.',
    'if_statements': 'The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.',
    'dictionaries': 'Dictionaries are used to store data values in key:value pairs.',
    'tuples': 'A tuple is a collection which is ordered and unchangeable.',
    'for_loop': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).',
    'comments': 'Comments can be used to explain Python code, to make the code more readable, or to prevent execution when testing code.',
    'operators': 'Operators are used to perform operations on variables and values.',
    'functions': 'A function is a block of code which only runs when it is called. A function can return data as a result. A function helps avoiding code repetition.',
    }

for word, meaning in glossary.items():
    print(f"{word}: {meaning}")