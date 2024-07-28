from myhdl import block, delay, instance, Signal, StopSimulation, Simulation
from logic_gates import And2, Or2, Not1



@block
def test_comb():
    input1, input2, and_output, or_output, not_output = [Signal(bool(0)) for _ in range(5)]

    and_inst = And2(and_output, input1, input2)
    or_inst = Or2(or_output, input1, input2)
    not_inst = Not1(not_output, input1)

    @instance
    def stimulus():
        print("input1 input2 | and or not_input1")
        for i in range(4):
            # Set input1 and input2 values and wait for the output to change
            input1.next, input2.next = ((i >> 1) & 1), (i & 1)
            yield delay(10)
            print("{} {} | {} {} {}".format(
                int(input1), int(input2), 
                int(and_output), int(or_output), int(not_output)))
        raise StopSimulation()

    return and_inst, or_inst, not_inst, stimulus



# Convert to Verilog
def convert():
    input1, input2, and_output, or_output, not_output = [Signal(bool(0)) for _ in range(5)]

    and_inst = And2(and_output, input1, input2)
    or_inst = Or2(or_output, input1, input2)
    not_inst = Not1(not_output, input1)

    and_inst.convert(hdl='Verilog')
    or_inst.convert(hdl='Verilog')
    not_inst.convert(hdl='Verilog')

if __name__ == "__main__":
    tb = test_comb()
    tb.config_sim(trace=False)
    tb.run_sim()

    convert()

