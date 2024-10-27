module circ1(in0, in1, in2, in3 , sel1, sel0, out);

input in0;
input in1;
input in2;
input in3;
input sel1;
input sel0;

output out;

wire w1;
wire w2;
wire w3;
wire w4;
wire w5;
wire w6;
wire w7;
wire w8;
wire w9;
wire w10;

wire sel_not0;
wire sel_not1;

not #(2) g1 (sel_not0,sel0);
not #(2) g2 (sel_not1,sel1);


and #(5) g3 (w1,sel_not1,sel_not0);
and #(5) g4 (w2,w1,in0); 


and #(5) g5 (w3,sel_not1,sel0);
and #(5) g6 (w4,w3,in1); 


and #(5) g7 (w5,sel1,sel_not0);
and #(5) g8 (w6,w5,in2); 

and #(5) g9 (w7,sel1,sel0);
and #(5) g10 (w8,in3,w7);

or #(9) g11 (w9,w2,w4);
or #(9) g12 (w10,w6,w8);
or #(9) g13 (out,w9,w10);



endmodule;