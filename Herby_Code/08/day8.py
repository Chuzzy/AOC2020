class console():
    #ops = {'nop': lambda _: (self.pc + 1, self.acc),\
    #         'acc': 2}
    #do_op = lambda p: ops[p[0]](p[1])

    def __init__(self, program):
        self.acc = 0
        self.pc = 0
        self.program = [( (s := l.split(' '))[0], int(s[1]) ) for l in program.splitlines()]


    def step(self, debug = False):

        opcode, operand = self.program[self.pc]

        if debug: print(f'pc {self.pc+1}\nopcode {opcode}\noperand {operand}\n')

        if opcode == 'nop':
            self.pc += 1
        elif opcode == 'acc':
            self.pc += 1
            self.acc += operand
        elif opcode == 'jmp':
            self.pc += operand
        
        return self.pc
    
    def check_loop(self):
        visited = []
        #last = 0

        while ( (last := self.step()) not in visited ) and ( last != len(self.program) ):
            acc = self.acc
            visited.append(last)
        

        if last == len(self.program):
            return ('finished', self.acc)
        else:
            return ('loop', acc)


program = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


program = open('input8.txt', 'r').read()
c = console(program)
print('Part 1:', c.check_loop()[1])


for i in range(len(c.program)):
    c = console(program)
    #print(i, c.program[i])
    if c.program[i][0] == 'nop':
        c.program[i] = ('jmp', c.program[i][1])
        end = c.check_loop()
    elif c.program[i][0] == 'jmp':
        c.program[i] = ('nop', c.program[i][1])
        end = c.check_loop()
    
    if end[0] == 'finished':
        print('Part 2:', end[1])
        break