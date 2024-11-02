module circ7(A, B, C, D, out1, out2, out3);

    input A;
    input B;
    input C;
    input D;
    
    output out1;
    output out2;
    output out3;

    wire w1;
    wire w2;
    wire w3;
    wire w4;
    wire w5;
    wire w6;
    wire w7;

    not #(2) g1 (w1,A);
    and #(5) g2 (w2,w1,B);
    or #(9) g3 (w3,C,D);
    nand #(7) g4 (out1,w2,w3);
    nand #(7) g5 (w4,w2,w3);
    nor #(1) g6 (w5,w1,w3);
    xor #(1) g7 (out2,w4,w5);
    xor #(1) g8 (w6,w4,w5);
    buf #(1) g9 (out3,w6);

endmodule