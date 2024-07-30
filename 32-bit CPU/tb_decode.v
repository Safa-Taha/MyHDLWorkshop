module tb_decode;

reg clk;
reg [31:0] fetched_instruction;
wire [7:0] opcode;
wire [7:0] operand1;
wire [7:0] operand2;

initial begin
    $from_myhdl(
        clk,
        fetched_instruction
    );
    $to_myhdl(
        opcode,
        operand1,
        operand2
    );
end

decode dut(
    clk,
    fetched_instruction,
    opcode,
    operand1,
    operand2
);

endmodule
