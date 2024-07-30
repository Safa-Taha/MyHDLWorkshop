from myhdl import Signal, intbv, always

OP_ADD = 1
OP_SUB = 2
OP_MUL = 3
OP_DIV = 4
OP_REM = 5

# Signals
clk = Signal(bool(0))
instruction = Signal(intbv(0)[32:])
opcode = Signal(intbv(0)[8:])
operand1 = Signal(intbv(0)[8:])
operand2 = Signal(intbv(0)[8:])
result = Signal(intbv(0)[8:])


def fetch(clk, instruction, fetched_instruction):
    @always(clk.posedge)
    def logic():
        fetched_instruction.next = instruction
    return logic


def decode(clk, fetched_instruction, opcode, operand1, operand2):
    @always(clk.posedge)
    def logic():
        opcode.next = fetched_instruction[24:16]
        operand1.next = fetched_instruction[16:8]
        operand2.next = fetched_instruction[8:0]
    return logic


def execute(clk, opcode, operand1, operand2, result):
    @always(clk.posedge)
    def logic():
        if opcode == OP_ADD:
            result.next = operand1 + operand2
        elif opcode == OP_SUB:
            result.next = operand1 - operand2
        elif opcode == OP_MUL:
            result.next = operand1 * operand2
        elif opcode == OP_DIV:
            result.next = operand1 // operand2
        elif opcode == OP_REM:
            result.next = operand1 % operand2
    return logic


def writeback(clk, result):
    @always(clk.posedge)
    def logic():
        pass  
    return logic
