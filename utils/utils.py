def print_header(title, width=80, char='#'):
    title = title.split('\n')
    print(char * width)
    for line in title:
        print(f"##{line.center(width - 4, ' ')}##")
    print(char * width)
    print()