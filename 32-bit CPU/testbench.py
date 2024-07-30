from myhdl import Signal, intbv, delay, instance, always, now, Simulation, traceSignals, instances
from cpu import clk, instruction, opcode, operand1, operand2, result, fetch, decode, execute, writeback


def test_cpu():
    fetched_instruction = Signal(intbv(0)[32:])
    
    fetch_inst = fetch(clk, instruction, fetched_instruction)
    decode_inst = decode(clk, fetched_instruction, opcode, operand1, operand2)
    execute_inst = execute(clk, opcode, operand1, operand2, result)
    writeback_inst = writeback(clk, result)

    @always(delay(10))
    def clk_driver():
        clk.next = not clk


    @instance
    def stimulus():
        for _ in range(10):
            yield clk.posedge
            instruction.next = 0b00000001 << 24 | 0b00000011 << 16 | 0b00000011 << 8 | 0b00000011  
            yield clk.posedge
            print(f"Clock: {clk}, Time: {now()}, Instruction: {instruction}, Result: {result}")

    return instances()


if __name__ == "__main__":
    tb = traceSignals(test_cpu)
    sim = Simulation(tb)
    sim.run(100)
