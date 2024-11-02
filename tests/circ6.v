module circ6(A, B, C, out);

input A;
input B;
input C;

output out;

wire w;

and #(5) g1 (w,A,B);

or #(9) g2 (out,C,w);

endmodule
