// File: StopWatch.v
// Generated by MyHDL 0.11.45
// Date: Thu Aug  1 15:52:18 2024


`timescale 1ns/10ps

module StopWatch (
    tens_led,
    ones_led,
    tenths_led,
    ss,
    rst,
    clk
);


output [6:0] tens_led;
reg [6:0] tens_led;
output [6:0] ones_led;
reg [6:0] ones_led;
output [6:0] tenths_led;
reg [6:0] tenths_led;
input ss;
input rst;
input clk;

reg [3:0] tens;
reg [3:0] ones;
reg [3:0] tenths;



always @(posedge clk, posedge rst) begin: STOPWATCH_TIMECOUNT0_LOGIC
    reg seen;
    reg counting;
    if (rst) begin
        tens <= 0;
        ones <= 0;
        tenths <= 0;
        seen = 1'b0;
        counting = 1'b0;
    end
    else begin
        if ((ss && (!seen))) begin
            seen = 1'b1;
            counting = (!counting);
        end
        else if ((!ss)) begin
            seen = 1'b0;
        end
        if (counting) begin
            if ((tenths == 9)) begin
                tenths <= 0;
                if ((ones == 9)) begin
                    ones <= 0;
                    if ((tens == 5)) begin
                        tens <= 0;
                    end
                    else begin
                        tens <= (tens + 1);
                    end
                end
                else begin
                    ones <= (ones + 1);
                end
            end
            else begin
                tenths <= (tenths + 1);
            end
        end
    end
end


always @(posedge clk) begin: STOPWATCH_BCDTOLED0_LOGIC
    case (tens)
        0: tens_led <= 64;
        1: tens_led <= 121;
        2: tens_led <= 36;
        3: tens_led <= 48;
        4: tens_led <= 25;
        5: tens_led <= 18;
        6: tens_led <= 2;
        7: tens_led <= 120;
        8: tens_led <= 0;
        default: tens_led <= 16;
    endcase
end


always @(posedge clk) begin: STOPWATCH_BCDTOLED1_LOGIC
    case (ones)
        0: ones_led <= 64;
        1: ones_led <= 121;
        2: ones_led <= 36;
        3: ones_led <= 48;
        4: ones_led <= 25;
        5: ones_led <= 18;
        6: ones_led <= 2;
        7: ones_led <= 120;
        8: ones_led <= 0;
        default: ones_led <= 16;
    endcase
end


always @(posedge clk) begin: STOPWATCH_BCDTOLED2_LOGIC
    case (tenths)
        0: tenths_led <= 64;
        1: tenths_led <= 121;
        2: tenths_led <= 36;
        3: tenths_led <= 48;
        4: tenths_led <= 25;
        5: tenths_led <= 18;
        6: tenths_led <= 2;
        7: tenths_led <= 120;
        8: tenths_led <= 0;
        default: tenths_led <= 16;
    endcase
end

endmodule
