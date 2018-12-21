def split_fileA(line):
        # split the input line in word and count on the comma
        key_value = line.split(",")
        word = key_value[0]
        # turn the count to an integer  
        count = int(key_value[1])
        return (word, count)