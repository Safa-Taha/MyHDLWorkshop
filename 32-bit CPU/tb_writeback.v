module tb_writeback;

reg clk;
reg [7:0] result;

initial begin
    $from_myhdl(
        clk,
        result
    );
end

writeback dut(
    clk,
    result
);

endmodule
