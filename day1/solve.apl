#!/usr/local/bin/dyalogscript
x←⍎¨⊃⎕NGET'input.txt'1
f←{×/x⌷⍨⊂⊃⍸2020=⊃∘.+/⍵⍴⊂x}
⎕←f 2
⎕←f 3
