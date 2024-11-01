module circ4(in0, in1, out, nout);
    
  input in1;
  input in0;

  output out;
  output nout;

  nor #(7) g1 (out,in0,nout);  
  nor #(7) g2 (nout,in1,w0);
    
  endmodule
