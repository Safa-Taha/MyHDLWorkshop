module tb_fetch;

reg clk;
reg [31:0] instruction;
wire [31:0] fetched_instruction;

initial begin
    $from_myhdl(
        clk,
        instruction
    );
    $to_myhdl(
        fetched_instruction
    );
end

fetch dut(
    clk,
    instruction,
    fetched_instruction
);

endmodule
