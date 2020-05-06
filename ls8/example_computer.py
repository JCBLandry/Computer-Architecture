import sys

# op codes (operations codes)
PRINT_JUSTIN   = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4
PRINT_REGISTER = 5
ADD            = 6

print_justin_program = [
    PRINT_JUSTIN,
    PRINT_JUSTIN,
    PRINT_JUSTIN,
    PRINT_JUSTIN,
    HALT,
]

print_some_nums = [
    PRINT_NUM,
    12,
    PRINT_NUM,
    15,
    PRINT_NUM,
    37,
    PRINT_JUSTIN,
    HALT,
]

save_num_to_reg = [
    SAVE, # SAVE, VAL, REG_NUM
    65,
    2,
    PRINT_REGISTER,
    HALT,
]

add_numbers = [
    SAVE, # SAVE number 12 to reg 1
    12,
    1,
    SAVE, # SAVE number 12 to reg 2
    45,
    2,
    ADD, # Reg1 += Reg2 (we add the two values in the two reg and store the result in the first register)
    1,
    2,
    PRINT_REGISTER,
    1,
    HALT,
]

memory = add_numbers



# lets write a basic computer

running = True
pc = 0
registers = [0] * 8


while running:
    
    # lets do some things
    command = memory[pc] 

    # lets receive some intructions and execute them
    # if command if PRINT_JUSTIN
    if command == PRINT_JUSTIN:
        print('Justin')
        pc += 1
        # print out Justin's name
    
    # if command is HALT
    elif command == HALT:
        # shutdown
        running = False
        pc += 1
    elif command == PRINT_NUM:
        # look at next line for number
        num = memory[pc + 1]
         # print that number
        print(num)
        pc += 2
    
    elif command == SAVE:
        num_to_save = memory[pc + 1]
        register = memory[pc + 2]
        registers[register] = num_to_save
        pc += 3

    elif command == PRINT_REGISTER:
        register = memory[pc + 1]
        print(registers[registers])
        pc += 2
    
    elif command == ADD:
        register1 = memory[pc + 1]
        register2 = memory[pc + 2]
        val1 = registers[register1]
        val2 = registers[register2]
        registers[register1] = val1 + val2
        pc += 3

    else:
    # if command is non reconizable
        print(f"Unknown Instructions: (command)")
        sys.exit(1)
        # lets crash :(

    