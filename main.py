initial_state = "q0"
halt_state = "qf"
blank_symbol = "#"

transition_rules = {
    'q0 0': 'q0 1 R',
    'q0 1': 'q0 0 R',
    'q0 #': 'qf # N'
}


class TuringMachine:
    def __init__(self, tape_str, initial_state, halt_state, blank, rules):
        self.tape = {i: char for i, char in enumerate(tape_str)}
        self.state = initial_state
        self.halt_state = halt_state
        self.blank = blank
        self.rules = rules
        self.head_position = 0

    def step(self):
        current_char = self.tape.get(self.head_position, self.blank)
        lookup_key = self.state + " " + current_char
        if lookup_key not in self.rules:
            print("error", lookup_key)
            return False
        next_state, next_char, movement = self.rules[lookup_key].split()
        self.tape[self.head_position] = next_char
        self.state = next_state
        if movement == 'R':
            self.head_position += 1
        elif movement == 'L':
            self.head_position -= 1
        return True

    def run(self):
        while self.state != self.halt_state:
            if not self.step():
                break
        return self.get_tape_string()
    
    def get_tape_string(self):
        if not self.tape:
            return ""
        min_index = min(self.tape.keys())
        max_index = max(self.tape.keys())
        result = ""
        for i in range(min_index, max_index + 1):
            result += self.tape.get(i, self.blank)
        return result


def main():
    initial_tape = input("Введите ленту: ")
    tm = TuringMachine(
        initial_tape,
        initial_state,
        halt_state,
        blank_symbol,
        transition_rules
    )
    result = tm.run()
    print(result)

main()
#asalamu aleikum