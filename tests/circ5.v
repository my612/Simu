`timescale 1ns/1ps

  module circ4(input [1:0] in, output out, output nout);
    
    wire w0, w1;
  
    nor(w0, in[0], nout);  
    nor(w1, in[1], w0);
  
    assign out = w0;
    assign nout = w1;
    
  endmodule
