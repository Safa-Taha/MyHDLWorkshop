module tb_MUX_Two_One;

wire [7:0] z;
reg [7:0] a;
reg [7:0] b;
reg [1:0] sel;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        z
    );
end

MUX_Two_One dut(
    z,
    a,
    b,
    sel
);

endmodule
