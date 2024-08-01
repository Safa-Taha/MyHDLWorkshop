from myhdl import *
from stopwatch import StopWatch


# Converting to Verilog
def convert():
    tens_led, ones_led, tenths_led = [Signal(intbv(0)[7:]) for _ in range(3)]
    ss, rst, clk = [Signal(bool(0)) for _ in range(3)]
    inst = StopWatch(tens_led, ones_led, tenths_led, ss, rst, clk)
    inst.convert(hdl='Verilog')


if __name__ == "__main__":
    convert()
