# Title:  AP2L0A Example 1. IF statement (i == j)	Filename: ex1.asm
# Author:  				Date:
# Description: Write the MIPS program for this C++ program.
#     int main()
#     {
#        int i, j;
#        int g = 30, h = 12, f = 0;
#        cin >> i >> j;
#        if (i == j) {
#           f = g + h;
#        } else {
#           f = g - h;
#        }
#        cout << f;
#     }
#   Read i and j (syscall 5) into ival and jval. Branch with bne to the else part,
#   jump over it with j. Store f (sw), then print f.
#   i = 0x10010000, j = 0x10010004, g = 0x10010008, h = 0x1001000C, f = 0x10010010.
#   Keep the .data block as it is. Do not use the pseudo-instructions blt, bgt, ble, bge.
# Input:  i and j, one integer per line (they may be negative)
# Output: f   (and f in memory after the run)
################# Data segment #####################
.data
	ival:	.word	0
	jval:	.word	0
	g:	.word	30
	h:	.word	12
	f:	.word	0
################# Code segment #####################
.text
.globl main
main:

	# TODO: implement

li $v0, 10  # Exit program
syscall
