from random import randrange
from myhdl import *
from stopwatch import TimeCount, BCDtoLED, StopWatch, encoding

PERIOD = 10
MAX_COUNT = 6 * 10 * 10

@block
def test_timecount():
    tens, ones, tenths = [Signal(intbv(0)[4:]) for _ in range(3)]
    ss, rst, clk = [Signal(bool(0)) for _ in range(3)]
    dut = TimeCount(tens, ones, tenths, ss, rst, clk)

    count = Signal(0)
    counting = Signal(False)

    @always(delay(PERIOD // 2))
    def clkgen():
        clk.next = not clk

    @always(ss.posedge, rst.posedge)
    def action():
        if rst:
            counting.next = False
            count.next = 0
        else:
            counting.next = not counting

    @always(clk.posedge)
    def counter():
        if counting:
            count.next = (count + 1) % MAX_COUNT

    @always(clk.negedge)
    def monitor():
        actual = (tens * 100) + (ones * 10) + tenths
        assert actual == count, f"Mismatch: actual={actual}, expected={count}"

    @instance
    def stimulus():
        test_cases = [
            (rst, True, 10),
            (rst, False, 100),
            (ss, True, 200),
            (ss, False, 300),
            (rst, True, 400),
            (ss, True, 500),
            (rst, False, 600),
            (ss, False, 700),
            # Simultaneous ss and rst
            (ss, True, 50),
            (rst, True, 50),
            (ss, False, 100),
            (rst, False, 100),
            # Extremely high and low counts
            (rst, True, 10),
            (rst, False, 10),
            (ss, True, 10),
            (ss, False, 10),
        ]
        for signal, value, wait_time in test_cases:
            yield delay(wait_time)
            yield clk.negedge
            signal.next = value
            yield delay(100)
            signal.next = not value
        raise StopSimulation

    return dut, clkgen, action, counter, monitor, stimulus

@block
def test_bcd2led():
    led = Signal(intbv(0)[7:])
    bcd = Signal(intbv(0)[4:])
    clk = Signal(bool(0))
    dut = BCDtoLED(led, bcd, clk)

    @always(delay(PERIOD // 2))
    def clkgen():
        clk.next = not clk

    @instance
    def check():
        for _ in range(100):
            bcd.next = randrange(10)
            yield clk.posedge
            yield clk.negedge
            expected = int(encoding[int(bcd)], 2)
            assert led == expected, f"BCD to LED Mismatch: bcd={int(bcd)}, actual={int(led)}, expected={expected}"
        raise StopSimulation

    return dut, clkgen, check

def test_all():
    sim = Simulation(test_timecount(), test_bcd2led())
    sim.run()

if __name__ == "__main__":
    test_all()
