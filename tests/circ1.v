`timescale 1ns/1ps

module circ1(input [3:0] in, input [1:0] sel, output out);
wire w1, w2, w3, w4, w5, w6, w7, w8;
wire [1:0] sel_not;
not(sel_not[1], sel[1]);
not(sel_not[0], sel[0]);


and(w1, sel_not[1], sel_not[0]);
and(w2, w1, in[0]); //W2


and(w3, sel_not[1], sel[0]);
and(w4, w3, in[1]); //W4


and(w5, sel[1], sel_not[0]);
and(w6, w5, in[2]); //W6

and(w7, sel[1], sel[0]);
and(w8, in[3], w7);

endmodule