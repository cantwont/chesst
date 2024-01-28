def load_names():
    names = []
    with open('names.txt', 'r') as file:
        for line in file:
            names.append(line.strip())
    return names