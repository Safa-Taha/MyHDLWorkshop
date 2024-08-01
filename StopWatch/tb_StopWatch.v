module tb_StopWatch;

wire [6:0] tens_led;
wire [6:0] ones_led;
wire [6:0] tenths_led;
reg ss;
reg rst;
reg clk;

initial begin
    $from_myhdl(
        ss,
        rst,
        clk
    );
    $to_myhdl(
        tens_led,
        ones_led,
        tenths_led
    );
end

StopWatch dut(
    tens_led,
    ones_led,
    tenths_led,
    ss,
    rst,
    clk
);

endmodule
