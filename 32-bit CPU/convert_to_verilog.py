from myhdl import toVerilog, Signal, intbv
from cpu import clk, instruction, opcode, operand1, operand2, result, fetch, decode, execute, writeback

fetched_instruction = Signal(intbv(0)[32:])


toVerilog(fetch, clk, instruction, fetched_instruction)
toVerilog(decode, clk, fetched_instruction, opcode, operand1, operand2)
toVerilog(execute, clk, opcode, operand1, operand2, result)
toVerilog(writeback, clk, result)
