actions = """F10
N3
F7
R90
F11""".splitlines()

ab = filter(lambda x: x[0] in 'NESW', actions)
fs = filter(lambda x: x[0] in 'F', actions)
rel = filter(lambda x: x[0] in 'LR', actions)

# no idea