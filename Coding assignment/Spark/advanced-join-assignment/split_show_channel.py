def split_show_channel(line):
        show_channel = line.split(",")
        show = show_views[0]
        channel = show_views[1]
        return (show, channel)