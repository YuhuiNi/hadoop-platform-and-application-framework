def split_show_views(line):
        show_views = line.split(",")
        show = show_views[0]
        views = show_views[1]
        return (show, views)