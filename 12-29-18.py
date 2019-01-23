def longest_dir(dir_string):
    length_list = []
    first_newline = dir_string.find("\n")
    length_list.append(first_newline)

    dir_string = dir_string[first_newline + 1:]
    old_depth = 0
    max_length = length_list[0]
    while len(dir_string) > 0:
        new_depth = 0
        while dir_string[new_depth] == "\t":
            new_depth += 1

        next_newline = dir_string.find("\n")
        if next_newline == -1:
            next_newline = len(dir_string)
        new_length = next_newline - new_depth

        depth_diff = new_depth - old_depth
        if depth_diff > 0:
            assert depth_diff == 1 # should only be 1 depth difference from parent to child
            length_list.append(length_list[-1] + new_length + 1)
        else:
            max_length = max(max_length, length_list[-1])
            length_list.pop()

            depth_diff *= -1
            for _ in range(depth_diff):
                length_list.pop()

            length_list.append(length_list[-1] + new_length + 1)

        dir_string = dir_string[next_newline + 1:]
        old_depth = new_depth
    
    return max(max_length, length_list[-1])

dir_string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
assert longest_dir(dir_string) == 20

dir_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert longest_dir(dir_string) == 32