`timescale 1ns/1ps

module circ2(input A, input B, input C_in, output S, output C_out);
wire w1, w2, w3, w4;

xor(w1, A, B);
xor(S, w1, C_in);

and(w2, A, B);
and(w3, A, C_in);
and(w4, B, C_in);

or(C_out, w2, w3, w4);

endmodule