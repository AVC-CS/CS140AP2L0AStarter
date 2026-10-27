# Title:  AP2L0A Example 3. IF statement (i < 10)	Filename: ex3.asm
# Author:  				Date:
# Description: Write the MIPS program for this C++ program.
#     int main()
#     {
#        int i;
#        int g = 30, h = 12, f = 0;
#        cin >> i;
#        if (i < 10) {
#           f = g + h;
#        } else {
#           f = g - h;
#        }
#        cout << f;
#     }
#   Read i (syscall 5) into ival. Compare with the constant 10 using slti, then beq to the
#   else part when the result is 0. Store f (sw), then print f.
#   i = 0x10010000, g = 0x10010004, h = 0x10010008, f = 0x1001000C.
#   Keep the .data block as it is. Do not use the pseudo-instructions blt, bgt, ble, bge.
# Input:  i (it may be negative)
# Output: f   (and f in memory after the run)
################# Data segment #####################
.data
	ival:	.word	0
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
