module tb_execute;

reg clk;
reg [7:0] opcode;
reg [7:0] operand1;
reg [7:0] operand2;
wire [7:0] result;

initial begin
    $from_myhdl(
        clk,
        opcode,
        operand1,
        operand2
    );
    $to_myhdl(
        result
    );
end

execute dut(
    clk,
    opcode,
    operand1,
    operand2,
    result
);

endmodule
