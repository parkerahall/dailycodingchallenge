def flatten(dictionary):
    new_dict = {}
    for key in dictionary:
        value = dictionary[key]
        if isinstance(value, dict):
            flattened = flatten(value)
            for inner_key in flattened:
                new_dict[key + "." + inner_key] = flattened[inner_key]
        else:
            new_dict[key] = value
    return new_dict

dictionary = {"key" : 3,
              "foo" : {
                "a" : 5,
                "bar" : {"baz" : 8}
                }
              }
expected = {"key" : 3,
            "foo.a" : 5,
            "foo.bar.baz" : 8}
assert flatten(dictionary) == expected