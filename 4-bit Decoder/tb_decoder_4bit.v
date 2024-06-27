module tb_decoder_4bit;

reg [3:0] inpu;
wire [15:0] out;
reg enable;

initial begin
    $from_myhdl(
        inpu,
        enable
    );
    $to_myhdl(
        out
    );
end

decoder_4bit dut(
    inpu,
    out,
    enable
);

endmodule
