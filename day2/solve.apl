#!/usr/local/bin/dyalogscript
x←⎕CSV('\W+'⎕R','⊃⎕NGET'input.txt'1)''4
⎕←+/{a b c d←⍵ ⋄ (≥∘a∧≤∘b)c+.=d}⍤1⊢x
⎕←+/{a b c d←⍵ ⋄ c≠.=a b⌷¨⊂d}⍤1⊢x
