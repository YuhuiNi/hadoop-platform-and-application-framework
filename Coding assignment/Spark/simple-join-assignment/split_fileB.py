def split_fileB(line):
        # split the input line into word, date and count_string
        dateword_count = line.split(",")
        count_string = key_value[1]
        date_word = key_value[0].split(" ")
        date = date_word[0]
        word = date_word[1] 
        return (word, date + " " + count_string)