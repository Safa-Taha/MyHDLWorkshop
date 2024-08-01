from myhdl import *


@block
def TimeCount(tens, ones, tenths, ss, rst, clk):
    @instance
    def logic():
        seen = False
        counting = False

        while True:
            yield clk.posedge, rst.posedge

            if rst:
                tens.next = 0
                ones.next = 0
                tenths.next = 0
                seen = False
                counting = False
            else:
                if ss and not seen:
                    seen = True
                    counting = not counting
                elif not ss:
                    seen = False

                if counting:
                    if tenths == 9:
                        tenths.next = 0
                        if ones == 9:
                            ones.next = 0
                            if tens == 5:
                                tens.next = 0
                            else:
                                tens.next = tens + 1
                        else:
                            ones.next = ones + 1
                    else:
                        tenths.next = tenths + 1

    return logic

encoding =  {0: "1000000", 1: "1111001", 2: "0100100", 3: "0110000",
             4: "0011001", 5: "0010010", 6: "0000010", 7: "1111000",
             8: "0000000", 9: "0010000"}



@block
def BCDtoLED(led, bcd, clk):
    code = tuple(int(encoding[i], 2) for i in range(10))

    @always(clk.posedge)
    def logic():
        led.next = code[int(bcd)]

    return logic



@block
def StopWatch(tens_led, ones_led, tenths_led, ss, rst, clk):
    tens, ones, tenths = [Signal(intbv(0)[4:]) for _ in range(3)]

    timecount_inst = TimeCount(tens, ones, tenths, ss, rst, clk)
    bcd2led_tens = BCDtoLED(tens_led, tens, clk)
    bcd2led_ones = BCDtoLED(ones_led, ones, clk)
    bcd2led_tenths = BCDtoLED(tenths_led, tenths, clk)

    return timecount_inst, bcd2led_tens, bcd2led_ones, bcd2led_tenths
