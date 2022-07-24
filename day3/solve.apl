#!/usr/local/bin/dyalogscript
⎕IO←0
x←↑⊃⎕NGET'input.txt'1
f←{'#'+.=x⌷⍤1 2⍨(⍴x)|⍤1⊢⍵×⍤1 0⊢1↓⍳⌈(≢x)÷⊣/⍵}
⎕←f 1 3
⎕←×/f¨(1 1)(1 3)(1 5)(1 7)(2 1)
