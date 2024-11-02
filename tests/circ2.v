`timescale 1ns/100ps 
module circ2(A, B, C_in, S, C_out); // full adder

input A;
input B;
input C_in;


output S;
output C_out;


wire w1;    
wire w2;
wire w3;
wire w4;
wire w5;

xor #(1) g1 (w1,A,B);
xor #(1) g2 (S,w1,C_in);

and #(5) g3 (w2,A,B);
and #(5) g4 (w3,A,C_in);
and #(5) g5 (w4,B,C_in);
or #(9) g6 (w5,w2,w3);
or #(9) g7 (C_out,w5,w4);

endmodule;