#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4
    
    names = dir(hidden_4)

    non_hidden_names = [name for name in names if not name.startswith("__")]
    
    sorted_names = sorted(non_hidden_names)

        for  name in sorted names:
            print(name )

