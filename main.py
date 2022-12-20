from FSM import FSM


alphabet2 = {'\n',' ','\t'}

line = "int "

line_as_list = list(line)

machine = FSM()

for value in line_as_list:
    machine.send_value(value)
